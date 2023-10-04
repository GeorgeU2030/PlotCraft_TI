import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.SpaceFST import SpaceFST

class TestSpaceFST(unittest.TestCase):

    def setUp(self):
        self.space_fst = SpaceFST()
        self.planet1 = "MARTE"
        self.planet2 = "VENUS"
        self.planet3 = "URANO"

    def test_transduce(self):
        result = self.space_fst.transform(self.planet1)
        r = ' '.join(result)
        self.assertEqual(r,self.planet2)
    
    def test_transduce(self):
        result = self.space_fst.transform(self.planet2)
        r = ' '.join(result)
        self.assertEqual(r,self.planet3)

if __name__ == '__main__':
    unittest.main()
