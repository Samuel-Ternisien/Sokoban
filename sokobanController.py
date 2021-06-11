import numpy as np
class sokobanController:

    def __init__(self):

        self.__model = None
        self.__view = None
        self.__mouvements = 0
        self.__win = None

    def setModel(self, model):

        self.__model = model

    def setView(self, view):

        self.__view = view

    def winCheck(self):

        pieces = self.__model.getPieces()

        caisse = self.__model.getCaisse()

        if(caisse == pieces):
            self.__view.winScreen()
            print("win")

    def moveEvent(self, v):
        positionmainCharacter = self.__model.getMainCharacter()
        pieces = self.__model.getPieces()

        if(v == (-1, 0)): #GAUCHE
            if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 1) != 1): # SI C'EST PAS UN MUR
                if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 1) == 4 or self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 1) == 6): #SI C'EST UNE CAISSE APRES
                    coord = positionmainCharacter[0], positionmainCharacter[1] - 1
                    if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 1) == 6 and coord not in pieces or self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 1) == 4 and coord not in pieces): # SI C DEJA SUR UNE PIECE
                        if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 2) != 1): # SI YA PAS DE MUR APRES LA CAISSE
                            if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 2) != 4 and self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 2) != 6): # SI YA PAS DE CAISSE APRES LA CAISSE
                                if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] - 2) == 2): # CHANGER LA CAISSE 
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[1] - 1 
                                    self.__model.set(positionmainCharacter[0], ligne, 3)
                                    self.__model.set(positionmainCharacter[0], ligne - 1, 6) # CHANGE LA CAISSE
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                                else:
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[1] - 1 
                                    self.__model.set(positionmainCharacter[0], ligne, 3)
                                    self.__model.set(positionmainCharacter[0], ligne - 1, 4)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                else:
                    coord = positionmainCharacter[0], positionmainCharacter[1]
                    if(coord in pieces):
                        ligne = positionmainCharacter[1] - 1 
                        self.__model.set(positionmainCharacter[0], ligne, 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 2)
                    else:
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                        ligne = positionmainCharacter[1] - 1 
                        self.__model.set(positionmainCharacter[0], ligne, 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)

        if(v == (1, 0)): #DROITE
            if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 1) != 1): # SI C'EST PAS UN MUR
                if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 1) == 4 or self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 1) == 6): #SI C'EST UNE CAISSE APRES
                    coord = positionmainCharacter[0], positionmainCharacter[1] + 1
                    if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 1) == 6 and coord not in pieces or self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 1) == 4 and coord not in pieces): # SI C DEJA SUR UNE PIECE
                        if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 2) != 1): # SI YA PAS DE MUR APRES LA CAISSE
                            if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 2) != 4 and self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 2) != 6) :
                                if(self.__model.getCase(positionmainCharacter[0], positionmainCharacter[1] + 2) == 2):
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[1] + 1 
                                    self.__model.set(positionmainCharacter[0], ligne, 3)
                                    self.__model.set(positionmainCharacter[0], ligne + 1, 6)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                                else:
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[1] + 1 
                                    self.__model.set(positionmainCharacter[0], ligne, 3)
                                    self.__model.set(positionmainCharacter[0], ligne + 1, 4)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                else:

                    coord = positionmainCharacter[0], positionmainCharacter[1]
                    if(coord in pieces):
                        ligne = positionmainCharacter[1] + 1 
                        self.__model.set(positionmainCharacter[0], ligne, 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 2)
                    else:
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                        ligne = positionmainCharacter[1] + 1 
                        self.__model.set(positionmainCharacter[0], ligne, 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
        
        if(v == (0, -1)): #HAUT
            if(self.__model.getCase(positionmainCharacter[0] - 1, positionmainCharacter[1]) != 1):
                if(self.__model.getCase(positionmainCharacter[0] - 1, positionmainCharacter[1]) == 4 or self.__model.getCase(positionmainCharacter[0] - 1, positionmainCharacter[1]) == 6):
                    coord = positionmainCharacter[0] - 1, positionmainCharacter[1]
                    if(self.__model.getCase(positionmainCharacter[0] - 1, positionmainCharacter[1]) == 6 and coord not in pieces or self.__model.getCase(positionmainCharacter[0] - 1, positionmainCharacter[1]) == 4 and coord not in pieces):
                        if(self.__model.getCase(positionmainCharacter[0] - 2, positionmainCharacter[1]) != 1):
                            if(self.__model.getCase(positionmainCharacter[0] - 2, positionmainCharacter[1]) != 4 and self.__model.getCase(positionmainCharacter[0] - 2, positionmainCharacter[1]) != 6):
                                if(self.__model.getCase(positionmainCharacter[0] - 2, positionmainCharacter[1]) == 2):
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[0] - 1 
                                    self.__model.set(ligne, positionmainCharacter[1], 3)
                                    self.__model.set(ligne - 1, positionmainCharacter[1], 6)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                                else:
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[0] - 1 
                                    self.__model.set(ligne, positionmainCharacter[1], 3)
                                    self.__model.set(ligne - 1, positionmainCharacter[1], 4)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                else:
                    coord = positionmainCharacter[0], positionmainCharacter[1]
                    if(coord in pieces):
                        ligne = positionmainCharacter[0] - 1 
                        self.__model.set(ligne, positionmainCharacter[1], 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 2)
                    else:
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                        ligne = positionmainCharacter[0] - 1 
                        self.__model.set(ligne, positionmainCharacter[1], 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)

        if(v == (0, 1)): #BAS
            if(self.__model.getCase(positionmainCharacter[0] + 1, positionmainCharacter[1]) != 1):
                if(self.__model.getCase(positionmainCharacter[0] + 1, positionmainCharacter[1]) == 4 or self.__model.getCase(positionmainCharacter[0] + 1, positionmainCharacter[1]) == 6):
                    coord = positionmainCharacter[0] + 1, positionmainCharacter[1]
                    if(self.__model.getCase(positionmainCharacter[0] + 1, positionmainCharacter[1]) == 6 and coord not in pieces or self.__model.getCase(positionmainCharacter[0] + 1, positionmainCharacter[1]) == 4 and coord not in pieces):
                        if(self.__model.getCase(positionmainCharacter[0] + 2, positionmainCharacter[1]) != 1):
                            if(self.__model.getCase(positionmainCharacter[0] + 2, positionmainCharacter[1]) != 4 and self.__model.getCase(positionmainCharacter[0] + 2, positionmainCharacter[1]) != 6):
                                if(self.__model.getCase(positionmainCharacter[0] + 2, positionmainCharacter[1]) == 2):
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[0] + 1 
                                    self.__model.set(ligne, positionmainCharacter[1], 3)
                                    self.__model.set(ligne + 1, positionmainCharacter[1], 6)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                                else:
                                    self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                                    ligne = positionmainCharacter[0] + 1 
                                    self.__model.set(ligne, positionmainCharacter[1], 3)
                                    self.__model.set(ligne + 1, positionmainCharacter[1], 4)
                                    self.__mouvements += 1
                                    self.__view.getMouvements(self.__mouvements)
                else:
                    coord = positionmainCharacter[0], positionmainCharacter[1]
                    if(coord in pieces):
                        ligne = positionmainCharacter[0] + 1 
                        self.__model.set(ligne, positionmainCharacter[1], 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 2)
                    else:
                        self.__model.set(positionmainCharacter[0], positionmainCharacter[1], 5)
                        ligne = positionmainCharacter[0] + 1 
                        self.__model.set(ligne, positionmainCharacter[1], 3)
                        self.__mouvements += 1
                        self.__view.getMouvements(self.__mouvements)
        
        self.winCheck()

    def restartGame(self):
        self.__model.clear()
        self.__view.cleanView()

        self.__mouvements = 0
        self.__win = None
        self.setLevel(self.__model.getLevel())

    def setLevel(self,level):
        l=0
        c=0
        with open(f"ressources/lvl/level{level}.txt") as file:
            files = [line.strip() for line in file]
        for x in range(len(files)):
            lvlayout=[[7 for j in range(len(files[x]))]for i in range(len(files))]
        for line in files:
            for items in line:
                if items !=",":
                    if items=="c": #caisse
                        lvlayout[l][c]=4 
                        c+=1
                    if items=="v": #vide
                        lvlayout[l][c]=0
                        c+=1
                    if items=="j": #joueur
                        lvlayout[l][c]=3
                        c+=1
                    if items=="m": #mur
                        lvlayout[l][c]=1
                        c+=1
                    if items=="s": #sol
                        lvlayout[l][c]=5
                        c+=1
                    if items=="p": #piece
                        lvlayout[l][c]=2
                        c+=1
            l+=1
            c=0
        result = np.array(lvlayout)
        self.__view.setMatrix(result)
        self.__model.setMatrix(result)
        self.__model.setLevel(level)