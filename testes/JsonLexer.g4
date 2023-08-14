/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
lexer grammar JSONLexer;

STRING
   : '"' (ESC | ~ ["\\])* '"'
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;


fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;


fragment HEX
   : [0-9a-fA-F]
   ;


NUMBER
   : '-'? INT '.' [0-9] + EXP? | '-'? INT EXP | '-'? INT
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

TRUE : 'true';
FALSE : 'false';
NULL : 'null';

LCURL : '{';
RCURL : '}';
COL : ':';
COMA : ',';
LBRACK : '[';
RBRACK : ']';

WS
   : [ \t\n\r] + -> skip
   ;

NON_VALID_STRING : . ->pushMode(MODE_ERR);

mode MODE_ERR;
WS1
   : [ \t\n\r] + -> skip
   ;
COL1 : ':' ->popMode;
MY_ERR_TOKEN : ~[':']* ->type(NON_VALID_STRING);