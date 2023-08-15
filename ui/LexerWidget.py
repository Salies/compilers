from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QTableWidget, QHeaderView, QPushButton

class LexerWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.editor = QTextEdit(self)
        # botão de ativação
        self.button = QPushButton("➜", self)
        self.button.setFixedWidth(40)
        self.button.setFixedHeight(40)
        # button: font size 24
        self.button.setStyleSheet("font-size:24px")
        # criando tabela de lexemas
        self.table = QTableWidget(1, 5, self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(["Lexema", "Token", "Linha", "Col. inicial", "Col. final"])
        # desabilitando edição da tabela
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        # selecionando linha inteira
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def setCode(self, code):
        self.editor.setText(code)
