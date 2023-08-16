from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QTabWidget, QVBoxLayout
from PySide6.QtGui import QAction
from ui.LexerWidget import LexerWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto de Compiladores")
        self.setFixedSize(900, 600)
        # criando central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # central layout
        centralLayout = QVBoxLayout()
        self.centralWidget.setLayout(centralLayout)
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
        # create tab widget
        tabWidget = QTabWidget(self)
        self.lexWidget = LexerWidget()
        tabWidget.addTab(self.lexWidget, "Analisador léxico")
        tabWidget.addTab(QWidget(), "...")
        centralLayout.addWidget(tabWidget)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "Arquivo de texto (*.txt)")
        if fileName == "":
            return
        # ler o arquivo
        f = open(fileName, "r")
        text = f.read()
        f.close()
        self.lexWidget.setCode(text)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", "Arquivo de texto (*.txt)")
        if fileName == "":
            return
        # salvar o arquivo no path
        f = open(fileName, "w")
        f.write(self.lexWidget.getCode())
        f.close()

    def close(self):
        super().close()