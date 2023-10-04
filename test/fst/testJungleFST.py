import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.JungleFST import JungleFST

class TestJungleFST(unittest.TestCase):

    def setUp(self):
        self.jungle_fst = JungleFST()
        self.place1 = "IGUAZU"
        self.place2 = "VICTORIA"

    def test_transduce(self):
        result = self.jungle_fst.transform(self.place1)
        r = ' '.join(result)
        self.assertEqual(r,self.place2)
    
    def test_transduce(self):
        result = self.jungle_fst.transform(self.place2)
        r = ' '.join(result)
        self.assertEqual(r,self.place1)

if __name__ == '__main__':
    unittest.main()
