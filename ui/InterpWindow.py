from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QDialog, QPushButton,
    QHBoxLayout, QVBoxLayout, QLabel, QTextEdit,
    QFileDialog, QSpinBox
)
from PyQt6.QtGui import QIcon, QPixmap, QImage, QAction, QFont
from PyQt6.QtCore import Qt
import os

from MEPA.Mepa import Mepa

class InterpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interpretador MEPA")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "../resources/meepo.png")
        self.setWindowIcon(QIcon(path))
        self.aboutWidget = About()
        self.setFixedSize(800, 500)
        # menu bar
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu("Arquivo")
        helpMenu = self.menuBar.addMenu("Ajuda")
        # actions
        openAction = QAction("Abrir", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)
        # Sobre
        aboutAction = QAction("Sobre", self)
        aboutAction.setShortcut("Ctrl+H")
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction)
        # criando janela em si
        mainLayout = QHBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(mainLayout)
        self.setCentralWidget(self.centralWidget)
        # criando widgets
        self.inputStr = ''
        self.inputWidget = QTextEdit()
        self.inputDialog = InputDialog()
        self.inputWidget.setReadOnly(True)
        self.outputWidget = QTextEdit()
        self.outputWidget.setReadOnly(True)
        # black background
        self.outputWidget.setStyleSheet("background-color: black; color: white;")
        # set font
        font = QFont("Courier New", 12)
        self.inputWidget.setFont(font)
        self.outputWidget.setFont(font)
        outputLayout = QVBoxLayout()
        outputLayout.addWidget(self.outputWidget)
        self.interpButton = QPushButton("Interpretar")
        self.interpButton.clicked.connect(self.interpret)
        outputLayout.addWidget(self.interpButton)
        # adicionando widgets
        mainLayout.addWidget(self.inputWidget)
        mainLayout.addLayout(outputLayout)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir compilação", "", "Arquivo MEPA (*.mepa)")
        if filename == "":
            return
        with open(filename, "r") as f:
            self.inputStr = f.read()
        self.inputWidget.setText(self.inputStr)

    def about(self):
        self.aboutWidget.exec()

    def interpret(self):
        print('interpretando código')
        # limpa output
        self.outputWidget.setText('')
        # inicia a máquina
        mepa = Mepa(self.inputStr, self.print_to_output, self.input_integer)
        # executa o código
        mepa.run_code()

    def print_to_output(self, text):
        self.outputWidget.append(str(text))

    def input_integer(self):
        self.inputDialog.exec()
        return self.inputDialog.get_input()

class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 100)
        self.setWindowTitle("Entrada")
        self.inputSpinbox = QSpinBox()
        self.inputSpinbox.setRange(-32768, 32767)
        self.inputSpinbox.setSingleStep(1)
        self.inputSpinbox.setValue(0)
        self.inputSpinbox.setWrapping(True)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Insira um número inteiro:"))
        layout.addWidget(self.inputSpinbox)
        layout.addWidget(QPushButton("Ok", clicked=self.accept))
        self.setLayout(layout)
        self.hide()

    def get_input(self):
        return int(self.inputSpinbox.value())

# safoda poo
class About(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 140)
        self.setWindowTitle("Sobre")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "../resources/meepo.png")
        self.setWindowIcon(QIcon(path))
        aboutLayout = QHBoxLayout()
        self.setLayout(aboutLayout)
        # Criando labels
        textLayout = QVBoxLayout()
        text = "<b>Daniel Serezane</b> e <b>Gabriel Nozawa</b>"
        text += "<br>orgulhosamente apresentam:"
        text += "<br><b>Interpretador MEPA v6.9</b>"
        text += "<br>FCT/UNESP, 2023"
        titleLabel = QLabel(text)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textLayout.addWidget(titleLabel)
        # Imagem
        imgLayout = QVBoxLayout()
        imageLabel = QLabel()
        path = os.path.join(current_dir, "../resources/mee2.png")
        img = QImage(path)
        pixmap = QPixmap.fromImage(img)
        imageLabel.setPixmap(pixmap)
        imgLayout.addWidget(imageLabel)
        imgLayout.addStretch()
        
        aboutLayout.addLayout(imgLayout)
        aboutLayout.addLayout(textLayout)

        self.hide()