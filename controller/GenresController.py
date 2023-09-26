import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from models.User import User
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class GenresController():
    def __init__(self,main_view,user):
        self.main_view = main_view
        self.user = user
    

    def chargeGenre(self, Ui_Form):
        text= self.main_view.enterGenreLine.text()
        # options
        optionA = re.compile(r"Adventure")
        optionB = re.compile(r"Sci-Fi")
        # imports
        from views.AdventureUI import Ui_adventureUI as Ui_Adv
        from views.SciFiUI import Ui_SciFi as Ui_Scf
        from models.automata.AdventureAutomata import AdventureAutomata
        if optionA.search(text):
            automaton = AdventureAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_Adv(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.Form.show()
        
        elif optionB.search(text):
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_Scf(self.user)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.Form.show()

       
