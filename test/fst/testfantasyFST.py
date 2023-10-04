import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.FantasyFST import FantasyFST

class TestFantasyFST(unittest.TestCase):

    def setUp(self):
        self.fantasy_fst = FantasyFST()
        self.artifact1 = "EXCALIBUR"
        self.artifact2 = "MAGICRING"

    def test_transduce(self):
        result = self.fantasy_fst.transform(self.artifact1)
        r = ' '.join(result)
        self.assertEqual(r,self.artifact2)
    
    def test_transduce(self):
        result = self.fantasy_fst.transform(self.artifact2)
        r = ' '.join(result)
        self.assertEqual(r,self.artifact1)

if __name__ == '__main__':
    unittest.main()
