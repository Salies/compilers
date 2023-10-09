parser grammar LangGrammar;
options { tokenVocab=LangLexer; }
    
numero: (INT | REAL);

relacao:
    ( EQUAL | DIFF | LT | LTE | GT | GTE ) ;

termo:
    fator ( ( MUL | INT_DIV | AND ) fator )* ;

expressaoSimples:
    ( SUM | SUB )? termo expressaoSimples1 ;

expressaoSimples1:
    ( ( SUM | SUB | OR ) termo expressaoSimples1 )? ;

expressao:
    expressaoSimples expressao1;

expressao1:
    (relacao expressaoSimples)? ;

fator:
    ( variavel | numero | ( LP expressao RP ) | ( NOT fator ) ) ;

variavel:
    IDENTIFICADOR variavel1 ;

variavel1:
    expressao? ;

declaracaoVariavel: 
    tipo listaIdentificadores ;

listaIdentificadores: 
    IDENTIFICADOR listaIdentificadores1;

listaIdentificadores1:
    ( COMMA IDENTIFICADOR listaIdentificadores1 )?  ;

parteDeclaracaoVariavel: 
    declaracaoVariavel parteDeclaracaoVariavel1 SEMICOLON + EOF ;

parteDeclaracaoVariavel1:
    ( SEMICOLON declaracaoVariavel parteDeclaracaoVariavel1 )? ;

tipo:
    ( TYPE_BOOL | TYPE_INT ) ;