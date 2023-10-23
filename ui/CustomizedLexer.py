# Projeto de Compiladores
# FCT-UNESP, 2023
# Daniel Serezane e Gabriel Nozawa
# Syntax highlighter para o editor de texto

import re
from PyQt6.Qsci import QsciLexerCustom
from PyQt6.QtGui import QFont, QColor
from tools.LangLexer import LangLexer
from antlr4 import *

class CustomizedLexer(QsciLexerCustom):

    def __init__(self, parent):
        super(CustomizedLexer, self).__init__(parent)
		
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Courier New", 12))
        
        # Define as cores da fonte que serão utilizadas
        self.setColor(QColor("#ff000000"), 0)   # Style 0: black
        self.setColor(QColor("#ff0000ff"), 1)   # Style 1: blue
        self.setColor(QColor("#ff00ff00"), 2)   # Style 2: green
        self.setColor(QColor("#ffff0000"), 3)   # Style 3: red

        # Define a cor do papel (cor de fundo) para cada estilo
        self.setPaper(QColor("#ffffffff"), 0)   # Style 0: white
        self.setPaper(QColor("#ffffffff"), 1)   # Style 1: white
        self.setPaper(QColor("#ffffffff"), 2)   # Style 2: white
        self.setPaper(QColor("#ffffffff"), 3)   # Style 3: white
        

        # Define o tipo de fonte para cada estilo
        self.setFont(QFont("Courier New", 12), 0)   # Style 0: 12pt
        self.setFont(QFont("Courier New", 12), 1)   # Style 1: 12pt
        self.setFont(QFont("Courier New", 12), 2)   # Style 2: 12pt
        self.setFont(QFont("Courier New", 12), 3)   # Style 3: 12pt
        
        

    def description(self, style_nr):
        if style_nr == 0:
            return "black"
        elif style_nr == 1:
            return "blue"
        elif style_nr == 2:
            return "green"
        elif style_nr == 3:
            return "red"
        return ""

    def styleText(self, start, end):
        self.startStyling(0)
        # adquire o texto do editor
        text = self.parent().text()
        
        # divide o texto em tokens
        p = re.compile(r"\s+|\w+|\/\/|\W|\t")
        token_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]

        # flags para controle de comentário
        comment_flag = False
        multiline_comm_flag = False

        # Aplica a syntax highlight
        for token in token_list:
            # checa se está no modo comentário
            if comment_flag:
                # pinta de verde
                self.setStyling(token[1], 2)
                # checa se é um comentário de múltiplas linha
                if multiline_comm_flag:
                    if token[0] == "}":
                        multiline_comm_flag = False
                        comment_flag = False
                else:
                    # checa se é um final de linha
                    if token[0][0] in ["\n", "\r", "\t"] or token[0][-1] in ["\n", "\r", "\t"]:
                        comment_flag = False
            # se não estiver em modo comentário, checa a syntax highlight
            else:
                # checa se é uma palavra e pinta de azul
                if token[0] in [ "program", "procedure", "var", "int", "boolean", "read", "write", "true", "false", "begin", "end", "if", "then", "else", "or", "and", "not", "div", "while", "do" ]:
                    # BLUE style
                    self.setStyling(token[1], 1)
                # checa se o token inicia um comentário
                elif token[0] in [ "//", "{"]:
                    self.setStyling(token[1], 2)
                    # checa se é um comentário multilinha
                    if token[0] == "{":
                        multiline_comm_flag = True
                    # inicia o modo comentário
                    comment_flag = True
                else:
                    # Default style
                    self.setStyling(token[1], 0)