import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from models.User import User
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
        # imports
        from views.AdventureUI import Ui_adventureUI as Ui_Adv
        from views.SciFiUI import Ui_SciFi as Ui_Scf
        from views.ThemeFormUI import Ui_ThemeForm as Ui_theme
        from models.automata.AdventureAutomata import AdventureAutomata
        from models.automata.SciFiAutomata import SciFiAutomata
        from models.automata.DramaAutomata import DramaAutomata

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

        else:
            image_path = "images/warning.png"
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
            
       
