import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.AlienFST import AlienFST

class TestAlienFST(unittest.TestCase):

    def setUp(self):
        self.alien_fst = AlienFST()
        self.country1 = "USA"
        self.country2 = "CHINA"
        self.country3 = "FRANCE"

    def test_transduce(self):
        result = self.alien_fst.transform(self.country1)
        r = ' '.join(result)
        self.assertEqual(r,self.country2)
    
    def test_transduce(self):
        result = self.alien_fst.transform(self.country2)
        r = ' '.join(result)
        self.assertEqual(r,self.country3)

if __name__ == '__main__':
    unittest.main()
