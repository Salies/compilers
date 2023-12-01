from __future__ import annotations
from typing import Optional
from tools.LangGrammar import LangGrammar
from tools.LangGrammarVisitor import LangGrammarVisitor

class Symbol:
    def __init__(self: Symbol, name: str, pos: int):
        self.name = name
        self.pos_stack = pos

class Scope:
    def __init__(self, scope_name: str, enclosing_scope: Optional[Scope] = None):
        self.scope_name = scope_name
        self.enclosing_scope: Optional[Scope] = enclosing_scope
        self.symbols: dict[str, Symbol] = {}

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)

class CodeGenerator(LangGrammarVisitor):
    
    def __init__(self, errorListener):
        self.current_scope: Scope = Scope("global")
        self.errorListener = errorListener
        self.generated_code = []
        self.historico_variavel = []

    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope

    def exitScope(self):
        if self.current_scope.enclosing_scope is not None:
            self.current_scope = self.current_scope.enclosing_scope

    def visitPrograma(self, ctx: LangGrammar.ProgramaContext):
        self.generated_code.append("INPP\n")
        self.visitChildren(ctx)
        self.generated_code.append("PARA\n")

    def visitListaIdentificadores(self, ctx: LangGrammar.ListaIdentificadoresContext):
        id = ctx.IDENTIFICADOR()
        if(id != None):
            nome_variavel = id.getText()
            pos_stack = int(len(self.current_scope.symbols))
            print("nome_variavel: ", nome_variavel)
            print("posicao: ", pos_stack)
            symbol = Symbol(nome_variavel, pos_stack)
            self.current_scope.define(symbol)
            self.generated_code.append("AMEM 1\n")
        self.visitChildren(ctx)

    def visitListaIdentificadores1(self, ctx: LangGrammar.ListaIdentificadoresContext):
        id = ctx.IDENTIFICADOR()
        if(id != None):
            nome_variavel = id.getText()
            pos_stack = int(len(self.current_scope.symbols))
            print("posicao: ", pos_stack)
            symbol = Symbol(nome_variavel, pos_stack)
            self.current_scope.define(symbol)
            self.generated_code.append("AMEM 1\n")
        self.visitChildren(ctx)

    def visitExpressao1(self, ctx: LangGrammar.Expressao1Context):
        relacao = ctx.relacao()
        if(relacao != None):
            print(len(self.generated_code))
            # self.visitChildren(ctx.expressaoSimples())
            # self.visitChildren(ctx.relacao())
            self.visitChildren(ctx)
            if(relacao.EQUAL() != None):
                print("EQ")
                self.generated_code.append("CMIG\n")
            elif(relacao.DIFF() != None):
                print("DIF")
                self.generated_code.append("CMDG\n")
            elif(relacao.LT() != None):
                print("MEN")
                self.generated_code.append("CMME\n")
            elif(relacao.LTE() != None):
                print("MEQ")
                self.generated_code.append("CMEG\n")
            elif(relacao.GT() != None):
                print("MAI")
                self.generated_code.append("CMMA\n")
            elif(relacao.GTE() != None):
                print("MAQ")
                self.generated_code.append("CMAG\n")
            

    # def visitRelacao(self, ctx:LangGrammar.RelacaoContext ):
    #     if(ctx.EQUAL() != None):
    #         print("EQ")
    #         self.generated_code.append("CMIG\n")
    #     elif(ctx.DIFF() != None):
    #         print("DIF")
    #         self.generated_code.append("CMDG\n")
    #     elif(ctx.LT() != None):
    #         print("MEN")
    #         self.generated_code.append("CMME\n")
    #     elif(ctx.LTE() != None):
    #         print("MEQ")
    #         self.generated_code.append("CMEG\n")
    #     elif(ctx.GT() != None):
    #         print("MAI")
    #         self.generated_code.append("CMMA\n")
    #     elif(ctx.GTE() != None):
    #         print("MAQ")
    #         self.generated_code.append("CMAG\n")

    def visitExpressaoSimples(self, ctx:LangGrammar.ExpressaoSimplesContext ):
        if(ctx.SUB() != None):
            if(type(ctx.parentCtx.parentCtx) == LangGrammar.Variavel1Context):
                self.visitChildren(ctx)
                self.generated_code.append("SUBT\n")
            else:
                instruction_reminder = len(self.generated_code)
                self.visitChildren(ctx.termo())
                self.generated_code.insert(instruction_reminder+1, "INVR\n")
                self.visitChildren(ctx.expressaoSimples1())
        elif(ctx.SUM() != None):
            self.visitChildren(ctx)
            self.generated_code.append("SOMA\n")
        else:
            self.visitChildren(ctx)

    def visitExpressaoSimples1(self, ctx:LangGrammar.ExpressaoSimples1Context ):
        self.visitChildren(ctx)
        if(ctx.SUB() != None):
            self.generated_code.append("SUBT\n")
        elif(ctx.SUM() != None):
            self.generated_code.append("SOMA\n")
        elif(ctx.OR() != None):
            self.generated_code.append("DISJ\n")

    def visitFator(self, ctx: LangGrammar.FatorContext):
        if(ctx.variavel() != None):
            #verificar como pegar a posicao da variavel no stack de dados
            variavel = ctx.variavel()
            id = variavel.IDENTIFICADOR()
            nome_variavel = id.getText()
            self.historico_variavel.append(nome_variavel)
            stack_position = self.current_scope.resolve(nome_variavel).pos_stack
            self.generated_code.append(f"CRVR {stack_position}\n")
            # pass
        elif(ctx.numero() != None):
            num = int(ctx.numero().getText())
            self.generated_code.append(f"CRVL {num}\n")
        #TODO verificar como representar booleanos na MEPA
        elif(ctx.CONST_FALSE() != None):
            self.generated_code.append(f"CRVL 0\n")
        elif(ctx.CONST_TRUE() != None):
            self.generated_code.append("CRVL 1\n")
        self.visitChildren(ctx)
        if(ctx.NOT() != None):
            self.generated_code.append("NEGA\n")
        
    #TODO
    def visitTermo1(self, ctx: LangGrammar.Termo1Context):
        #resolve primeiro o fator e depois resolve o termo
        if(ctx.children != None):
            self.visitChildren(ctx)

            if(ctx.MUL() != None):
                self.generated_code.append(f"MULT\n")

            elif(ctx.INT_DIV() != None):
                self.generated_code.append(f"DIVI\n")

            elif(ctx.AND() != None):
                self.generated_code.append(f"CONJ\n")
            

    def visitComandoRepetitivo1(self, ctx:LangGrammar.ComandoRepetitivo1Context):
        inicio_laco = len(self.generated_code)
        self.generated_code.append("NADA\n")
        #visita a expressao e adiciona um placeholder para indicar o final do bloco de repeticao
        self.visitChildren(ctx.expressao())
        instruction_reminder = len(self.generated_code)
        #adicionei placeholder ao inves de vazio para debug
        self.generated_code.append("PLACEHOLDER COMANDO REPETITIVO\n")
        self.visitChildren(ctx.comando())
        self.generated_code.append(f"DSVS {inicio_laco}\n")
        self.generated_code[instruction_reminder] = f"DSVF {len(self.generated_code)}\n"
        self.generated_code.append("NADA\n")

    def visitAtribuicao(self, ctx: LangGrammar.AtribuicaoContext):
        variavel = ctx.variavel()
        id = variavel.IDENTIFICADOR()
        nome_variavel = id.getText()
        self.historico_variavel.append(nome_variavel)
        symbol = self.current_scope.resolve(nome_variavel)
        num = symbol.pos_stack
        self.visitChildren(ctx)
        self.generated_code.append(f"ARMZ {num}\n")

    def visitComandoCondicional(self, ctx: LangGrammar.ComandoCondicionalContext):
        self.visitChildren(ctx.expressao())
        instruction_reminder = len(self.generated_code)
        self.generated_code.append("PLACEHOLDER COMANDO CONDICIONAL\n")
        #armazena todas as instrucoes caso verdadeiro
        self.visitChildren(ctx.comando())
        #retorna a instrucao placeholder e substituição pelo valor de instrução atual
        self.generated_code[instruction_reminder] = f"DSVF {len(self.generated_code)}\n"
        self.generated_code.append("NADA\n")
        instruction_reminder = len(self.generated_code)
        self.visitChildren(ctx.comandoCondicional1())
        current_instruction = len(self.generated_code)
        if(instruction_reminder != current_instruction):
            self.generated_code.insert(instruction_reminder, f"DSVS {current_instruction+1}\n")
            self.generated_code.append("NADA\n")

    def visitChamadaProcedimento(self, ctx: LangGrammar.ChamadaProcedimentoContext):
        if(ctx.PROC_READ() != None):
            new_instruction_pointer = len(self.generated_code)
            self.visitChildren(ctx)
            #descarta as operacoes inuteis
            while(new_instruction_pointer != len(self.generated_code)):
                self.generated_code.pop()
            for variavel in self.historico_variavel:
                #permite a entrada de multiplas variaveis numa mesma chamada
                self.generated_code.append("LEIT\n")
                stack_position = self.current_scope.resolve(variavel).pos_stack
                self.generated_code.append(f"ARMZ {stack_position}\n")

        elif(ctx.PROC_WRITE() != None):
            self.visitChildren(ctx)
            self.generated_code.append("IMPR\n")

    #lista para leitura de variavel
    def visitListaExpressao(self, ctx: LangGrammar.ListaExpressaoContext):
        self.historico_variavel = []
        self.visitChildren(ctx)

    def salvarPrograma(self, filename):
        codigo_final = "".join(self.generated_code)
        f = open(filename, "w")
        f.write(codigo_final)
        f.close()