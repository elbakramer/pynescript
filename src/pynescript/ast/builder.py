# Copyright 2024 Yunseong Hwang
#
# Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import re

from ast import literal_eval

from antlr4 import ParserRuleContext

from pynescript.ast import node as ast
from pynescript.ast.grammar.antlr4.parser import PinescriptParser
from pynescript.ast.grammar.antlr4.visitor import PinescriptParserVisitor


class PinescriptASTLocator:
    # ruff: noqa: N802

    def _getLocations(self, ctx: ParserRuleContext) -> dict[str, int]:
        start = ctx.start
        stop = ctx.stop
        stop_len = stop.stop - stop.start + 1
        stop_nls = stop.text.count("\n")
        stop_nlpos = stop.text.rfind("\n")
        lineno = start.line
        col_offset = start.column
        end_lineno = stop.line + stop_nls
        end_col_offset = stop_len - stop_nlpos + 1 if stop_nls > 0 else stop.column + stop_len
        return {
            "lineno": lineno,
            "col_offset": col_offset,
            "end_lineno": end_lineno,
            "end_col_offset": end_col_offset,
        }

    def _setLocations(self, node: ast.AST, ctx: ParserRuleContext) -> ast.AST:
        for name, value in self._getLocations(ctx).items():
            setattr(node, name, value)
        return node


class PinescriptCommentParser:
    # ruff: noqa: N802

    _ASSIGNMENT_ANNOTATION_PATTERN = re.compile(r"^(//)(\s*)(@)(\s*)(version)(\s*)(=)(\s*)(.+)$")
    _SIMPLE_ANNOTATION_PATTERN = re.compile(
        r"^(//)(\s*)(@)(\s*)(description|function|returns|type|variable|strategy_alert_message)(\s+)(.+)$"
    )
    _NAMED_ANNOTATION_PATTERN = re.compile(r"^(//)(\s*)(@)(\s*)(param|field)(\s+)(\w+)(\s+)(.+)$")
    _REGION_BORDER_PATTERN = re.compile(r"^(//)(\s*)(#)(\s*)(region|endregion)$")

    def _parseComment(self, comment: str):  # noqa: C901
        m = self._ASSIGNMENT_ANNOTATION_PATTERN.match(comment)
        if m:
            kind = "@="
            parts = (m.group(5), m.group(9))
            if parts[0] in {"version"}:
                kind += "S"
            return kind, parts
        m = self._SIMPLE_ANNOTATION_PATTERN.match(comment)
        if m:
            kind = "@0"
            parts = (m.group(5), m.group(7))
            if parts[0] in {"description", "strategy_alert_message"}:
                kind += "S"
            elif parts[0] in {"function", "returns"}:
                kind += "F"
            elif parts[0] in {"type"}:
                kind += "T"
            elif parts[0] in {"variable"}:
                kind += "V"
            return kind, parts
        m = self._NAMED_ANNOTATION_PATTERN.match(comment)
        if m:
            kind = "@1"
            parts = (m.group(5), m.group(7), m.group(9))
            if parts[0] in {"param"}:
                kind += "F"
            elif parts[0] in {"field"}:
                kind += "T"
            return kind, parts
        m = self._REGION_BORDER_PATTERN.match(comment)
        if m:
            kind = "#"
            parts = (m.group(5),)
            return kind, parts
        kind = "//"
        parts = (comment,)
        return kind, parts


