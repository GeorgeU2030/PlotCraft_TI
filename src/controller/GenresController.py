import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from src.models.User import User
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap

class GenresController():
    def __init__(self,main_view,user):
        self.main_view = main_view
        self.user = user
    

    def chargeGenre(self, Ui_Form):
        text= self.main_view.enterGenreLine.text()
        # options
        optionA = re.compile(r"Adventure")
        optionB = re.compile(r"Sci-Fi")
        optionC = re.compile(r"Drama")
        optionD = re.compile(r"Fantasy")
        optionE = re.compile(r"Mystery")
        optionF = re.compile(r"Horror")
        optionG = re.compile(r"Historical")
        # imports
        from src.views.AdventureUI import Ui_adventureUI as Ui_Adv
        from src.views.SciFiUI import Ui_SciFi as Ui_Scf
        from src.views.ThemeFormUI import Ui_ThemeForm as Ui_theme
        from src.models.automata.AdventureAutomata import AdventureAutomata
        from src.models.automata.SciFiAutomata import SciFiAutomata
        from src.models.automata.DramaAutomata import DramaAutomata
        from src.models.automata.FantasyAutomata import FantasyAutomata
        from src.models.automata.MysteryAutomata import MysteryAutomata
        from src.models.automata.HorrorAutomata import HorrorAutomata
        from src.models.automata.HistoricalAutomata import HistoricalAutomata

        if optionA.search(text):
            automaton = AdventureAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_Adv(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.Form.show()
        
        elif optionB.search(text):
            automaton = SciFiAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_Scf(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.Form.show()

        elif optionC.search(text):
            automaton = DramaAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_theme(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.Form.show()
        
        elif optionD.search(text):
            automaton = FantasyAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_theme(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.label_4.setPixmap(QtGui.QPixmap("images/fantasy.jpg"))
            self.main_view.ui.label_5.setText("Fantasy")
            self.main_view.ui.genreBtn.setText("Magical Artifact")
            self.main_view.Form.show()
        
        elif optionE.search(text):
            automaton = MysteryAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_theme(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.label_4.setPixmap(QtGui.QPixmap("images/mystery.jpg"))
            self.main_view.ui.label_5.setText("Mystery")
            self.main_view.ui.genreBtn.setText("A New Mystery")
            self.main_view.Form.show()
        
        elif optionF.search(text):
            automaton = HorrorAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_theme(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.label_4.setPixmap(QtGui.QPixmap("images/horror.jpg"))
            self.main_view.ui.label_5.setText("Horror")
            self.main_view.ui.genreBtn.setText("The Nightmare")
            self.main_view.Form.show()

        elif optionG.search(text):
            automaton = HistoricalAutomata()
            Ui_Form.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Ui_theme(self.user,automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.label_4.setPixmap(QtGui.QPixmap("images/historical.jpg"))
            self.main_view.ui.label_5.setText("Historical")
            self.main_view.ui.genreBtn.setText("Court Intrigue")
            self.main_view.Form.show()

        else:
            image_path = "src/images/warning.png"
            original_pixmap = QPixmap(image_path)

            max_width = 80
            max_height = 80

            scaled_pixmap = original_pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)
            msgBox = QMessageBox()
            msgBox.setIconPixmap(scaled_pixmap)  
            msgBox.setWindowTitle("Warning")
            msgBox.setText("Choose a valid genre.")
            msgBox.setStandardButtons(QMessageBox.Ok)  

            
            msgBox.setStyleSheet("""
                QMessageBox {
                    background-color: #f0f0f0; /* Color de fondo */
                    font-size: 14px; /* Tamaño de fuente */
                }
                QLabel {
                    color: black; /* Color del texto */
                    padding-top:10px; 
                }
                QPushButton {
                    background-color: #007acc; /* Color de fondo del botón */
                    color: white; /* Color del texto del botón */
                    border: 1px solid #007acc; /* Borde del botón */
                    padding: 5px 15px; /* Espaciado interno del botón */
                    border-radius: 5px; /* Bordes redondeados */
                }
                QPushButton:hover {
                    background-color: #005ca3; /* Cambio de color al pasar el mouse */
                    border: 1px solid #005ca3; /* Cambio de borde al pasar el mouse */
                }
            """)

            result = msgBox.exec_()
            
       
