import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.HistoricalFST import HistoricalFST

class TestHistoricalFST(unittest.TestCase):

    def setUp(self):
        self.historical_fst = HistoricalFST()
        self.city1 = "ROMA"
        self.city2 = "ATENAS"
        self.city3 = "PARIS"

    def test_transduce(self):
        result = self.historical_fst.transform(self.city1)
        r = ' '.join(result)
        self.assertEqual(r,self.city2)
    
    def test_transduce(self):
        result = self.historical_fst.transform(self.city2)
        r = ' '.join(result)
        self.assertEqual(r,self.city3)

if __name__ == '__main__':
    unittest.main()
