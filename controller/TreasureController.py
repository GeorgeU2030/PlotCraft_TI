import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from models.grammar.GrammarAdventure import GrammarAdventure
class TreasureController():
    def __init__(self,main_view,user,automaton,story):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton
        self.story = story

    def goDesc(self,mainwindow):
        text = self.main_view.textInp.toPlainText() 
        jungleExp1 = re.compile(r"You arrive on a deserted island after discovering an ancient treasure map")
        jungleExp2 = re.compile(r"You arrive on a beautiful tropical island after discovering an ancient treasure map")

        dev1 = re.compile(r"Then begin to explore the island in search of clues and buried treasures in island")
        dev2 = re.compile(r"The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by")
        dev3 = re.compile(r"As they explore the island, they discover clues that lead them to secret and lush corners of the island")
        dev4 = re.compile(r"The exploration becomes complicated due to the island's natural dangers, and the treasure hunt is temporarily suspended by")

        end1 = re.compile(r"You find a chest with valuable treasures and celebrate their success on the beach")
        end2 = re.compile(r"Then discover a series of riddles and clues that lead them to another unknown island")
        end3 = re.compile(r"Then decide to leave the island but remain intrigued by the unresolved mystery")
        end4 = re.compile(r"You find temporary shelter on the island and learn to survive before embarking on a new journey in search of the treasure")
        end5 = re.compile(r"Later discover a hidden waterfall with hidden treasures and celebrate their success in the tropical sunlight")
        end6 = re.compile(r"The clues lead them to a mysterious coral reef where they find ancient artifacts, but also face underwater dangers")
        end7 = re.compile(r"You decide to go back home, but the island has left a lasting impression on their souls, and they dream of returning someday")
        end8 = re.compile(r"You find temporary shelter on the island and learn to live in harmony with nature before embarking on new adventures")

        if jungleExp1.search(text) or jungleExp2.search(text):
            text_in='treasure hunt'
            current_state = self.automaton.q0;

            if current_state in self.automaton.transitions:
                state_transitions = self.automaton.transitions[current_state]
    
            # Busco la transición que coincide con el texto de entrada
                for symbol, estado_siguiente in state_transitions:
                    if symbol == text_in:
            # Encontre una transición que coincide
                        current_state = estado_siguiente
                        self.automaton.current_state = current_state
                        break
            
            state_transitions = self.automaton.transitions[current_state]

            symbols = []
            for transition in state_transitions:
                symbol = transition[0] 
                symbols.append(symbol)

            from views.StoryUI import Ui_storyWindow as Story_Form
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,2)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("Beginning")
            self.main_view.ui.textInp.setText(text)

            self.main_view.ui.nextBtn.setVisible(True)
            self.main_view.ui.exchangeBtn.setVisible(False)
            self.main_view.ui.nextBtn.setEnabled(True)
            self.main_view.ui.goBtn.setEnabled(False)
            self.main_view.ui.textInp.setEnabled(False)
            grammar = GrammarAdventure()
            if jungleExp1.search(text):
                description = grammar.descgic3()
            elif jungleExp2.search(text):
                description = grammar.descgic4()
            self.main_view.ui.auxiliarlabel.setText(description)
        
            self.main_view.Form.show()
        
        elif dev1.search(text) or dev2.search(text) or dev3.search(text) or dev4.search(text):
            text = self.main_view.textInp.toPlainText() 
            text_in=text
            current_state = self.automaton.current_state;
                
            state_transitions = self.automaton.transitions[current_state]

            symbols = []
            for transition in state_transitions:
                symbol = transition[0] 
                symbols.append(symbol)

            from views.StoryUI import Ui_storyWindow as Story_Form
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,2)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("Development")
            self.main_view.ui.textInp.setText(text)
            if dev1.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" CHRISTMAS")
            if dev2.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" EARTHQUAKE")
            if dev3.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" FIJI")
            if dev4.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" SANDSTORM")
            self.main_view.ui.nextBtn.setVisible(True)
            self.main_view.ui.exchangeBtn.setVisible(True)
            self.main_view.ui.exchangeBtn.setEnabled(True)
            self.main_view.ui.nextBtn.setEnabled(True)
            self.main_view.ui.goBtn.setEnabled(False)
            self.main_view.ui.textInp.setEnabled(False)

            self.main_view.Form.show()
        
        elif end1.search(text) or end2.search(text) or end3.search(text) or end4.search(text) or end5.search(text) or end6.search(text) or end7.search(text) or end8.search(text):
            text = self.main_view.textInp.toPlainText() 
            text_in=text
            current_state = self.automaton.current_state;
                
            state_transitions = self.automaton.transitions[current_state]

            symbols = []
            for transition in state_transitions:
                symbol = transition[0] 
                symbols.append(symbol)

            from views.StoryUI import Ui_storyWindow as Story_Form
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,2)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("End")
            self.main_view.ui.textInp.setText(text)    
            self.main_view.ui.auxiliarlabel.setText(text+" The End.")
            self.main_view.ui.nextBtn.setVisible(True)
            self.main_view.ui.exchangeBtn.setVisible(False)
            self.main_view.ui.exchangeBtn.setEnabled(False)
            self.main_view.ui.nextBtn.setEnabled(True)
            self.main_view.ui.goBtn.setEnabled(False)
            self.main_view.ui.textInp.setEnabled(False)

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
            msgBox.setText("The input is not a valid option, please enter a valid option")
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
        


    def nextDesc(self, mainwindow):
        phase = self.main_view.phaseStory.text()
        if phase != "End":
            text = self.main_view.textInp.toPlainText()
            textauxiliar = self.main_view.auxiliarlabel.text()
            textauxiliar += " "
            self.story.content += textauxiliar
            text_in=text
            current_state = self.automaton.current_state;

            if current_state in self.automaton.transitions:
                state_transitions = self.automaton.transitions[current_state]
        
                # Busco la transición que coincide con el texto de entrada
                for symbol, estado_siguiente in state_transitions:
                    if symbol == text_in:
                        current_state = estado_siguiente
                        self.automaton.current_state = current_state
                        break
                
            state_transitions = self.automaton.transitions[current_state]

            symbols = []
            for transition in state_transitions:
                symbol = transition[0] 
                symbols.append(symbol)
            
            from views.StoryUI import Ui_storyWindow as Story_Form
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,2)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            if self.main_view.phaseStory.text()=='Beginning':
                self.main_view.ui.phaseStory.setText("Development")
            elif self.main_view.phaseStory.text()=='Development':
                self.main_view.ui.phaseStory.setText("End")
            self.main_view.ui.nextBtn.setVisible(False)
            self.main_view.ui.exchangeBtn.setVisible(False)
            self.main_view.Form.show()
        else:
            textauxiliar = self.main_view.auxiliarlabel.text()
            textauxiliar += " "
            self.story.content += textauxiliar
            textstory = self.story.content
            from views.FinishUI import Ui_FinishStory as Finishform
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Finishform(self.user)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.storylabel.setText(textstory)
            self.main_view.Form.show()

    
    def exchange(self):
        text = self.main_view.auxiliarlabel.text()
        word = text.split()
        lastword = word[-1]
        from models.fst.TreasureFST import TreasureFST
        newfst = TreasureFST()
        result = newfst.transform(lastword)
        textnew = word[:-1]
        r_text = ' '.join(textnew)
        wfst = ' '.join(result)
        self.main_view.auxiliarlabel.setText(r_text+" "+wfst)