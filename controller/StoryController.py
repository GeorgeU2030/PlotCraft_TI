import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from PyQt5 import QtWidgets, QtGui
from models.grammar.GrammarAdventure import GrammarAdventure
class StoryController():
    def __init__(self,main_view,user,automaton):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton

    def goDesc(self,mainwindow):
        text = self.main_view.textInp.toPlainText() 
        jungleExp1 = re.compile(r"Despiertas en medio de la jungla")
        jungleExp2 = re.compile(r"Llegas a una aldea oculta en la jungla")
        if jungleExp1.search(text):
        
            text_in='jungle exploration'
            estado_actual = self.automaton.q0;

            if estado_actual in self.automaton.transitions:
                state_transitions = self.automaton.transitions[estado_actual]
    
            # Busco la transición que coincide con el texto de entrada
                for symbol, estado_siguiente in state_transitions:
                    if symbol == text_in:
            # Encontre una transición que coincide
                        estado_actual = estado_siguiente
                        self.automaton.current_state = estado_actual
                        break
            
            state_transitions = self.automaton.transitions[estado_actual]

            symbols = []
            for transition in state_transitions:
                symbol = transition[0] 
                symbols.append(symbol)

            from views.StoryUI import Ui_storyWindow as Story_Form
            mainwindow.hide()
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.phaseStory.setText("Beginning")
            self.main_view.ui.textInp.setText(text)

            if self.main_view.phaseStory.text()=='Beginning':
                self.main_view.ui.nextBtn.setVisible(True)
                self.main_view.ui.exchangeBtn.setVisible(False)
                self.main_view.ui.nextBtn.setEnabled(True)
                grammar = GrammarAdventure()
                if jungleExp1.search(text):
                    description = grammar.descgic1()
                elif jungleExp2.search(text):
                    description = grammar.descgic2()
                self.main_view.ui.auxiliarlabel.setText(description)

            self.main_view.Form.show()
        
        else:
            pass
        # ----- alerta de no entradas validas


    def nextDesc(self, mainwindow):
        
            text = self.main_view.textInp.toPlainText() 
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
            self.main_view.ui = Story_Form(self.user,self.automaton)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            if self.main_view.phaseStory.text()=='Beginning':
                self.main_view.ui.phaseStory.setText("Development")
                self.main_view.ui.nextBtn.setVisible(False)
                self.main_view.ui.exchangeBtn.setVisible(True)
            self.main_view.Form.show()