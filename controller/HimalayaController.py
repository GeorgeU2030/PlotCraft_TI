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
class HimalayaController():
    def __init__(self,main_view,user,automaton,story):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton
        self.story = story

    def goDesc(self,mainwindow):
        text = self.main_view.textInp.toPlainText() 
        jungleExp1 = re.compile(r"A team of brave explorers embarks on an expedition to the majestic Himalayas")
        jungleExp2 = re.compile(r"A group of nature enthusiasts and friends embarks on a journey through the Himalayas")

        dev1 = re.compile(r"As they ascend the high peaks, they face natural challenges such as snowstorms and")
        dev2 = re.compile(r"Their expedition becomes complicated due to fatigue and extreme weather")
        dev3 = re.compile(r"While traveling through the mountains, they discover ancient monasteries and form friendships with the community")
        dev4 = re.compile(r"The journey becomes challenging due to altitude and adapting to the environment, leading them to make crucial")

        end1 = re.compile(r"They reach one of the highest summits, feeling the satisfaction of conquest and the breathtaking panoramic view of the mountains")
        end2 = re.compile(r"Despite not reaching the summit, the experience strengthens their bond as a team and fills them with awe for the majesty of the Himalayas")
        end3 = re.compile(r"They decide to return safely, recognizing that safety comes first, but with the determination to return in the future")
        end4 = re.compile(r"Their adventure in the Himalayas changes them profoundly, inspiring them to explore other corners of the world and appreciate the beauty of nature")
        end5 = re.compile(r"They visit a Buddhist monastery and are warmly welcomed, learning about the spirituality and culture of the Himalayas")
        end6 = re.compile(r"They join a local celebration and take part in spiritual practices that enrich their experience")
        end7 = re.compile(r"Although they decide to return earlier than planned, they deeply value their experience in the Himalayas and their connection with nature")
        end8 = re.compile(r"Their adventure in the Himalayas inspires them to lead a more mindful and environmentally respectful lifestyle")

        if jungleExp1.search(text) or jungleExp2.search(text):
            text_in='himalaya'
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,3)
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
                description = grammar.descgic5()
            elif jungleExp2.search(text):
                description = grammar.descgic6()
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,3)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("Development")
            self.main_view.ui.textInp.setText(text)
            if dev1.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" AVALANCHES")
            if dev2.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" WINDY")
            if dev3.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" BHUTIA")
            if dev4.search(text):    
                self.main_view.ui.auxiliarlabel.setText(text+" DECISIONS")
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,3)
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
            self.main_view.ui = Story_Form(self.user,self.automaton,self.story,3)
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
        from models.fst.HimalayaFST import HimalayaFST
        newfst = HimalayaFST()
        result = newfst.transform(lastword)
        textnew = word[:-1]
        r_text = ' '.join(textnew)
        wfst = ' '.join(result)
        self.main_view.auxiliarlabel.setText(r_text+" "+wfst)