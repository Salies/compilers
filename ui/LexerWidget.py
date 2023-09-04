from PyQt6.QtWidgets import QPlainTextEdit, QWidget, QTextEdit, QHBoxLayout, QTableWidget, QHeaderView, QPushButton, QTableWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.Qsci import *
from antlr4 import *
from tools.LangLexer import LangLexer

class LexerWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.editor = QsciScintilla(self)
        # set ANTLR lexer
        # TODO: NOZAWA MUDA AQUI
        lexer = QsciLexerPascal(self.editor)
        self.editor.setLexer(lexer)
        self.editor.setMarginLineNumbers(1, True)
        font = QFont("Courier New", 12) # TODO: subsituir
        self.editor.setFont(font)
        lexer.setFont(font)
        # padding
        self.editor.setMarginsFont(font)
        # botão de ativação
        self.button = QPushButton("➜", self)
        self.button.setFixedWidth(40)
        self.button.setFixedHeight(40)
        self.button.clicked.connect(self.lex)
        # button: font size 24
        self.button.setStyleSheet("font-size:24px")
        # criando tabela de lexemas
        self.table = QTableWidget(1, 5, self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(["Lexema", "Token", "Linha", "Col. inicial", "Col. final"])
        # desabilitando edição da tabela
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # selecionando linha inteira
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def setCode(self, code):
        self.editor.setText(code)

    def getCode(self):
        return self.editor.text()

    def lex(self):
        # pega texto do editor
        # nota: toPlainText() ainda mantém a quebra de linha, ou seja, sem problemas
        code = self.getCode()
        # create stream from code
        stream = InputStream(code)
        # cria lexer a partir da stream
        lexer = LangLexer(stream)
        # pega os tokens
        tokens = lexer.getAllTokens()
        # monta a listinha pra tabela
        token_list = [[token.text, lexer.symbolicNames[token.type], token.line, token.column, token.column + len(token.text)] for token in tokens]
        # atualiza a tabela
        self.table.setRowCount(len(token_list))
        for i, token in enumerate(token_list):
            for j, value in enumerate(token):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

