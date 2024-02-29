// Copyright 2024 Yunseong Hwang
// 
// Licensed under the GNU Lesser General Public License Version 3.0 (the "License"); you may not use this file except in
// compliance with the License. You may obtain a copy of the License at
// 
// https://www.gnu.org/licenses/lgpl-3.0.en.html
// 
// Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
// an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.
// 
// SPDX-License-Identifier: LGPL-3.0-or-later

parser grammar PinescriptParser;

options {
    tokenVocab = PinescriptLexer;
    superClass = PinescriptParserBase;
}

// STARTING RULES

start: start_script;

start_script:     statements? EOF;
start_expression: expression NEWLINE? EOF;

start_comments: comments? EOF;

// STATEMENTS

statements: statement+;
statement:  compound_statement | simple_statements;

// COMPOUND_STATEMENTS

compound_statement
    : compound_assignment
    | function_declaration
    | type_declaration
    | structure_statement;

// SIMPLE STATEMENTS

simple_statements: simple_statement (COMMA simple_statement)* COMMA? NEWLINE;

simple_statement
    : simple_assignment
    | expression_statement
    | import_statement
    | break_statement
    | continue_statement;

// COMPOUND ASSIGNMENTS

compound_assignment
    : compound_variable_initialization
    | compound_reassignment
    | compound_augassignment;

compound_variable_initialization
    : compound_name_initialization
    | compound_tuple_initialization;

compound_name_initialization:  variable_declaration EQUAL structure_expression;
compound_tuple_initialization: tuple_declaration EQUAL structure_expression;

compound_reassignment:  assignment_target COLONEQUAL structure_expression;
compound_augassignment: assignment_target augassign_op structure_expression;

// FUNCTION DECLARATION

function_declaration
    : EXPORT? METHOD? name LPAR parameter_list? RPAR RARROW local_block;

parameter_list:       parameter_definition (COMMA parameter_definition)* COMMA?;
parameter_definition: type_specification? name_store (EQUAL expression)?;

// TYPE DECLARATION

type_declaration: EXPORT? TYPE name NEWLINE INDENT field_definitions DEDENT;

field_definitions: field_definition+;
field_definition:  type_specification name_store (EQUAL expression)? NEWLINE;

// STRUCTURES

structure: if_structure | for_structure | while_structure | switch_structure;

structure_statement:  structure;
structure_expression: structure;

// IF STRUCTURE

if_structure: if_structure_elif | if_structure_else;

if_structure_elif: IF expression local_block elif_structure;
if_structure_else: IF expression local_block else_block?;

elif_structure: elif_structure_elif | elif_structure_else;

elif_structure_elif: ELSE IF expression local_block elif_structure;
elif_structure_else: ELSE IF expression local_block else_block?;

else_block: ELSE local_block;

// FOR STRUCTURE

for_structure: for_structure_to | for_structure_in;

for_structure_to
    : FOR for_iterator EQUAL expression TO expression (BY expression)? local_block;
for_structure_in: FOR for_iterator IN expression local_block;

for_iterator: name_store | tuple_declaration;

// WHILE STRUCTURE

while_structure: WHILE expression local_block;

// SWITCH STRUCTURE

switch_structure: SWITCH expression? NEWLINE INDENT switch_cases DEDENT;

switch_cases: switch_pattern_case+ switch_default_case?;

switch_pattern_case: expression RARROW local_block;
switch_default_case: RARROW local_block;

// LOCAL BLOCK

local_block: indented_local_block | inline_local_block;

indented_local_block: NEWLINE INDENT statements DEDENT;
inline_local_block:   statement;

// SIMPLE ASSIGNMENTS

simple_assignment
    : simple_variable_initialization
    | simple_reassignment
    | simple_augassignment;

simple_variable_initialization
    : simple_name_initialization
    | simple_tuple_initialization;

simple_name_initialization:  variable_declaration EQUAL expression;
simple_tuple_initialization: tuple_declaration EQUAL expression;

simple_reassignment:  assignment_target COLONEQUAL expression;
simple_augassignment: assignment_target augassign_op expression;

// EXPRESSIONS

expression:           conditional_expression;
expression_statement: expression;

// CONDITIONAL TERNARY EXPRESSION

conditional_expression: conditional_expression_rule | disjunction_expression;
conditional_expression_rule
    : disjunction_expression QUESTION expression COLON expression;

// LOGICAL EXPRESSIONS

