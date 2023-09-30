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
class StoryController():
    def __init__(self,main_view,user,automaton,story):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton
        self.story = story

    def goDesc(self,mainwindow):
        text = self.main_view.textInp.toPlainText() 
        jungleExp1 = re.compile(r"Despiertas en medio de la jungla")
        jungleExp2 = re.compile(r"Llegas a una aldea oculta en la jungla")

        dev1 = re.compile(r"Exploras la jungla y encuentras la cascada")
        dev2 = re.compile(r"Encuentras rastros de una antigua de la civilizacion")
        dev3 = re.compile(r"Te vas por el río y llegas a un misterioso templo")
        dev4 = re.compile(r"Encuentras y te unes a la expedicion arqueologica")

        end1 = re.compile(r"En la cascada encuentras un tesoro y te conviertes en una leyenda")
        end2 = re.compile(r"Alli encuentras una tribu y adoptas su estilo de vida en la jungla")
        end3 = re.compile(r"Regresas a casa con artefactos valiosos y te conviertes en un experto")
        end4 = re.compile(r"Eres rescatado por un equipo de la civilizacion y regresas a casa")
        end5 = re.compile(r"Te conviertes en un renombrado explorador de la jungla")
        end6 = re.compile(r"En el templo quedas atrapado por siempre al caer en una trampa")
        end7 = re.compile(r"Encuentras muchos tesoros en la expedicion y eres millonario")
        end8 = re.compile(r"Te pierdes en la jungla para siempre, convirtiendote en una leyenda perdida")

        if jungleExp1.search(text) or jungleExp2.search(text):
            text_in='jungle exploration'
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story)
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
                description = grammar.descgic1()
            elif jungleExp2.search(text):
                description = grammar.descgic2()
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("Development")
            self.main_view.ui.textInp.setText(text)
            if dev1.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" IGUAZU")
            if dev2.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" MAYA")
            if dev3.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" PALENQUE")
            if dev4.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" FRANKLIN")
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story)
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story)
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
        from models.fst.AdventureFST import AdventureFST
        newfst = AdventureFST()
        result = newfst.transform(lastword)
        textnew = word[:-1]
        r_text = ' '.join(textnew)
        wfst = ' '.join(result)
        self.main_view.auxiliarlabel.setText(r_text+" "+wfst)