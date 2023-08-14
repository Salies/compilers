from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto de Compiladores")
        self.setFixedSize(800, 600)
        # criando central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # criando menu bar
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu("Arquivo")
        # criando actions: fileMenu
        # Abrir
        openAction = QAction("Abrir", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)
        # Salvar
        saveAction = QAction("Salvar", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)
        # Sair
        exitAction = QAction("Sair", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "Arquivo de texto (*.txt)")
        print(fileName)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", "Arquivo de texto (*.txt)")
        print(fileName)

    def close(self):
        super().close()