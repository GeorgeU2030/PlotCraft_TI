import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)


from models.User import User
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class SciFiController():
    def __init__(self,main_view,user):
        self.main_view = main_view
        self.user = user
    
    def backScreen(self, mainwindow):
        from views.Genres import Ui_GenresUI as Genres_Form
        mainwindow.hide()
        self.main_view.Form = QtWidgets.QMainWindow()
        self.main_view.ui = Genres_Form(self.user)
        self.main_view.ui.setupUi(self.main_view.Form)
        self.main_view.Form.show()
    
    