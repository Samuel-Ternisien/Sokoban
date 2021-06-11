import numpy as np
class SokobanModel:

    def __init__(self):
        self.__controller = None
        self.__view = None


        self.__views = []
        self.__matrix = None
        self.__baseMatrix = None

        self.__pieces = []
        self.__level=0

    def clear(self):
        self.__view = []
        self.__matrix = self.__baseMatrix

    def addView(self, view):

        self.__views.append(view)

    def get(self, l, c):

        return self.__matrix[l][c]
    
    def getLevel(self):
        return self.__level

    def set(self, l, c, v):

        self.__matrix[l][c] = v

        for view in self.__views:
            view.updateView([(l, c, v)])

    def getMainCharacter(self):
        result = np.where(self.__matrix == 3)
        listOfCoordinates= list(zip(result[0], result[1]))
        for cord in listOfCoordinates:
            val = cord
        return val

    def getCase(self, l, c):
        return self.__matrix[l][c]

    def getPieces(self):
        return self.__pieces

    def getCaisse(self):
        val = []
        result = np.where(self.__matrix == 4)
        listOfCoordinates= list(zip(result[0], result[1]))
        for cord in listOfCoordinates:
            val.append(cord)
        return val
    
    def setMatrix(self,matrix):
        self.__matrix=matrix
        self.__baseMatrix=matrix
        
    def setLevel(self,level):
        self.__level=level
    def setPiece(self):
        result = np.where(self.__matrix == 2)
        listOfCoordinates= list(zip(result[0], result[1]))
        for cord in listOfCoordinates:
            self.__pieces.append(cord)