disjunction_expression: disjunction_expression_rule | conjunction_expression;
disjunction_expression_rule
    : conjunction_expression (OR conjunction_expression)+;

conjunction_expression:      conjunction_expression_rule | equality_expression;
conjunction_expression_rule: equality_expression (AND equality_expression)+;

// COMPARISON EXPRESSIONS

equality_expression:      equality_expression_rule | inequality_expression;
equality_expression_rule: inequality_expression equality_trailing_pair+;

equality_trailing_pair: equal_trailing_pair | not_equal_trailing_pair;

equal_trailing_pair:     EQEQUAL inequality_expression;
not_equal_trailing_pair: NOTEQUAL inequality_expression;

inequality_expression:      inequality_expression_rule | additive_expression;
inequality_expression_rule: additive_expression inequality_trailing_pair+;

inequality_trailing_pair
    : less_than_equal_trailing_pair
    | less_than_trailing_pair
    | greater_than_equal_trailing_pair
    | greater_than_trailing_pair;

less_than_equal_trailing_pair:    LESSEQUAL additive_expression;
less_than_trailing_pair:          LESS additive_expression;
greater_than_equal_trailing_pair: GREATEREQUAL additive_expression;
greater_than_trailing_pair:       GREATER additive_expression;

// ARITHMETIC EXPRESSIONS

additive_expression
    : additive_expression additive_op multiplicative_expression
    | multiplicative_expression;

additive_op: PLUS | MINUS;

multiplicative_expression
    : multiplicative_expression multiplicative_op unary_expression
    | unary_expression;

multiplicative_op: STAR | SLASH | PERCENT;

unary_expression: unary_op unary_expression | primary_expression;

unary_op: NOT | PLUS | MINUS;

// PRIMARY EXPRESSIONS

primary_expression
    : primary_expression DOT name_load                                  # primary_expression_attribute
    | primary_expression template_spec_suffix? LPAR argument_list? RPAR # primary_expression_call
    | primary_expression LSQB subscript_slice RSQB                      # primary_expression_subscript
    | atomic_expression                                                 # primary_expression_fallback;

argument_list:       argument_definition (COMMA argument_definition)* COMMA?;
argument_definition: (name_store EQUAL)? expression;

subscript_slice: expression (COMMA expression)* COMMA?;

// ATOMIC EXPRESSIONS

atomic_expression
    : name_load
    | literal_expression
    | grouped_expression
    | tuple_expression;

literal_expression
    : literal_number
    | literal_string
    | literal_bool
    | literal_color;

literal_number: NUMBER;
literal_string: STRING;
literal_bool:   TRUE | FALSE;
literal_color:  COLOR;

grouped_expression: LPAR expression RPAR;
tuple_expression:   LSQB expression (COMMA expression)* COMMA? RSQB;

// IMPORT

import_statement: IMPORT name SLASH name SLASH literal_number (AS name)?;

// LOOP CONTROLS

break_statement:    BREAK;
continue_statement: CONTINUE;

// VARIABLE DECLARATION AND ASSIGNMENT RELATED SEGMENTS

variable_declaration: declaration_mode? type_specification? name_store;
tuple_declaration:    LSQB name_store (COMMA name_store)* COMMA? RSQB;

declaration_mode: VARIP | VAR;

assignment_target
    : assignment_target_attribute
    | assignment_target_subscript
    | assignment_target_name
    | assignment_target_group;

assignment_target_attribute: primary_expression DOT name_store;
assignment_target_subscript: primary_expression LSQB subscript_slice RSQB;
assignment_target_name:      name_store;
assignment_target_group:     LPAR assignment_target RPAR;

augassign_op: STAREQUAL | SLASHEQUAL | PERCENTEQUAL | PLUSEQUAL | MINEQUAL;

// TYPE SPECIFICATION

type_specification
    : type_qualifier? attributed_type_name template_spec_suffix? array_type_suffix?;

type_qualifier:       CONST | INPUT | SIMPLE | SERIES;
attributed_type_name: name_load (DOT name_load)*;

template_spec_suffix: LESS type_argument_list? GREATER;
array_type_suffix:    LSQB RSQB;

type_argument_list: type_specification (COMMA type_specification)* COMMA?;

// NAME WITH SOFT KEYWORDS

name: NAME | TYPE | METHOD | CONST | INPUT | SIMPLE | SERIES;

name_load:  name;
name_store: name;

// COMMENTS

comments: comment+;
comment:  COMMENT;