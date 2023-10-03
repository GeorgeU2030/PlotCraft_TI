import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from src.models.User import User
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class SciFiController():
    def __init__(self,main_view,user,automaton):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton
    
    def backScreen(self, mainwindow):
        from src.views.Genres import Ui_GenresUI as Genres_Form
        mainwindow.hide()
        self.main_view.Form = QtWidgets.QMainWindow()
        self.main_view.ui = Genres_Form(self.user)
        self.main_view.ui.setupUi(self.main_view.Form)
        self.main_view.Form.show()
    
    def scifiDesc(self,text,mainwindow):
        
        #options
        optionA = re.compile(r"alien")
        optionB = re.compile(r"space")
        if optionA.search(text):
            text_in='alien'
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

            from src.views.StoryUI import Ui_storyWindow as Story_Form
            from src.models.ShortStory import ShortStory
            mainwindow.hide()
            story = ShortStory()
            condition = 5
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,story,condition)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.nextBtn.setVisible(False)
            self.main_view.ui.exchangeBtn.setVisible(False)
            self.main_view.ui.phaseStory.setText("Beginning")
            self.main_view.Form.show()
            
            

        elif optionB.search(text):
            text_in='space'
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

            from src.views.StoryUI import Ui_storyWindow as Story_Form
            from src.models.ShortStory import ShortStory
            mainwindow.hide()
            story = ShortStory()
            condition = 6
            self.main_view.Form = QtWidgets.QMainWindow()
            self.main_view.ui = Story_Form(self.user,self.automaton,story,condition)
            self.main_view.ui.setupUi(self.main_view.Form)
            self.main_view.ui.option1label.setText(symbols[0])
            self.main_view.ui.option2label.setText(symbols[1])
            self.main_view.ui.nextBtn.setVisible(False)
            self.main_view.ui.exchangeBtn.setVisible(False)
            self.main_view.ui.phaseStory.setText("Beginning")
            self.main_view.Form.show()