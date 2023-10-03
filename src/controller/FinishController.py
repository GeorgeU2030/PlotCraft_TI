import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import QtWidgets

class FinishController():
    def __init__(self,main_view,user):
        self.main_view = main_view
        self.user = user
    
    def backMenu(self, Ui_Form):
        from src.views.MainWindow import Ui_MainWindow as Main
        Ui_Form.hide()
        self.main_view.Form = QtWidgets.QMainWindow()
        self.main_view.ui = Main()
        self.main_view.ui.setupUi(self.main_view.Form)
        self.main_view.Form.show()