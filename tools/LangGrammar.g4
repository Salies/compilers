parser grammar LangGrammar;
options { tokenVocab=LangLexer; }

numero: (INT | REAL);

relacao:
    ( EQUAL | DIFF | LT | LTE | GT | GTE ) ;

termo:
    fator termo1 ;

termo1:
    ( ( MUL | INT_DIV | AND ) fator termo1 )? ;

expressaoSimples:
    ( SUM | SUB )? termo expressaoSimples1 ;

expressaoSimples1:
    ( ( SUM | SUB | OR ) termo expressaoSimples1 )? ;

expressao:
    expressaoSimples expressao1;

expressao1:
    (relacao expressaoSimples)? ;

fator:
    ( variavel | numero | ( LP expressao RP ) | ( NOT fator ) | CONST_TRUE | CONST_FALSE ) ;

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
    declaracaoVariavel parteDeclaracaoVariavel1 SEMICOLON ;

parteDeclaracaoVariavel1:
    ( SEMICOLON declaracaoVariavel parteDeclaracaoVariavel1 )? ;

tipo:
    ( TYPE_BOOL | TYPE_INT ) ;

programa:
    PROGRAM IDENTIFICADOR SEMICOLON
    bloco DOT + EOF;

bloco:  
    ( parteDeclaracaoVariavel )? 
    ( parteDeclaracaoSubRotina )? 
    comandoComposto ;

parteDeclaracaoSubRotina: 
    declaracaoProcedimento SEMICOLON parteDeclaracaoSubRotina1  ;

parteDeclaracaoSubRotina1:
    ( declaracaoProcedimento parteDeclaracaoSubRotina1 SEMICOLON ) ? ; 

declaracaoProcedimento: 
    PROCEDURE IDENTIFICADOR declaracaoProcedimento1 SEMICOLON bloco ;

declaracaoProcedimento1:
    ( parametrosFormais )? ;

parametrosFormais:
    LP secaoParametrosFormais parametrosFormais1 RP ;

parametrosFormais1:
    (SEMICOLON secaoParametrosFormais parametrosFormais1) ? ; 

//ADICIONADO tipo E FATORADO A REGRA secaoParametrosFormais
secaoParametrosFormais:
    ( VAR )? listaIdentificadores COLON secaoParametrosFormais1 ;
// todo verificar identificador
secaoParametrosFormais1:
    IDENTIFICADOR | tipo ;
// todo

comandoComposto:
    BEGIN comando comandoComposto1 END ;

comandoComposto1:
    ( SEMICOLON comando comandoComposto1 ) ? ;

comando:
    ( atribuicao | chamadaProcedimento | comandoComposto | comandoCondicional | comandoRepetitivo1 ) ;

atribuicao:
    variavel ATTRIB expressao ;

//ADICIONADO READ_PROC e PROC_WRITE
chamadaProcedimento:
    (IDENTIFICADOR | PROC_READ | PROC_WRITE) chamadaProcedimento1 ;
//

chamadaProcedimento1:
    ( LP listaExpressao RP )? ;

comandoCondicional:
    IF expressao THEN comando comandoCondicional1 ;

comandoCondicional1:
    (ELSE comando)? ;

comandoRepetitivo1:
    WHILE expressao DO comando ;

listaExpressao:
    expressao listaExpressao1 ;

listaExpressao1:
    ( COMMA expressao listaExpressao1 ) ? ;