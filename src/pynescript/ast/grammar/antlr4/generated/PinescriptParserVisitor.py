# Generated from src/pynescript/ast/grammar/antlr4/resource/PinescriptParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PinescriptParser import PinescriptParser
else:
    from PinescriptParser import PinescriptParser

# This class defines a complete generic visitor for a parse tree produced by PinescriptParser.

class PinescriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PinescriptParser#start.
    def visitStart(self, ctx:PinescriptParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#start_script.
    def visitStart_script(self, ctx:PinescriptParser.Start_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#start_expression.
    def visitStart_expression(self, ctx:PinescriptParser.Start_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#start_comments.
    def visitStart_comments(self, ctx:PinescriptParser.Start_commentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#statements.
    def visitStatements(self, ctx:PinescriptParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#statement.
    def visitStatement(self, ctx:PinescriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_statement.
    def visitCompound_statement(self, ctx:PinescriptParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_statements.
    def visitSimple_statements(self, ctx:PinescriptParser.Simple_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_statement.
    def visitSimple_statement(self, ctx:PinescriptParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_assignment.
    def visitCompound_assignment(self, ctx:PinescriptParser.Compound_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_variable_initialization.
    def visitCompound_variable_initialization(self, ctx:PinescriptParser.Compound_variable_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_name_initialization.
    def visitCompound_name_initialization(self, ctx:PinescriptParser.Compound_name_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_tuple_initialization.
    def visitCompound_tuple_initialization(self, ctx:PinescriptParser.Compound_tuple_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_reassignment.
    def visitCompound_reassignment(self, ctx:PinescriptParser.Compound_reassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#compound_augassignment.
    def visitCompound_augassignment(self, ctx:PinescriptParser.Compound_augassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#function_declaration.
    def visitFunction_declaration(self, ctx:PinescriptParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#parameter_list.
    def visitParameter_list(self, ctx:PinescriptParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#parameter_definition.
    def visitParameter_definition(self, ctx:PinescriptParser.Parameter_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#type_declaration.
    def visitType_declaration(self, ctx:PinescriptParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#field_definitions.
    def visitField_definitions(self, ctx:PinescriptParser.Field_definitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#field_definition.
    def visitField_definition(self, ctx:PinescriptParser.Field_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#enum_declaration.
    def visitEnum_declaration(self, ctx:PinescriptParser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#enum_definitions.
    def visitEnum_definitions(self, ctx:PinescriptParser.Enum_definitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#enum_definition.
    def visitEnum_definition(self, ctx:PinescriptParser.Enum_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#structure.
    def visitStructure(self, ctx:PinescriptParser.StructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#structure_statement.
    def visitStructure_statement(self, ctx:PinescriptParser.Structure_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#structure_expression.
    def visitStructure_expression(self, ctx:PinescriptParser.Structure_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#if_structure.
    def visitIf_structure(self, ctx:PinescriptParser.If_structureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#if_structure_elif.
    def visitIf_structure_elif(self, ctx:PinescriptParser.If_structure_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#if_structure_else.
    def visitIf_structure_else(self, ctx:PinescriptParser.If_structure_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#elif_structure.
    def visitElif_structure(self, ctx:PinescriptParser.Elif_structureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#elif_structure_elif.
    def visitElif_structure_elif(self, ctx:PinescriptParser.Elif_structure_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#elif_structure_else.
    def visitElif_structure_else(self, ctx:PinescriptParser.Elif_structure_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#else_block.
    def visitElse_block(self, ctx:PinescriptParser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#for_structure.
    def visitFor_structure(self, ctx:PinescriptParser.For_structureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#for_structure_to.
    def visitFor_structure_to(self, ctx:PinescriptParser.For_structure_toContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#for_structure_in.
    def visitFor_structure_in(self, ctx:PinescriptParser.For_structure_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#for_iterator.
    def visitFor_iterator(self, ctx:PinescriptParser.For_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#while_structure.
    def visitWhile_structure(self, ctx:PinescriptParser.While_structureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#switch_structure.
    def visitSwitch_structure(self, ctx:PinescriptParser.Switch_structureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#switch_cases.
    def visitSwitch_cases(self, ctx:PinescriptParser.Switch_casesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#switch_pattern_case.
    def visitSwitch_pattern_case(self, ctx:PinescriptParser.Switch_pattern_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#switch_default_case.
    def visitSwitch_default_case(self, ctx:PinescriptParser.Switch_default_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#local_block.
    def visitLocal_block(self, ctx:PinescriptParser.Local_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#indented_local_block.
    def visitIndented_local_block(self, ctx:PinescriptParser.Indented_local_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#inline_local_block.
    def visitInline_local_block(self, ctx:PinescriptParser.Inline_local_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_assignment.
    def visitSimple_assignment(self, ctx:PinescriptParser.Simple_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_variable_initialization.
    def visitSimple_variable_initialization(self, ctx:PinescriptParser.Simple_variable_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_name_initialization.
    def visitSimple_name_initialization(self, ctx:PinescriptParser.Simple_name_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_tuple_initialization.
    def visitSimple_tuple_initialization(self, ctx:PinescriptParser.Simple_tuple_initializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_reassignment.
    def visitSimple_reassignment(self, ctx:PinescriptParser.Simple_reassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#simple_augassignment.
    def visitSimple_augassignment(self, ctx:PinescriptParser.Simple_augassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#expression.
    def visitExpression(self, ctx:PinescriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#expression_statement.
    def visitExpression_statement(self, ctx:PinescriptParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#conditional_expression.
    def visitConditional_expression(self, ctx:PinescriptParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#conditional_expression_rule.
    def visitConditional_expression_rule(self, ctx:PinescriptParser.Conditional_expression_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#disjunction_expression.
    def visitDisjunction_expression(self, ctx:PinescriptParser.Disjunction_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#disjunction_expression_rule.
    def visitDisjunction_expression_rule(self, ctx:PinescriptParser.Disjunction_expression_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#conjunction_expression.
    def visitConjunction_expression(self, ctx:PinescriptParser.Conjunction_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#conjunction_expression_rule.
    def visitConjunction_expression_rule(self, ctx:PinescriptParser.Conjunction_expression_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#equality_expression.
    def visitEquality_expression(self, ctx:PinescriptParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#equality_expression_rule.
    def visitEquality_expression_rule(self, ctx:PinescriptParser.Equality_expression_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#equality_trailing_pair.
    def visitEquality_trailing_pair(self, ctx:PinescriptParser.Equality_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#equal_trailing_pair.
    def visitEqual_trailing_pair(self, ctx:PinescriptParser.Equal_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#not_equal_trailing_pair.
    def visitNot_equal_trailing_pair(self, ctx:PinescriptParser.Not_equal_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#inequality_expression.
    def visitInequality_expression(self, ctx:PinescriptParser.Inequality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#inequality_expression_rule.
    def visitInequality_expression_rule(self, ctx:PinescriptParser.Inequality_expression_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#inequality_trailing_pair.
    def visitInequality_trailing_pair(self, ctx:PinescriptParser.Inequality_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#less_than_equal_trailing_pair.
    def visitLess_than_equal_trailing_pair(self, ctx:PinescriptParser.Less_than_equal_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#less_than_trailing_pair.
    def visitLess_than_trailing_pair(self, ctx:PinescriptParser.Less_than_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#greater_than_equal_trailing_pair.
    def visitGreater_than_equal_trailing_pair(self, ctx:PinescriptParser.Greater_than_equal_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#greater_than_trailing_pair.
    def visitGreater_than_trailing_pair(self, ctx:PinescriptParser.Greater_than_trailing_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#additive_expression.
    def visitAdditive_expression(self, ctx:PinescriptParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#additive_op.
    def visitAdditive_op(self, ctx:PinescriptParser.Additive_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:PinescriptParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#multiplicative_op.
    def visitMultiplicative_op(self, ctx:PinescriptParser.Multiplicative_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#unary_expression.
    def visitUnary_expression(self, ctx:PinescriptParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#unary_op.
    def visitUnary_op(self, ctx:PinescriptParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#primary_expression_attribute.
    def visitPrimary_expression_attribute(self, ctx:PinescriptParser.Primary_expression_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#primary_expression_call.
    def visitPrimary_expression_call(self, ctx:PinescriptParser.Primary_expression_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#primary_expression_fallback.
    def visitPrimary_expression_fallback(self, ctx:PinescriptParser.Primary_expression_fallbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#primary_expression_subscript.
    def visitPrimary_expression_subscript(self, ctx:PinescriptParser.Primary_expression_subscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#argument_list.
    def visitArgument_list(self, ctx:PinescriptParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#argument_definition.
    def visitArgument_definition(self, ctx:PinescriptParser.Argument_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#subscript_slice.
    def visitSubscript_slice(self, ctx:PinescriptParser.Subscript_sliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#atomic_expression.
    def visitAtomic_expression(self, ctx:PinescriptParser.Atomic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#literal_expression.
    def visitLiteral_expression(self, ctx:PinescriptParser.Literal_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#literal_number.
    def visitLiteral_number(self, ctx:PinescriptParser.Literal_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#literal_string.
    def visitLiteral_string(self, ctx:PinescriptParser.Literal_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#literal_bool.
    def visitLiteral_bool(self, ctx:PinescriptParser.Literal_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#literal_color.
    def visitLiteral_color(self, ctx:PinescriptParser.Literal_colorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#grouped_expression.
    def visitGrouped_expression(self, ctx:PinescriptParser.Grouped_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#tuple_expression.
    def visitTuple_expression(self, ctx:PinescriptParser.Tuple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#import_statement.
    def visitImport_statement(self, ctx:PinescriptParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#break_statement.
    def visitBreak_statement(self, ctx:PinescriptParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#continue_statement.
    def visitContinue_statement(self, ctx:PinescriptParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#variable_declaration.
    def visitVariable_declaration(self, ctx:PinescriptParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#tuple_declaration.
    def visitTuple_declaration(self, ctx:PinescriptParser.Tuple_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#declaration_mode.
    def visitDeclaration_mode(self, ctx:PinescriptParser.Declaration_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#assignment_target.
    def visitAssignment_target(self, ctx:PinescriptParser.Assignment_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#assignment_target_attribute.
    def visitAssignment_target_attribute(self, ctx:PinescriptParser.Assignment_target_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#assignment_target_subscript.
    def visitAssignment_target_subscript(self, ctx:PinescriptParser.Assignment_target_subscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#assignment_target_name.
    def visitAssignment_target_name(self, ctx:PinescriptParser.Assignment_target_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#assignment_target_group.
    def visitAssignment_target_group(self, ctx:PinescriptParser.Assignment_target_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#augassign_op.
    def visitAugassign_op(self, ctx:PinescriptParser.Augassign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#type_specification.
    def visitType_specification(self, ctx:PinescriptParser.Type_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#type_qualifier.
    def visitType_qualifier(self, ctx:PinescriptParser.Type_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#attributed_type_name.
    def visitAttributed_type_name(self, ctx:PinescriptParser.Attributed_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#template_spec_suffix.
    def visitTemplate_spec_suffix(self, ctx:PinescriptParser.Template_spec_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#array_type_suffix.
    def visitArray_type_suffix(self, ctx:PinescriptParser.Array_type_suffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#type_argument_list.
    def visitType_argument_list(self, ctx:PinescriptParser.Type_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#name.
    def visitName(self, ctx:PinescriptParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#name_load.
    def visitName_load(self, ctx:PinescriptParser.Name_loadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#name_store.
    def visitName_store(self, ctx:PinescriptParser.Name_storeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#comments.
    def visitComments(self, ctx:PinescriptParser.CommentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PinescriptParser#comment.
    def visitComment(self, ctx:PinescriptParser.CommentContext):
        return self.visitChildren(ctx)



del PinescriptParser