// Base ANTLR para o analisador léxico
// Calculadora
// Autores:
// Daniel Serezane
// Gabriel Nozawa
lexer grammar LangLexer;

INT: [0-9]+;
REAL: [0-9]+'.'[0-9]+;

SUM: '+';
MUL: '*';
DIV: '/';
SUB: '-';

LP: '(';
RP: ')';

WS: [ \t\n\r\f]+ -> skip ;

INVALID_TOKEN: INVALID+? ;
INVALID: . ;