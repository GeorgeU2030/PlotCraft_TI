import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

class User:
    def __init__(self, name):
        self.name = name
