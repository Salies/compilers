from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QTableView

class LexerWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.editor = QTextEdit(self)
        self.table = QTableView(self)
        layout.addWidget(self.editor)
        layout.addWidget(self.table)
        self.setLayout(layout)
