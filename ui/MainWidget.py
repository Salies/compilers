# Projeto de Compiladores
# FCT-UNESP, 2023
# Daniel Serezane e Gabriel Nozawa
# Widget principal da UI

from PyQt6.QtWidgets import (
    QTextEdit, QWidget, QHBoxLayout, 
    QVBoxLayout, QTableWidget, QHeaderView, 
    QPushButton, QTabWidget
)
from PyQt6.QtGui import QFont
from PyQt6.Qsci import *
from antlr4 import *
from ui.CustomizedLexer import CustomizedLexer
from ana.Ana import Ana

def inputFactory():
    editWidget = QTextEdit()
    editWidget.setFixedHeight(100)
    editWidget.setReadOnly(True)
    return editWidget

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
        lexer = CustomizedLexer(self.editor)
        self.editor.setLexer(lexer)
        self.editor.setMarginLineNumbers(1, True)
        font = QFont("Courier New", 10) # TODO: subsituir
        # callback para atualizar tamanho da margem
        self.editor.linesChanged.connect(self.qtdLineChanged)
        self.editor.setFont(font)
        lexer.setFont(font)
        # padding
        self.editor.setMarginsFont(font)
        # botão de ativação
        self.button = QPushButton("Analisar", self)
        self.button.clicked.connect(self.analyze)
        # botão de limpar
        clearButton = QPushButton("Limpar", self)
        clearButton.clicked.connect(self.clear)
        # criando tabela de lexemas
        self.table = QTableWidget(1, 5, self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(["Lexema", "Token", "Linha", "Col. inicial", "Col. final"])
        # desabilitando edição da tabela
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # selecionando linha inteira
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setRowCount(0)
        # Criando outputs léxico e sintático
        self.tabWidget = QTabWidget() # tab widget para alternar
        self.lexOutput = inputFactory()
        self.sinOutput = inputFactory()
        self.semOutput = inputFactory()
        lexLayout.addWidget(self.lexOutput)
        sinLayout.addWidget(self.sinOutput)
        # adapt tab widget to fit textedit
        self.tabWidget.setFixedHeight(129)
        self.tabWidget.addTab(self.lexOutput, "Erros léxicos")
        self.tabWidget.addTab(self.sinOutput, "Erros sintáticos")
        self.tabWidget.addTab(self.semOutput, "Erros semânticos")
        bottomLayout.addWidget(self.tabWidget)
        edAndTableLay.addWidget(self.editor)
        edAndTableLay.addWidget(self.table)
        # buttons layout
        btnsLayout = QVBoxLayout()
        btnsLayout.addStretch()
        btnsLayout.addWidget(self.button)
        btnsLayout.addWidget(clearButton)
        bottomLayout.addLayout(btnsLayout)
        centralLayout.addLayout(edAndTableLay)
        centralLayout.addLayout(bottomLayout)
        # remove stretch
        centralLayout.setStretch(0, 1)
        self.setLayout(centralLayout)

    def qtdLineChanged(self):
        # mudar tamanho da margem
        n_digits = len(str(self.editor.lines()))
        zeros = "0" * n_digits
        zeros += "0" # add zero extra
        self.editor.setMarginWidth(1, zeros)

    def setCode(self, code):
        self.editor.setText(code)

    def getCode(self):
        return self.editor.text()
    
    def clear(self):
        self.editor.clear()
        self.table.clearContents()
        self.table.setRowCount(0)
        self.lexOutput.clear()
        self.sinOutput.clear()
    
    def analyze(self):
        self.lex()
        # muda título da tab de erros léxicos para: Erros léxicos (qtd_erros)
        qtd_err_lex = len(self.lex_errors)
        self.tabWidget.setTabText(0, f"Erros léxicos ({qtd_err_lex})")
        self.sintaxAnalysis()
        qtd_err_sintax = len(self.sin_errors)
        self.tabWidget.setTabText(1, f"Erros sintáticos ({qtd_err_sintax})")
        self.semantics()

    def lex(self):
        # pega texto do editor
        # nota: toPlainText() ainda mantém a quebra de linha, ou seja, sem problemas
        code = self.getCode()
        self.filtered_code, self.lex_errors, out_txt, self.all_tokens = Ana.lex(code, self.table)
        self.lexOutput.setText(out_txt)

    def sintaxAnalysis(self):
        errStr, sinErrors = Ana.sintax(self.filtered_code)
        # output errors
        self.sinOutput.setText(errStr)
        self.sin_errors = sinErrors

    def semantics(self):
        if(len(self.sin_errors) != 0 or len(self.lex_errors) != 0):
            return
        Ana.semantics(self.all_tokens)

        

