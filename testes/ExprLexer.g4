// DELETE THIS CONTENT IF YOU PUT COMBINED GRAMMAR IN Parser TAB
lexer grammar ExprLexer;

AND : 'and' ;
OR : 'or' ;

INT : [0-9]+ ;
ID: [a-zA-Z_]+[0-9]* ;
ERR_TOKEN: . ;
WS : ' ' -> skip;