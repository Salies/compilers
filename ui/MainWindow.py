# Projeto de Compiladores
# FCT-UNESP, 2023
# Daniel Serezane e Gabriel Nozawa
# Janela principal da UI

import os
from PyQt6.QtWidgets import QMainWindow, QWidget, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QDialog
from PyQt6.QtGui import QAction, QPixmap, QImage
from PyQt6.QtCore import Qt
from ui.MainWidget import MainWidget
from ui.InterpWindow import InterpWindow

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
        toolsMenu = self.menuBar.addMenu("Ferramentas")
        helpMenu = self.menuBar.addMenu("Ajuda")
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
        # criando actions: toolsMenu
        # Interpretador
        interpreterAction = QAction("Interpretador", self)
        interpreterAction.setShortcut("Ctrl+I")
        interpreterAction.triggered.connect(self.openInterpreter)
        toolsMenu.addAction(interpreterAction)
        # criando actions: helpMenu
        # Sobre
        aboutAction = QAction("Sobre", self)
        aboutAction.setShortcut("Ctrl+H")
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction)
        # Montando o widget de Sobre
        self.aboutWidget = About()
        self.interpWindow = InterpWindow()
        # Montando o widget de Interpretador
        # Criando abas (tab widget)
        self.mainWidget = MainWidget()
        centralLayout.addWidget(self.mainWidget)
        
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "Arquivo de texto (*.txt)")
        if fileName == "":
            return
        # ler o arquivo
        f = open(fileName, "r")
        text = f.read()
        f.close()
        self.mainWidget.setCode(text)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", "Arquivo de texto (*.txt)")
        if fileName == "":
            return
        # salvar o arquivo no path
        f = open(fileName, "w")
        f.write(self.mainWidget.getCode())
        f.close()

    def close(self):
        super().close()

    # Interpretação de código
    def openInterpreter(self):
        print("Abrindo interpretador")
        self.interpWindow.show()

    # Sobre
    def about(self):
        self.aboutWidget.exec()


class About(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 140)
        self.setWindowTitle("Sobre")
        aboutLayout = QHBoxLayout()
        self.setLayout(aboutLayout)
        # Criando labels
        textLayout = QVBoxLayout()
        text = "<b>Daniel Serezane</b> e <b>Gabriel Nozawa</b>"
        text += "<br>orgulhosamente apresentam:"
        text += "<br><b>Projeto de Compiladores v6.6.6.1</b>"
        text += "<br>FCT/UNESP, 2023"
        titleLabel = QLabel(text)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textLayout.addWidget(titleLabel)
        # Imagem
        imgLayout = QVBoxLayout()
        imageLabel = QLabel()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "../resources/dragao.png")
        img = QImage(path)
        pixmap = QPixmap.fromImage(img)
        imageLabel.setPixmap(pixmap)
        imgLayout.addWidget(imageLabel)
        imgLayout.addStretch()
        
        aboutLayout.addLayout(imgLayout)
        aboutLayout.addLayout(textLayout)

        self.hide()