import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.RaceFST import RaceFST

class TestRaceFST(unittest.TestCase):

    def setUp(self):
        self.race_fst = RaceFST()
        self.brand1 = "CHEVROLET"
        self.brand2 = "NISSAN"
        self.brand3 = "TOYOTA"

    def test_transduce(self):
        result = self.race_fst.transform(self.brand1)
        r = ' '.join(result)
        self.assertEqual(r,self.brand2)
    
    def test_transduce(self):
        result = self.race_fst.transform(self.brand2)
        r = ' '.join(result)
        self.assertEqual(r,self.brand3)

if __name__ == '__main__':
    unittest.main()
