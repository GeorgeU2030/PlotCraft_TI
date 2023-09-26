import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

class StoryController():
    def __init__(self,main_view,user,automaton):
        self.main_view = main_view
        self.user = user
        self.automaton = automaton