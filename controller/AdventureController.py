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
from PyQt5.QtCore import Qt

class AdventureController():
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

    def jungleDesc(self,text):
        msgBox = QMessageBox()
        image_path = "icon.png"
        original_pixmap = QPixmap("images/libro.png")

        #TEXT - DESCRIPTION
        description=""
        #options
        optionA = re.compile(r"jungle")
        optionB = re.compile(r"treasure")
        optionC = re.compile(r"race")
        optionD = re.compile(r"himalaya")
        if optionA.search(text):
            description=("Venture deep into a lush tropical jungle, where the vegetation is dense, "
                    "and wildlife is abundant. Your team of explorers will face natural challenges "
                    "like rushing rivers, dense forests, and unknown creatures. Discover hidden ancient "
                    "ruins and unravel ancestral mysteries as you journey into uncharted territories.")
        elif optionB.search(text):
            description=("Embark on an exciting treasure hunt that will take you "
                         " through varied and mysterious landscapes. Follow encoded clues and solve clever "
                         " riddles as you get closer to the legendary lost treasure. Along the way, "
                         " you'll encounter challenges, traps, and greedy rivals who are also " 
                         " after the treasure. Who will be the first to find it and claim it?")
        elif optionC.search(text):
            description=("Take part in an exhilarating race through the vast Sahara Desert, "
                         "where sand dunes stretch as far as the eye can see. Your off-road " 
                         "vehicle will tackle challenging terrain, from expansive dune fields"
                          " to rocky and scorching landscapes. The race is a test of endurance "
                          "in an unforgiving environment, where precise navigation and speed " 
                          " are crucial to reach the finish line.")
        elif optionD.search(text):
            description = ("Travel to the majestic Himalayan mountains, where peaks rise above the clouds,"
                           " and the rugged beauty of the region is awe-inspiring. Join a mountaineering"
                           " expedition that will challenge you both physically and mentally as you scale "
                           " the highest heights on Earth. But beware, extreme weather conditions and "
                           " treacherous terrain make this adventure an epic challenge.")


        max_width = 50
        max_height = 50
        scaled_pixmap = original_pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)
        msgBox.setIconPixmap(scaled_pixmap)  # Establece la imagen informativa
        msgBox.setWindowTitle("Confirmation")
        msgBox.setText(description)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)  # Agrega botones personalizados

        # Personaliza el cuadro de mensaje con hojas de estilo CSS
        msgBox.setStyleSheet("""
            QMessageBox {
                background-color: #f0f0f0; 
                font-size: 14px; 
            }
            QLabel {
                color: #333; 
            }
            QPushButton {
                background-color: #007acc; 
                color: white; 
                border: 1px solid #007acc; 
                padding: 5px 15px; 
                border-radius: 5px; 
            }
            QPushButton:hover {
                background-color: #005ca3; 
                border: 1px solid #005ca3; 
            }
        """)
        msgBox.exec_()

        