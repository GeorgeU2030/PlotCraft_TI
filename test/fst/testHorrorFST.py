import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.HorrorFST import HorrorFST

class TestHorrorFST(unittest.TestCase):

    def setUp(self):
        self.horror_fst = HorrorFST()
        self.spirit1 = "GHOST"
        self.spirit2 = "DEMON"

    def test_transduce(self):
        result = self.horror_fst.transform(self.spirit1)
        r = ' '.join(result)
        self.assertEqual(r,self.spirit2)
    
    def test_transduce(self):
        result = self.horror_fst.transform(self.spirit2)
        r = ' '.join(result)
        self.assertEqual(r,self.spirit1)

if __name__ == '__main__':
    unittest.main()
