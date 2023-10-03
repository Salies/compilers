parser grammar LangParser;
options { tokenVocab=LangLexer; }
    
numero: (INT | REAL);

relacao:
    ( EQUAL | DIFF | LT | LTE | GT | GTE ) ;

termo:
    fator ( ( MUL | INT_DIV | AND ) fator )* ;

expressaoSimples:
    ( SUM | SUB )? termo ( ( SUM | SUB | OR ) termo )* ;

expressao:
    expressaoSimples (relacao expressaoSimples)? ;

fator:
    ( variavel | numero | ( LP expressao RP ) | ( NOT fator ) ) ;

variavel:
    IDENTIFICADOR expressao? ;

declaracaoVariavel: 
    tipo listaIdentificadores ;

listaIdentificadores: 
    IDENTIFICADOR ( COMMA IDENTIFICADOR )* ;

parteDeclaracaoVariavel: 
    declaracaoVariavel ( SEMICOLON declaracaoVariavel )* SEMICOLON EOF ;

tipo:
    ( TYPE_BOOL | TYPE_INT ) ;