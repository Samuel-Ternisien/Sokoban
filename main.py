from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel, QMenuBar,QMessageBox)
from PyQt5 import QtGui
from sokobanModel import SokobanModel
from sokobanView import sokobanView
from sokobanController import sokobanController
import sys,os
iconroot = os.path.dirname(__file__)


app = QApplication(sys.argv)

model = SokobanModel()
controller = sokobanController()
view = sokobanView()

model.addView(view)
view.setModel(model)
view.setController(controller)

controller.setModel(model)
controller.setView(view)
controller.setLevel(1)
model.getMainCharacter()
model.setPiece()

view.show()

#model.set(3,3,3)

sys.exit(app.exec_())