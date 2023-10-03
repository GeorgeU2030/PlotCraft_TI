import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.User import User
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class MainWindowController():
    def __init__(self,main_view):
        self.main_view = main_view
    
    def lookgenres(self,Ui_lookgenres,mainWindow):
        name = self.main_view.lineEdit.text()  
        user = User(name)
        mainWindow.hide()
        self.main_view.Form = QtWidgets.QMainWindow()
        self.main_view.ui = Ui_lookgenres(user)
        self.main_view.ui.setupUi(self.main_view.Form)
        self.main_view.Form.show()