class PinescriptASTBuilder(
    PinescriptParserVisitor,
    PinescriptASTLocator,
    PinescriptCommentParser,
):
    # ruff: noqa: N802

    def visitStart(self, ctx: PinescriptParser.StartContext):
        return self.visitChildren(ctx)

    def visitStart_script(self, ctx: PinescriptParser.Start_scriptContext):
        stmts = ctx.statements()
        body = stmts and self.visit(stmts) or []
        script = ast.Script(body)
        return script

    def visitStart_expression(self, ctx: PinescriptParser.Start_expressionContext):
        expr = ctx.expression()
        body = self.visit(expr)
        expr = ast.Expression(body)
        return expr

    def visitStatements(self, ctx: PinescriptParser.StatementsContext):
        stmts = ctx.statement()
        stmts = [self.visit(stmt) for stmt in stmts]
        stmts = [s for stmt in stmts for s in stmt]
        return stmts

    def visitStatement(self, ctx: PinescriptParser.StatementContext):
        comp = ctx.compound_statement()
        simp = ctx.simple_statements()
        if comp:
            return [self.visit(comp)]
        if simp:
            return self.visit(simp)

    def visitCompound_name_initialization(self, ctx: PinescriptParser.Compound_name_initializationContext):
        assign = ctx.variable_declaration()
        value = ctx.structure_expression()
        assign = self.visit(assign)
        value = self.visit(value)
        assign.value = value
        self._setLocations(assign, ctx)
        return assign

    def visitCompound_tuple_initialization(self, ctx: PinescriptParser.Compound_tuple_initializationContext):
        target = ctx.tuple_declaration()
        value = ctx.structure_expression()
        target = self.visit(target)
        value = self.visit(value)
        assign = ast.Assign(
            target=target,
            value=value,
        )
        self._setLocations(assign, ctx)
        return assign

    def visitCompound_reassignment(self, ctx: PinescriptParser.Compound_reassignmentContext):
        target = ctx.assignment_target()
        value = ctx.structure_expression()
        target = self.visit(target)
        value = self.visit(value)
        re_assign = ast.ReAssign(
            target=target,
            value=value,
        )
        self._setLocations(re_assign, ctx)
        return re_assign

    def visitCompound_augassignment(self, ctx: PinescriptParser.Compound_augassignmentContext):
        target = ctx.assignment_target()
        op = ctx.augassign_op()
        value = ctx.structure_expression()
        target = self.visit(target)
        op = self.visit(op)
        value = self.visit(value)
        aug_assign = ast.AugAssign(
            target=target,
            op=op,
            value=value,
        )
        self._setLocations(aug_assign, ctx)
        return aug_assign

    def visitSimple_name_initialization(self, ctx: PinescriptParser.Simple_name_initializationContext):
        assign = ctx.variable_declaration()
        value = ctx.expression()
        assign = self.visit(assign)
        value = self.visit(value)
        assign.value = value
        self._setLocations(assign, ctx)
        return assign

    def visitSimple_tuple_initialization(self, ctx: PinescriptParser.Simple_tuple_initializationContext):
        target = ctx.tuple_declaration()
        value = ctx.expression()
        target = self.visit(target)
        value = self.visit(value)
        assign = ast.Assign(
            target=target,
            value=value,
        )
        self._setLocations(assign, ctx)
        return assign

    def visitSimple_reassignment(self, ctx: PinescriptParser.Simple_reassignmentContext):
        target = ctx.assignment_target()
        value = ctx.expression()
        target = self.visit(target)
        value = self.visit(value)
        re_assign = ast.ReAssign(
            target=target,
            value=value,
        )
        self._setLocations(re_assign, ctx)
        return re_assign

    def visitSimple_augassignment(self, ctx: PinescriptParser.Simple_augassignmentContext):
        target = ctx.assignment_target()
        op = ctx.augassign_op()
        value = ctx.expression()
        target = self.visit(target)
        op = self.visit(op)
        value = self.visit(value)
        aug_assign = ast.AugAssign(
            target=target,
            op=op,
            value=value,
        )
        self._setLocations(aug_assign, ctx)
        return aug_assign

    def visitVariable_declaration(self, ctx: PinescriptParser.Variable_declarationContext):
        target = ctx.name_store()
        type_spec = ctx.type_specification()
        dec_mode = ctx.declaration_mode()
        target = self.visit(target)
        type_spec = type_spec and self.visit(type_spec)
        dec_mode = dec_mode and self.visit(dec_mode)
        assign = ast.Assign(
            target=target,
            type=type_spec,
            mode=dec_mode,
        )
        self._setLocations(assign, ctx)
        return assign

    def visitTuple_declaration(self, ctx: PinescriptParser.Tuple_declarationContext):
        elts = ctx.name_store()
        elts = [self.visit(elt) for elt in elts]
        tup = ast.Tuple(
            elts=elts,
            ctx=ast.Store(),
        )
        self._setLocations(tup, ctx)
        return tup

    def visitDeclaration_mode(self, ctx: PinescriptParser.Declaration_modeContext):
        if ctx.VARIP():
            return ast.VarIp()
        if ctx.VAR():
            return ast.Var()

    def visitAssignment_target_attribute(self, ctx: PinescriptParser.Assignment_target_attributeContext):
        value = ctx.primary_expression()
        name = ctx.name_store()
        value = self.visit(value)
        name = self.visit(name)
        attr = ast.Attribute(
            value=value,
            attr=name.id,
            ctx=ast.Store(),
        )
        self._setLocations(attr, ctx)
        return attr

    def visitAssignment_target_subscript(self, ctx: PinescriptParser.Assignment_target_subscriptContext):
        value = ctx.primary_expression()
        items = ctx.subscript_slice()
        value = self.visit(value)
        items = self.visit(items)
        sub = ast.Subscript(
            value=value,
            slice=items,
            ctx=ast.Store(),
        )
        self._setLocations(sub, ctx)
        return sub

    def visitAssignment_target_name(self, ctx: PinescriptParser.Assignment_target_nameContext):
        return self.visit(ctx.name_store())

    def visitAssignment_target_group(self, ctx: PinescriptParser.Assignment_target_groupContext):
        return self.visit(ctx.assignment_target())

    def visitAugassign_op(self, ctx: PinescriptParser.Augassign_opContext):
        if ctx.STAREQUAL():
            return ast.Mult()
        if ctx.SLASHEQUAL():
            return ast.Div()
        if ctx.PERCENTEQUAL():
            return ast.Mod()
        if ctx.PLUSEQUAL():
            return ast.Add()
        if ctx.MINEQUAL():
            return ast.Sub()

    def visitFunction_declaration(self, ctx: PinescriptParser.Function_declarationContext):
        name = ctx.name()
        args = ctx.parameter_list()
        body = ctx.local_block()
        name = self.visit(name)
        args = args and self.visit(args) or []
        body = self.visit(body)
        method = ctx.METHOD()
        export = ctx.EXPORT()
        method = 1 if method else 0
        export = 1 if export else 0
        func_def = ast.FunctionDef(
            name=name,
            args=args,
            body=body,
            method=method,
            export=export,
        )
        self._setLocations(func_def, ctx)
        return func_def

    def visitParameter_list(self, ctx: PinescriptParser.Parameter_listContext):
        params = ctx.parameter_definition()
        params = [self.visit(param) for param in params]
        return params

    def visitParameter_definition(self, ctx: PinescriptParser.Parameter_definitionContext):
        name = ctx.name_store()
        default = ctx.expression()
        type_spec = ctx.type_specification()
        name = self.visit(name)
        default = default and self.visit(default)
        type_spec = type_spec and self.visit(type_spec)
        param = ast.Param(
            name=name.id,
            default=default,
            type=type_spec,
        )
        self._setLocations(param, ctx)
        return param

    def visitType_declaration(self, ctx: PinescriptParser.Type_declarationContext):
        name = ctx.name()
        body = ctx.field_definitions()
        export = ctx.EXPORT()
        name = self.visit(name)
        body = self.visit(body)
        export = 1 if export else 0
        type_def = ast.TypeDef(
            name=name,
            body=body,
            export=export,
        )
        self._setLocations(type_def, ctx)
        return type_def

    def visitEnum_declaration(self, ctx: PinescriptParser.Enum_declarationContext):
        name = ctx.name()
        body = ctx.enum_definitions()
        export = ctx.EXPORT()
        name = self.visit(name)
        body = self.visit(body)
        export = 1 if export else 0
        enum_def = ast.EnumDef(
            name=name,
            body=body,
            export=export,
        )
        self._setLocations(enum_def, ctx)
        return enum_def

    def visitField_definitions(self, ctx: PinescriptParser.Field_definitionsContext):
        defs = ctx.field_definition()
        defs = [self.visit(d) for d in defs]
        return defs

    def visitField_definition(self, ctx: PinescriptParser.Field_definitionContext):
        target = ctx.name_store()
        target = self.visit(target)
        value = ctx.expression()
        value = value and self.visit(value)
        type_spec = ctx.type_specification()
        type_spec = self.visit(type_spec)
        stmt = ast.Assign(
            target=target,
            value=value,
            type=type_spec,
        )
        self._setLocations(stmt, ctx)
        return stmt

    def visitEnum_definitions(self, ctx: PinescriptParser.Enum_definitionsContext):
        defs = ctx.enum_definition()
        defs = [self.visit(d) for d in defs]
        return defs

    def visitEnum_definition(self, ctx: PinescriptParser.Enum_definitionContext):
        target = ctx.name_store()
        target = self.visit(target)
        value = ctx.expression()
        value = value and self.visit(value)
        stmt = ast.Assign(
            target=target,
            value=value,
        )
        self._setLocations(stmt, ctx)
        return stmt

    def visitStructure_statement(self, ctx: PinescriptParser.Structure_statementContext):
        struct = ctx.structure()
        struct = self.visit(struct)
        stmt = ast.Expr(struct)
        self._setLocations(stmt, ctx)
        return stmt

    def visitStructure_expression(self, ctx: PinescriptParser.Structure_expressionContext):
        struct = ctx.structure()
        struct = self.visit(struct)
        expr = struct
        self._setLocations(expr, ctx)
        return expr

    def visitIf_structure_elif(self, ctx: PinescriptParser.If_structure_elifContext):
        test = ctx.expression()
        body = ctx.local_block()
        orelse = ctx.elif_structure()
        test = self.visit(test)
        body = self.visit(body)
        orelse = self.visit(orelse)
        if_struct = ast.If(
            test=test,
            body=body,
            orelse=orelse,
        )
        self._setLocations(if_struct, ctx)
        return if_struct

    def visitIf_structure_else(self, ctx: PinescriptParser.If_structure_elseContext):
        test = ctx.expression()
        body = ctx.local_block()
        orelse = ctx.else_block()
        test = self.visit(test)
        body = self.visit(body)
        orelse = orelse and self.visit(orelse) or []
        if_struct = ast.If(
            test=test,
            body=body,
            orelse=orelse,
        )
        self._setLocations(if_struct, ctx)
        return if_struct

    def visitElif_structure_elif(self, ctx: PinescriptParser.Elif_structure_elifContext):
        test = ctx.expression()
        body = ctx.local_block()
        orelse = ctx.elif_structure()
        test = self.visit(test)
        body = self.visit(body)
        orelse = self.visit(orelse)
        elif_struct = ast.If(
            test=test,
            body=body,
            orelse=orelse,
        )
        self._setLocations(elif_struct, ctx)
        elif_struct = ast.Expr(elif_struct)
        self._setLocations(elif_struct, ctx)
        return [elif_struct]

    def visitElif_structure_else(self, ctx: PinescriptParser.Elif_structure_elseContext):
        test = ctx.expression()
        body = ctx.local_block()
        orelse = ctx.else_block()
        test = self.visit(test)
        body = self.visit(body)
        orelse = orelse and self.visit(orelse) or []
        elif_struct = ast.If(
            test=test,
            body=body,
            orelse=orelse,
        )
        self._setLocations(elif_struct, ctx)
        elif_struct = ast.Expr(elif_struct)
        self._setLocations(elif_struct, ctx)
        return [elif_struct]

    def visitElse_block(self, ctx: PinescriptParser.Else_blockContext):
        return self.visit(ctx.local_block())

    def visitFor_structure_to(self, ctx: PinescriptParser.For_structure_toContext):
        target = ctx.for_iterator()
        start = ctx.expression(0)
        end = ctx.expression(1)
        step = ctx.expression(2)
        body = ctx.local_block()
        target = self.visit(target)
        start = self.visit(start)
        end = self.visit(end)
        step = step and self.visit(step)
        body = self.visit(body)
        for_struct = ast.ForTo(
            target=target,
            start=start,
            end=end,
            body=body,
            step=step,
        )
        self._setLocations(for_struct, ctx)
        return for_struct

    def visitFor_structure_in(self, ctx: PinescriptParser.For_structure_inContext):
        target = ctx.for_iterator()
        iterable = ctx.expression()
        body = ctx.local_block()
        target = self.visit(target)
        iterable = self.visit(iterable)
        body = self.visit(body)
        for_struct = ast.ForIn(
            target=target,
            iter=iterable,
            body=body,
        )
        self._setLocations(for_struct, ctx)
        return for_struct

    def visitWhile_structure(self, ctx: PinescriptParser.While_structureContext):
        test = ctx.expression()
        body = ctx.local_block()
        test = self.visit(test)
        body = self.visit(body)
        while_struct = ast.While(
            test=test,
            body=body,
        )
        self._setLocations(while_struct, ctx)
        return while_struct

    def visitSwitch_structure(self, ctx: PinescriptParser.Switch_structureContext):
        cases = ctx.switch_cases()
        subject = ctx.expression()
        cases = self.visit(cases)
        subject = subject and self.visit(subject)
        switch_struct = ast.Switch(
            cases=cases,
            subject=subject,
        )
        self._setLocations(switch_struct, ctx)
        return switch_struct

    def visitSwitch_cases(self, ctx: PinescriptParser.Switch_casesContext):
        pattern_cases = ctx.switch_pattern_case()
        default_case = ctx.switch_default_case()
        cases = [self.visit(case) for case in pattern_cases]
        if default_case:
            case = self.visit(default_case)
            cases.append(case)
        return cases

    def visitSwitch_pattern_case(self, ctx: PinescriptParser.Switch_pattern_caseContext):
        body = ctx.local_block()
        pattern = ctx.expression()
        body = self.visit(body)
        pattern = self.visit(pattern)
        case = ast.Case(
            body=body,
            pattern=pattern,
        )
        self._setLocations(case, ctx)
        return case

    def visitSwitch_default_case(self, ctx: PinescriptParser.Switch_default_caseContext):
        body = ctx.local_block()
        body = self.visit(body)
        case = ast.Case(
            body=body,
        )
        self._setLocations(case, ctx)
        return case

    def visitIndented_local_block(self, ctx: PinescriptParser.Indented_local_blockContext):
        return self.visit(ctx.statements())

    def visitInline_local_block(self, ctx: PinescriptParser.Inline_local_blockContext):
        return self.visit(ctx.statement())

    def visitSimple_statements(self, ctx: PinescriptParser.Simple_statementsContext):
        stmts = ctx.simple_statement()
        stmts = [self.visit(stmt) for stmt in stmts]
        return stmts

    def visitExpression_statement(self, ctx: PinescriptParser.Expression_statementContext):
        expr = ctx.expression()
        expr = self.visit(expr)
        stmt = ast.Expr(
            value=expr,
        )
        self._setLocations(stmt, ctx)
        return stmt

    def visitConditional_expression_rule(self, ctx: PinescriptParser.Conditional_expression_ruleContext):
        test = self.visit(ctx.disjunction_expression())
        body, orelse = (self.visit(expr) for expr in ctx.expression())
        expr = ast.Conditional(
            test=test,
            body=body,
            orelse=orelse,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitDisjunction_expression_rule(self, ctx: PinescriptParser.Disjunction_expression_ruleContext):
        exprs = ctx.conjunction_expression()
        exprs = [self.visit(expr) for expr in exprs]
        expr = ast.BoolOp(
            op=ast.Or(),
            values=exprs,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitConjunction_expression_rule(self, ctx: PinescriptParser.Conjunction_expression_ruleContext):
        exprs = ctx.equality_expression()
        exprs = [self.visit(expr) for expr in exprs]
        expr = ast.BoolOp(
            op=ast.And(),
            values=exprs,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitEquality_expression_rule(self, ctx: PinescriptParser.Equality_expression_ruleContext):
        expr = ctx.inequality_expression()
        expr = self.visit(expr)
        pairs = ctx.equality_trailing_pair()
        pairs = [self.visit(pair) for pair in pairs]
        ops = [pair[0] for pair in pairs]
        comparators = [pair[1] for pair in pairs]
        expr = ast.Compare(
            left=expr,
            ops=ops,
            comparators=comparators,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitInequality_expression_rule(self, ctx: PinescriptParser.Inequality_expression_ruleContext):
        expr = ctx.additive_expression()
        expr = self.visit(expr)
        pairs = ctx.inequality_trailing_pair()
        pairs = [self.visit(pair) for pair in pairs]
        ops = [pair[0] for pair in pairs]
        comparators = [pair[1] for pair in pairs]
        expr = ast.Compare(
            left=expr,
            ops=ops,
            comparators=comparators,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitEqual_trailing_pair(self, ctx: PinescriptParser.Equal_trailing_pairContext):
        return (ast.Eq(), self.visit(ctx.inequality_expression()))

    def visitNot_equal_trailing_pair(self, ctx: PinescriptParser.Not_equal_trailing_pairContext):
        return (ast.NotEq(), self.visit(ctx.inequality_expression()))

    def visitLess_than_equal_trailing_pair(self, ctx: PinescriptParser.Less_than_equal_trailing_pairContext):
        return (ast.LtE(), self.visit(ctx.additive_expression()))

    def visitLess_than_trailing_pair(self, ctx: PinescriptParser.Less_than_trailing_pairContext):
        return (ast.Lt(), self.visit(ctx.additive_expression()))

    def visitGreater_than_equal_trailing_pair(self, ctx: PinescriptParser.Greater_than_equal_trailing_pairContext):
        return (ast.GtE(), self.visit(ctx.additive_expression()))

    def visitGreater_than_trailing_pair(self, ctx: PinescriptParser.Greater_than_trailing_pairContext):
        return (ast.Gt(), self.visit(ctx.additive_expression()))

    def visitAdditive_op(self, ctx: PinescriptParser.Additive_opContext):
        if ctx.PLUS():
            return ast.Add()
        if ctx.MINUS():
            return ast.Sub()

    def visitAdditive_expression(self, ctx: PinescriptParser.Additive_expressionContext):
        if ctx.additive_op():
            op = ctx.additive_op()
            op = self.visit(op)
            left = ctx.additive_expression()
            right = ctx.multiplicative_expression()
            left = self.visit(left)
            right = self.visit(right)
            expr = ast.BinOp(
                left=left,
                op=op,
                right=right,
            )
            self._setLocations(expr, ctx)
            return expr
        else:
            return self.visit(ctx.multiplicative_expression())

    def visitMultiplicative_op(self, ctx: PinescriptParser.Multiplicative_opContext):
        if ctx.STAR():
            return ast.Mult()
        if ctx.SLASH():
            return ast.Div()
        if ctx.PERCENT():
            return ast.Mod()

    def visitMultiplicative_expression(self, ctx: PinescriptParser.Multiplicative_expressionContext):
        if ctx.multiplicative_op():
            op = ctx.multiplicative_op()
            op = self.visit(op)
            left = ctx.multiplicative_expression()
            right = ctx.unary_expression()
            left = self.visit(left)
            right = self.visit(right)
            expr = ast.BinOp(
                left=left,
                op=op,
                right=right,
            )
            self._setLocations(expr, ctx)
            return expr
        else:
            return self.visit(ctx.unary_expression())

    def visitUnary_op(self, ctx: PinescriptParser.Unary_opContext):
        if ctx.NOT():
            return ast.Not()
        if ctx.PLUS():
            return ast.UAdd()
        if ctx.MINUS():
            return ast.USub()

    def visitUnary_expression(self, ctx: PinescriptParser.Unary_expressionContext):
        if ctx.unary_op():
            op = ctx.unary_op()
            op = self.visit(op)
            operand = ctx.unary_expression()
            operand = self.visit(operand)
            expr = ast.UnaryOp(
                op=op,
                operand=operand,
            )
            self._setLocations(expr, ctx)
            return expr
        else:
            return self.visit(ctx.primary_expression())

    def visitPrimary_expression_subscript(self, ctx: PinescriptParser.Primary_expression_subscriptContext):
        value = ctx.primary_expression()
        items = ctx.subscript_slice()
        value = self.visit(value)
        items = self.visit(items)
        expr = ast.Subscript(
            value=value,
            slice=items,
            ctx=ast.Load(),
        )
        self._setLocations(expr, ctx)
        return expr

    def visitPrimary_expression_call(self, ctx: PinescriptParser.Primary_expression_callContext):
        func = ctx.primary_expression()
        spec = ctx.template_spec_suffix()
        args = ctx.argument_list()
        func = self.visit(func)
        if spec:
            spec_args = self.visit(spec)
            func = ast.Specialize(
                value=func,
                args=spec_args,
                lineno=func.lineno,
                col_offset=func.col_offset,
                end_lineno=spec_args.end_lineno,
                end_col_offset=spec_args.end_col_offset,
            )
        args = args and self.visit(args) or []
        expr = ast.Call(
            func=func,
            args=args,
        )
        self._setLocations(expr, ctx)
        return expr

    def visitPrimary_expression_attribute(self, ctx: PinescriptParser.Primary_expression_attributeContext):
        value = ctx.primary_expression()
        name = ctx.name_load()
        value = self.visit(value)
        name = self.visit(name)
        expr = ast.Attribute(
            value=value,
            attr=name.id,
            ctx=ast.Load(),
        )
        self._setLocations(expr, ctx)
        return expr

    def visitArgument_list(self, ctx: PinescriptParser.Argument_listContext):
        args = ctx.argument_definition()
        args = [self.visit(arg) for arg in args]
        return args

    def visitArgument_definition(self, ctx: PinescriptParser.Argument_definitionContext):
        name = ctx.name_store()
        value = ctx.expression()
        if name:
            name = self.visit(name)
            name = name.id
        value = self.visit(value)
        arg = ast.Arg(
            value=value,
            name=name,
        )
        self._setLocations(arg, ctx)
        return arg

    def visitSubscript_slice(self, ctx: PinescriptParser.Subscript_sliceContext):
        items = ctx.expression()
        items = [self.visit(item) for item in items]
        if len(items) == 1:
            items = items[0]
        else:
            items = ast.Tuple(
                elts=items,
                ctx=ast.Load(),
            )
            self._setLocations(items, ctx)
        return items

    def visitLiteral_expression(self, ctx: PinescriptParser.Literal_expressionContext):
        child = ctx.getChild(0)
        value = self.visit(child)
        expr = ast.Constant(
            value=value,
        )
        self._setLocations(expr, ctx)
        if ctx.literal_color():
            expr.kind = "#"
        return expr

    def visitLiteral_number(self, ctx: PinescriptParser.Literal_numberContext):
        text = ctx.getText()
        number = literal_eval(text)
        return number

    def visitLiteral_string(self, ctx: PinescriptParser.Literal_stringContext):
        text = ctx.getText()
        string = literal_eval(text)
        return string

    def visitLiteral_bool(self, ctx: PinescriptParser.Literal_boolContext):
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False

    def visitLiteral_color(self, ctx: PinescriptParser.Literal_colorContext):
        text = ctx.getText()
        return text

    def visitGrouped_expression(self, ctx: PinescriptParser.Grouped_expressionContext):
        return self.visit(ctx.expression())

    def visitTuple_expression(self, ctx: PinescriptParser.Tuple_expressionContext):
        elts = ctx.expression()
        elts = [self.visit(elt) for elt in elts]
        expr = ast.Tuple(
            elts=elts,
            ctx=ast.Load(),
        )
        self._setLocations(expr, ctx)
        return expr

    def visitImport_statement(self, ctx: PinescriptParser.Import_statementContext):
        namespace = ctx.name(0)
        name = ctx.name(1)
        version = ctx.literal_number()
        alias = ctx.name(2)
        namespace = self.visit(namespace)
        name = self.visit(name)
        version = self.visit(version)
        alias = alias and self.visit(alias)
        stmt = ast.Import(
            namespace=namespace,
            name=name,
            version=version,
            alias=alias,
        )
        self._setLocations(stmt, ctx)
        return stmt

    def visitBreak_statement(self, ctx: PinescriptParser.Break_statementContext):
        stmt = ast.Break()
        self._setLocations(stmt, ctx)
        return stmt

    def visitContinue_statement(self, ctx: PinescriptParser.Continue_statementContext):
        stmt = ast.Continue()
        self._setLocations(stmt, ctx)
        return stmt

    def visitType_specification(self, ctx: PinescriptParser.Type_specificationContext):
        type_qual = ctx.type_qualifier()
        ident = ctx.attributed_type_name()
        temp_spec = ctx.template_spec_suffix()
        array_suffix = ctx.array_type_suffix()
        type_spec = self.visit(ident)
        if temp_spec:
            args = self.visit(temp_spec)
            new_type_spec = ast.Specialize(
                value=type_spec,
                args=args,
            )
            self._setLocations(new_type_spec, temp_spec)
            new_type_spec.lineno = type_spec.lineno
            new_type_spec.col_offset = type_spec.col_offset
            type_spec = new_type_spec
        if array_suffix:
            new_type_spec = ast.Subscript(
                value=type_spec,
            )
            self._setLocations(new_type_spec, array_suffix)
            new_type_spec.lineno = type_spec.lineno
            new_type_spec.col_offset = type_spec.col_offset
            type_spec = new_type_spec
        if type_qual:
            qualifier = self.visit(type_qual)
            new_type_spec = ast.Qualify(
                qualifier=qualifier,
                value=type_spec,
            )
            self._setLocations(new_type_spec, type_qual)
            new_type_spec.end_lineno = type_spec.end_lineno
            new_type_spec.end_col_offset = type_spec.end_col_offset
            type_spec = new_type_spec
        return type_spec

    def visitType_qualifier(self, ctx: PinescriptParser.Type_qualifierContext):
        if ctx.CONST():
            return ast.Const()
        if ctx.INPUT():
            return ast.Input()
        if ctx.SIMPLE():
            return ast.Simple()
        if ctx.SERIES():
            return ast.Series()

    def visitAttributed_type_name(self, ctx: PinescriptParser.Attributed_type_nameContext):
        names = ctx.name_load()
        names = [self.visit(name) for name in names]
        if len(names) == 1:
            ident = names[0]
        else:
            value = names[0]
            attr = names[1]
            ident = ast.Attribute(
                value=value,
                attr=attr.id,
                ctx=ast.Load(),
                lineno=value.lineno,
                col_offset=value.col_offset,
                end_lineno=attr.end_lineno,
                end_col_offset=attr.end_col_offset,
            )
            for attr in names[2:]:
                ident = ast.Attribute(
                    value=ident,
                    attr=attr.id,
                    ctx=ast.Load(),
                    lineno=ident.lineno,
                    col_offset=ident.col_offset,
                    end_lineno=attr.end_lineno,
                    end_col_offset=attr.end_col_offset,
                )
        return ident

    def visitTemplate_spec_suffix(self, ctx: PinescriptParser.Template_spec_suffixContext):
        args = ctx.type_argument_list()
        args = args and self.visit(args)
        return args

    def visitType_argument_list(self, ctx: PinescriptParser.Type_argument_listContext):
        args = ctx.type_specification()
        args = [self.visit(arg) for arg in args]
        if len(args) == 1:
            args = args[0]
        else:
            args = ast.Tuple(
                elts=args,
                ctx=ast.Load(),
            )
            self._setLocations(args, ctx)
        return args

    def visitName(self, ctx: PinescriptParser.NameContext):
        name = ctx.getText()
        return name

    def visitName_load(self, ctx: PinescriptParser.Name_loadContext):
        name = self.visit(ctx.name())
        name = ast.Name(
            id=name,
            ctx=ast.Load(),
        )
        self._setLocations(name, ctx)
        return name

    def visitName_store(self, ctx: PinescriptParser.Name_storeContext):
        name = self.visit(ctx.name())
        name = ast.Name(
            id=name,
            ctx=ast.Store(),
        )
        self._setLocations(name, ctx)
        return name

    def visitStart_comments(self, ctx: PinescriptParser.Start_commentsContext):
        comments = ctx.comments()
        comments = self.visit(comments) if comments else []
        return comments

    def visitComments(self, ctx: PinescriptParser.CommentsContext):
        comments = ctx.comment()
        comments = [self.visit(comment) for comment in comments]
        return comments

    def visitComment(self, ctx: PinescriptParser.CommentContext):
        comment = ctx.getText()
        kind, parts = self._parseComment(comment)
        comment = ast.Comment(
            value=comment,
            kind=kind,
        )
        self._setLocations(comment, ctx)
        return comment
