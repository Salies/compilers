from antlr4 import *
from tools.LangLexer import LangLexer
from tools.LangGrammar import LangGrammar
from tools.ErrorHandler import ErrorListener, CustomErrorStrategy
from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog
from .SemanticAna import SemanticAna
from MEPA.CodeGenerator import CodeGenerator
from datetime import datetime

# temporário até ter custom
from antlr4.error.ErrorListener import ErrorListener as ANTLRErrorListener

class Ana:
    def lex(code, table):
        stream = InputStream(code)
        # cria lexer a partir da stream
        lexer = LangLexer(stream)
        # pega os tokens
        tokens = lexer.getAllTokens()
        # monta a listinha pra tabela
        token_list = [[token.text, lexer.symbolicNames[token.type], token.line, token.column, token.column + len(token.text)] for token in tokens]
        # lista para pegar os erros e exibir no output
        lex_errors = []
        # atualiza a tabela
        table.setRowCount(len(token_list))
        filtered_code = code
        for i, token in enumerate(token_list):
            # se o token for um erro, adiciona na lista de erros
            if token[1] == "INVALID_TOKEN":
                lex_errors.append(token)
                # remove do código
                filtered_code = filtered_code.replace(token[0], "")
            for j, value in enumerate(token):
                table.setItem(i, j, QTableWidgetItem(str(value)))
        # output errors
        error_template = "Lexema inválido: '{lexema}', na linha {linha}, coluna {coluna}."
        out_txt = "\n".join([error_template.format(lexema=token[0], linha=token[2], coluna=token[3]) for token in lex_errors])
        return filtered_code, lex_errors, out_txt, tokens
    
    def sintax(filtered_code):
        lexer = LangLexer(InputStream(filtered_code))
        tokens = CommonTokenStream(lexer)
        parser = LangGrammar(tokens)
        # custom error strategy
        parser._errHandler = CustomErrorStrategy()
        # custom error listener
        errorListener = ErrorListener()
        lexer.removeErrorListeners()
        parser.removeErrorListeners()
        lexer.addErrorListener(errorListener)
        parser.addErrorListener(errorListener)
        # parse
        tree = parser.programa()
        return errorListener.getErrorsAsStr(), errorListener.getErrors(), tree
    
    def semantics(tree):
        print('començando análise semantica')
        errorListener = ErrorListener()
        semanticAna = SemanticAna(errorListener)
        semanticAna.visit(tree)
        semanticAna.encontrarVarGlobaisNaoUtilizadas()
        return errorListener.getErrorsAsStr(), errorListener.getErrors()

    def generate_code(tree):
        print('començando geracao codigo')
        errorListener = ErrorListener()
        codeGenerator = CodeGenerator(errorListener)
        codeGenerator.visit(tree)
        # pega hora atual
        now = datetime.now()
        now_str = now.strftime("%d-%m-%Y_%H-%M-%S")
        filname = f"mepa_{now_str}.mepa"
        # abre um filedialog com essa sugestão de nome
        final_filename, _ = QFileDialog.getSaveFileName(None, "Salvar compilação", filname, "Arquivo MEPA (*.mepa)")
        if final_filename == "":
            return
        # salva o arquivo
        codeGenerator.salvarPrograma(final_filename)
        
        


