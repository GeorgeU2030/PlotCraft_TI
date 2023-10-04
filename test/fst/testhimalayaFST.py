import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
import unittest

from pyformlang.finite_automaton import Symbol
from src.models.fst.HimalayaFST import HimalayaFST

class TestHimalayaFST(unittest.TestCase):

    def setUp(self):
        self.himalaya_fst = HimalayaFST()
        self.option1 = "ACTIONS"
        self.option2 = "DECISIONS"

    def test_transduce(self):
        result = self.himalaya_fst.transform(self.option1)
        r = ' '.join(result)
        self.assertEqual(r,self.option2)
    
    def test_transduce(self):
        result = self.himalaya_fst.transform(self.option2)
        r = ' '.join(result)
        self.assertEqual(r,self.option1)

if __name__ == '__main__':
    unittest.main()
