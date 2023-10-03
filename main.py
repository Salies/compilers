# Projeto de Compiladores
# FCT-UNESP, 2023
# Daniel Serezane e Gabriel Nozawa

from ui.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# TODO: limit identifier size