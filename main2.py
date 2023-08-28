import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QPalette

class LineCounterWidget(QWidget):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        # make layout elements float to the top
        layout.setAlignment(Qt.AlignTop)
        self.line_label = QLabel()
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.line_label.setFont(font)
        self.line_label.setFixedWidth(30)
        # set background color using qpalette
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.lightGray)
        self.line_label.setAutoFillBackground(True)
        self.line_label.setPalette(palette)
        # make label align right
        self.line_label.setAlignment(Qt.AlignRight)
        self.line_label.setStyleSheet("font-size:14px")
        # set label row
        layout.addWidget(self.line_label)
        layout.addWidget(self.text_edit)
        layout.setContentsMargins(0, 6, 0, 0)
        self.setLayout(layout)
        self.updateLineCount()

        self.text_edit.textChanged.connect(self.updateLineCount)

    def updateLineCount(self):
        block_count = self.text_edit.document().blockCount()
        self.line_label.setText('\n'.join(str(i) for i in range(1, block_count + 1)))

    def sizeHint(self):
        return QSize(self.line_label.sizeHint().width() + 10, super().sizeHint().height())


class CustomTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        # font size 14
        self.setStyleSheet("font-size:14px")
        # set monospace font
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.setFont(font)

    def sizeHint(self):
        return QSize(super().sizeHint().width() - 30, super().sizeHint().height())


class LineCounterMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        text_edit = CustomTextEdit()
        line_counter = LineCounterWidget(text_edit)

        central_widget = QWidget()
        central_layout = QHBoxLayout()
        # remove gaps
        central_layout.setContentsMargins(0, 0, 0, 0)
        # remove padding
        central_layout.setSpacing(0)
        central_layout.addWidget(line_counter)
        central_layout.addWidget(text_edit)
        central_widget.setLayout(central_layout)

        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Line Counter Example")

def main():
    app = QApplication(sys.argv)
    window = LineCounterMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
