import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.MysteryFST import MysteryFST

class TestMysteryFST(unittest.TestCase):

    def setUp(self):
        self.mystery_fst = MysteryFST()
        self.place1 = "MANSION"
        self.place2 = "HOSPITAL"
        self.place3 = "STATION"

    def test_transduce(self):
        result = self.mystery_fst.transform(self.place1)
        r = ' '.join(result)
        self.assertEqual(r,self.place2)
    
    def test_transduce(self):
        result = self.mystery_fst.transform(self.place2)
        r = ' '.join(result)
        self.assertEqual(r,self.place3)

if __name__ == '__main__':
    unittest.main()
