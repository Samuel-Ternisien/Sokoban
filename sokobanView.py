from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QMenuBar, QLabel, QWidget, QAction,QMessageBox,QMenu)
from PyQt5.QtMultimedia import QSound
from sokobanModel import SokobanModel
from PyQt5 import QtGui
import sys, os
iconroot = os.path.dirname(__file__)
import numpy as np

class sokobanView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sokoban")
        self.__controller = None
        self.__model = None

        self.__matrix = None

        self.__previousMatrix = None


        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.__gridLayout = QGridLayout()
        self.__gridLayout.setContentsMargins(0,0,0,0)
        self.__gridLayout.setHorizontalSpacing(0)
        self.__gridLayout.setVerticalSpacing(0)
        self.__window.setLayout(self.__gridLayout)
        self.statusBar().showMessage("Number of mouvement: 0")
        self.setLayout(self.__gridLayout)
        self.setFixedSize(600,600)

        #MENU DU JEU : INIT
        menuBar = self.menuBar()
        gameMenu = QMenu("&Game", self)
        menuBar.addMenu(gameMenu)

        #MENU DU JEU : RESTART
        restart = QAction(self)
        restart.setText("&Restart")
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)

        #MENU DU JEU : QUIT
        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        #MENU DE NIVEAUX : INIT
        levelBar = self.menuBar()
        levelMenu = QMenu("&Level",self)
        levelBar.addMenu(levelMenu)

        #MENU DE NIVEAUX : 1
        one = QAction(self)
        one.setText("&Level 1")
        levelMenu.addAction(one)
        one.triggered.connect(lambda: self.__controller.setLevel(1))

        #MENU DE NIVEAUX : 2
        one = QAction(self)
        one.setText("&Level 2")
        levelMenu.addAction(one)
        one.triggered.connect(lambda: self.__controller.setLevel(2))

        #MENU DE NIVEAUX : 3
        one = QAction(self)
        one.setText("&{Test Only}Level 3")
        levelMenu.addAction(one)
        one.triggered.connect(lambda: self.__controller.setLevel(3))

        #MENU DE NIVEAUX : 4
        one = QAction(self)
        one.setText("&{Test Only}Level 4")
        levelMenu.addAction(one)
        one.triggered.connect(lambda: self.__controller.setLevel(4))

        #MENU DE NIVEAUX : 5
        one = QAction(self)
        one.setText("&{Test Only}Level 5")
        levelMenu.addAction(one)
        one.triggered.connect(lambda: self.__controller.setLevel(5))

        
    
    def setModel(self, model):
        self.__model = model
 
    def setController(self, controller):
        self.__controller = controller
    
    def keyPressEvent(self, event):
        if(event.key() == 16777236  or event.key() == 16777234  or event.key() == 16777235  or event.key() == 16777237):
            value = event.key() - 16777234
            direction = [(-1, 0), (0, -1), (1,0), (0, 1)][value]

            self.__controller.moveEvent(direction)
        else:
            """
            TODO
            """


    def cleanView(self):
        QSound.play("ressources/sound/Welcome.wav")
        tab = self.__matrix
        tabb = self.__previousMatrix
        vide = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/vide.png"))
        mur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/mur.png"))
        piece = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/piece.png"))
        joueur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/joueur.png"))
        caisse = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/caisse.png"))
        sol = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/sol.png"))

        for x in range(len(tabb)):
            for y in range(len(tabb[x])):
                label = QLabel(self)
                label.setPixmap(vide)
                self.__gridLayout.addWidget(label, x, y)

        for x in range(len(tab)):
            for y in range(len(tab[x])):
                label = QLabel(self)
                if(tab[x][y] == 0):
                    label.setPixmap(vide)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 1):
                    label.setPixmap(mur)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 2):
                    label.setPixmap(piece)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 3):
                    label.setPixmap(joueur)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 4):
                    label.setPixmap(caisse)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 5):
                    label.setPixmap(sol)
                    self.__gridLayout.addWidget(label, x, y)


    def restart(self):
        self.__controller.restartGame()

    def updateView(self, changes):
        vide = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/vide.png"))
        mur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/mur.png"))
        piece = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/piece.png"))
        joueur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/joueur.png"))
        caisse = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/caisse.png"))
        sol = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/sol.png"))
        score = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/scored.png"))
        for change in changes:
            i = change[0]
            j = change[1]
            v = change[2]
            label = QLabel(self)
            if(v == 0):
                label.setPixmap(vide)
                self.__gridLayout.addWidget(label, i, j)
            if(v == 1):
                label.setPixmap(mur)
                self.__gridLayout.addWidget(label, i, j)
            if(v == 2):
                label.setPixmap(piece)
                self.__gridLayout.addWidget(label, i, j)
            if(v == 3):
                label.setPixmap(joueur)
                self.__gridLayout.addWidget(label, i, j)
            if(v == 4):
                label.setPixmap(caisse)
                self.__gridLayout.addWidget(label, i, j)
            if(v == 5):
                label.setPixmap(sol)
                self.__gridLayout.addWidget(label, i, j)
            if(v==6):
                QSound.play("ressources/sound/Score.wav")
                label.setPixmap(score)
                self.__gridLayout.addWidget(label,i,j)

    def winScreen(self):
        """
        TODO
        """
        QSound.play("ressources/sound/victory.wav")
    def getMouvements(self, mouvements):
        self.statusBar().showMessage("Number of mouvement: "+ str(mouvements))

    def getMatrix(self):
        return self.__matrix

    def setPrev(self, matrix):
        self.__previousMatrix = matrix

    def setMatrix(self,matrix):
        tab=matrix
        vide = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/vide.png"))
        mur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/mur.png"))
        piece = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/piece.png"))
        joueur = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/joueur.png"))
        caisse = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/caisse.png"))
        sol = QtGui.QPixmap(os.path.join(iconroot, "ressources/img/sol.png"))

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                label = QLabel(self)
                if(tab[x][y] == 0):
                    label.setPixmap(vide)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 1):
                    label.setPixmap(mur)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 2):
                    label.setPixmap(piece)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 3):
                    label.setPixmap(joueur)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 4):
                    label.setPixmap(caisse)
                    self.__gridLayout.addWidget(label, x, y)
                if(tab[x][y] == 5):
                    label.setPixmap(sol)
                    self.__gridLayout.addWidget(label, x, y)
        self.__matrix=matrix
        if(self.__previousMatrix is None):
            self.__previousMatrix = matrix