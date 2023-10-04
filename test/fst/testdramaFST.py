import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.DramaFST import DramaFST

class TestDramaFST(unittest.TestCase):

    def setUp(self):
        self.drama_fst = DramaFST()
        self.city1 = "PARIS"
        self.city2 = "BARCELONA"

    def test_transduce(self):
        result = self.drama_fst.transform(self.city1)
        r = ' '.join(result)
        self.assertEqual(r,self.city2)
    
    def test_transduce(self):
        result = self.drama_fst.transform(self.city2)
        r = ' '.join(result)
        self.assertEqual(r,self.city1)

if __name__ == '__main__':
    unittest.main()
