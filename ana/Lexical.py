from antlr4 import *
from tools.LangLexer import LangLexer
from PyQt6.QtWidgets import QTableWidgetItem

class Lexical:
    def ana(code, table):
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
        return filtered_code, lex_errors, out_txt
