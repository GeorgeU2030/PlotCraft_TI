import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import re
from models.grammar.GrammarAdventure import GrammarAdventure
class StoryController():
    def __init__(self,main_view,user,automaton):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton

    def goDesc(self,mainwindow):
        text = self.main_view.textInp.text()
        jungleExp = r"Despiertas en medio de la jungla"
        adventurebeg1 = re.search(jungleExp, text)
        

