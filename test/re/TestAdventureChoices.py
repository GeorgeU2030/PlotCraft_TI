import unittest
import re

class TestAdventureChoices(unittest.TestCase):
    def test_optionA(self):
        optionA = re.compile(r"jungle")
        self.assertTrue(optionA.match("jungle"))
        self.assertFalse(optionA.match("treasure"))

    def test_optionB(self):
        optionB = re.compile(r"treasure")
        self.assertTrue(optionB.match("treasure"))
        self.assertFalse(optionB.match("race"))

    def test_optionC(self):
        optionC = re.compile(r"race")
        self.assertTrue(optionC.match("race"))
        self.assertFalse(optionC.match("himalaya"))

    def test_optionD(self):
        optionD = re.compile(r"himalaya")
        self.assertTrue(optionD.match("himalaya"))
        self.assertFalse(optionD.match("jungle"))

if __name__ == "__main__":
    unittest.main()
