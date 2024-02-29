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

lexer grammar PinescriptLexer;

options {
    superClass = PinescriptLexerBase;
}

tokens {
    INDENT,
    DEDENT
}

channels {
    COMMENT_CHANNEL
}

// KEYWORDS

AND:      'and';
AS:       'as';
BREAK:    'break';
BY:       'by';
CONST:    'const';
CONTINUE: 'continue';
ELSE:     'else';
EXPORT:   'export';
FALSE:    'false';
FOR:      'for';
IF:       'if';
IMPORT:   'import';
IN:       'in';
INPUT:    'input';
METHOD:   'method';
NOT:      'not';
OR:       'or';
SERIES:   'series';
SIMPLE:   'simple';
SWITCH:   'switch';
TO:       'to';
TYPE:     'type';
TRUE:     'true';
VAR:      'var';
VARIP:    'varip';
WHILE:    'while';

// PUNCTUATIONS AND OPERATORS

LPAR: '(';
RPAR: ')';
LSQB: '[';
RSQB: ']';

LESS:         '<';
GREATER:      '>';
EQUAL:        '=';
EQEQUAL:      '==';
NOTEQUAL:     '!=';
LESSEQUAL:    '<=';
GREATEREQUAL: '>=';

RARROW: '=>';

DOT:      '.';
COMMA:    ',';
COLON:    ':';
QUESTION: '?';

PLUS:    '+';
MINUS:   '-';
STAR:    '*';
SLASH:   '/';
PERCENT: '%';

PLUSEQUAL:    '+=';
MINEQUAL:     '-=';
STAREQUAL:    '*=';
SLASHEQUAL:   '/=';
PERCENTEQUAL: '%=';

COLONEQUAL: ':=';

// COMMON TOKENS

NAME:    ID_START ID_CONTINUE*;
NUMBER:  NUMBER_LITERAL;
STRING:  STRING_LITERAL;
COLOR:   COLOR_LITERAL;
NEWLINE: OS_INDEPENDENT_NL;

// WHITE SPACES, COMMENTS, MISCS

WS:          [ \t\f]+      -> channel(HIDDEN);
COMMENT:     '//' ~[\r\n]* -> channel(COMMENT_CHANNEL);
ERROR_TOKEN: .;

// FRAGMENTS

fragment STRING_LITERAL: SINGLE_QUOTED_STRING | DOUBLE_QUOTED_STRING;

fragment SINGLE_QUOTED_STRING: '\'' STRING_ITEM_FOR_SINGLE_QUOTE* '\'';
fragment DOUBLE_QUOTED_STRING: '"' STRING_ITEM_FOR_DOUBLE_QUOTE* '"';

fragment STRING_ITEM_FOR_SINGLE_QUOTE
    : STRING_CHAR_NO_SINGLE_QUOTE
    | STRING_ESCAPE_SEQ;
fragment STRING_ITEM_FOR_DOUBLE_QUOTE
    : STRING_CHAR_NO_DOUBLE_QUOTE
    | STRING_ESCAPE_SEQ;

fragment STRING_CHAR_NO_SINGLE_QUOTE: ~[\\'];
fragment STRING_CHAR_NO_DOUBLE_QUOTE: ~[\\"];

fragment STRING_ESCAPE_SEQ: '\\' .;

fragment COLOR_LITERAL: COLOR_LITERAL_RGBA | COLOR_LITERAL_RGB;

fragment COLOR_LITERAL_RGBA
    : '#' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT;
fragment COLOR_LITERAL_RGB
    : '#' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT;

fragment NUMBER_LITERAL: INTEGER | FLOAT_NUMBER | IMAG_NUMBER;

fragment INTEGER:        DEC_INTEGER | BIN_INTEGER | OCT_INTEGER | HEX_INTEGER;
fragment DEC_INTEGER:    NON_ZERO_DIGIT ('_'? DIGIT)* | '0'+ ('_'? '0')*;
fragment BIN_INTEGER:    '0' ('b' | 'B') ('_'? BIN_DIGIT)+;
fragment OCT_INTEGER:    '0' ('o' | 'O') ('_'? OCT_DIGIT)+;
fragment HEX_INTEGER:    '0' ('x' | 'X') ('_'? HEX_DIGIT)+;
fragment NON_ZERO_DIGIT: [1-9];
fragment DIGIT:          [0-9];
fragment BIN_DIGIT:      '0' | '1';
fragment OCT_DIGIT:      [0-7];
fragment HEX_DIGIT:      DIGIT | [a-f] | [A-F];

fragment FLOAT_NUMBER:   POINT_FLOAT | EXPONENT_FLOAT;
fragment POINT_FLOAT:    DIGIT_PART? FRACTION | DIGIT_PART '.';
fragment EXPONENT_FLOAT: (DIGIT_PART | POINT_FLOAT) EXPONENT;
fragment DIGIT_PART:     DIGIT ('_'? DIGIT)*;
fragment FRACTION:       '.' DIGIT_PART;
fragment EXPONENT:       ('e' | 'E') ('+' | '-')? DIGIT_PART;

fragment IMAG_NUMBER: (FLOAT_NUMBER | DIGIT_PART) ('j' | 'J');

fragment OS_INDEPENDENT_NL: '\r'? '\n';

fragment ID_START:    [a-zA-Z_];
fragment ID_CONTINUE: [a-zA-Z_0-9];