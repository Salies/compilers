from __future__ import annotations
from typing import Optional
from tools.LangGrammar import LangGrammar
from tools.LangGrammarVisitor import LangGrammarVisitor

class Symbol:
    def __init__(self: Symbol, name: str, type: str):
        self.name = name
        self.type = type

class Scope:
    def __init__(self, scope_name: str, enclosing_scope: Optional[Scope] = None):
        self.scope_name = scope_name
        self.enclosing_scope: Optional[Scope] = enclosing_scope
        self.symbols = {}

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)
    
# Objetivos da análise semântica:
# * Variável ou procedimento não declarado
# * Variável ou procedimento declarado mais de uma vez
# * Incompatibilidade de parâmetros formais e reais: número, ordeme tipo
# * Uso de variáveis variáveis de escopo inadequado
# * Atribuição de um inteiro a um booleano
# * Divisão que não é entre números inteiros
# * Variável declarada e nunca utilizada
# * Read e write com variáveis de tipo diferentes
# * Tratamento de escopo
#   - Erro: variável local a um procedimento utilizada no programa principa

# Esta classe herda e sobrescreve o visitor do ANTLR para fazer a análise semântica
class SemanticAna(LangGrammarVisitor):
    
    def __init__(self, errorListener):
        self.current_scope: Optional[Scope] = None
        self.errorListener = errorListener


    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope


    def exitScope(self):
        self.current_scope = self.current_scope.enclosing_scope

    # Variável não declarada
    # Variáveis só aparecem em dois contextos, além de sua declaração:
    # Atribuição (atribuicao) e fator

    # Visit a parse tree produced by LangGrammar#atribuicao.
    def visitAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        nome_variavel = ctx.variavel().getText()
        print('visitAtribuicao', nome_variavel)