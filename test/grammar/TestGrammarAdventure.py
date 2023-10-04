import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.grammar.GrammarAdventure import GrammarAdventure
import unittest 

class TestGrammarAdventure(unittest.TestCase):
    def setUp(self):
        self.grammar_adventure = GrammarAdventure()

    def test_grammar1(self):
        descripcion = self.grammar_adventure.descgic1()
        print(descripcion) 

    def test_grammar2(self):
        descripcion = self.grammar_adventure.descgic2()
        print(descripcion) 

    def test_grammar3(self):
        descripcion = self.grammar_adventure.descgic3()
        print(descripcion) 

    def test_grammar4(self):
        descripcion = self.grammar_adventure.descgic4()
        print(descripcion) 

if __name__ == "__main__":
    unittest.main()


