from PyQt6.QtWidgets import QMainWindow, QDialog, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QPixmap, QImage, QAction
from PyQt6.QtCore import Qt
import os

class InterpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interpretador MEPA")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "../resources/meepo.png")
        self.setWindowIcon(QIcon(path))
        self.aboutWidget = About()
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

    def openFile(self):
        print('abridno arquivo')

    def about(self):
        self.aboutWidget.exec()


# safoda poo
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
        text += "<br><b>Interpretador MEPA v6.9</b>"
        text += "<br>FCT/UNESP, 2023"
        titleLabel = QLabel(text)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textLayout.addWidget(titleLabel)
        # Imagem
        imgLayout = QVBoxLayout()
        imageLabel = QLabel()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "../resources/mee2.png")
        img = QImage(path)
        pixmap = QPixmap.fromImage(img)
        imageLabel.setPixmap(pixmap)
        imgLayout.addWidget(imageLabel)
        imgLayout.addStretch()
        
        aboutLayout.addLayout(imgLayout)
        aboutLayout.addLayout(textLayout)

        self.hide()