from PyQt6.QtWidgets import QTextEdit, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView, QPushButton, QTableWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.Qsci import *
from antlr4 import *
from tools.LangLexer import LangLexer
from ui.CustomizedLexer import CustomizedLexer

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        centralLayout = QVBoxLayout()
        edAndTableLay = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        lexLayout = QVBoxLayout()
        sinLayout = QVBoxLayout()
        self.editor = QsciScintilla(self)
        # set ANTLR lexer
        # TODO: NOZAWA MUDA AQUI
        lexer = CustomizedLexer(self.editor)
        self.editor.setLexer(lexer)
        self.editor.setMarginLineNumbers(1, True)
        font = QFont("Courier New", 12) # TODO: subsituir
        self.editor.setFont(font)
        lexer.setFont(font)
        # padding
        self.editor.setMarginsFont(font)
        # botão de ativação
        self.button = QPushButton("Analisar", self)
        self.button.clicked.connect(self.lex)
        # criando tabela de lexemas
        self.table = QTableWidget(1, 5, self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(["Lexema", "Token", "Linha", "Col. inicial", "Col. final"])
        # desabilitando edição da tabela
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # selecionando linha inteira
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        # Criando outputs léxico e sintático
        lexTitle = QLabel("<b>Erros Léxicos</b>")
        lexOutput = QTextEdit()
        lexOutput.setReadOnly(True)
        lexLayout.addStretch()
        lexLayout.addWidget(lexTitle)
        lexLayout.addWidget(lexOutput)
        sinTitle = QLabel("<b>Erros Sintáticos</b>")
        sinOutput = QTextEdit()
        sinOutput.setReadOnly(True)
        sinLayout.addStretch()
        sinLayout.addWidget(sinTitle)
        sinLayout.addWidget(sinOutput)
        # smaller textedit height
        lexOutput.setFixedHeight(100)
        sinOutput.setFixedHeight(100)
        bottomLayout.addLayout(lexLayout)
        bottomLayout.addLayout(sinLayout)
        edAndTableLay.addWidget(self.editor)
        edAndTableLay.addWidget(self.table)
        # buttons layout
        btnsLayout = QVBoxLayout()
        btnsLayout.addStretch()
        btnsLayout.addWidget(self.button)
        bottomLayout.addLayout(btnsLayout)
        centralLayout.addLayout(edAndTableLay)
        centralLayout.addLayout(bottomLayout)
        # remove stretch
        centralLayout.setStretch(0, 1)
        self.setLayout(centralLayout)

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

