import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.TreasureFST import TreasureFST

class TestTreasureFST(unittest.TestCase):

    def setUp(self):
        self.treasure_fst = TreasureFST()
        self.condition1 = "HEAT"
        self.condition2 = "SANDSTORM"

    def test_transduce(self):
        result = self.treasure_fst.transform(self.condition1)
        r = ' '.join(result)
        self.assertEqual(r,self.condition2)
    
    def test_transduce(self):
        result = self.treasure_fst.transform(self.condition2)
        r = ' '.join(result)
        self.assertEqual(r,self.condition1)

if __name__ == '__main__':
    unittest.main()
