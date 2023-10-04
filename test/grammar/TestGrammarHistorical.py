import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.grammar.GrammarHistorical import GrammarHistorical
import unittest 

class TestGrammarHistorical(unittest.TestCase):
    def setUp(self):
        self.grammar_adventure = GrammarHistorical()

    def test_grammar1(self):
        descripcion = self.grammar_adventure.descgic1()
        print(descripcion) 

    def test_grammar2(self):
        descripcion = self.grammar_adventure.descgic2()
        print(descripcion) 


if __name__ == "__main__":
    unittest.main()


