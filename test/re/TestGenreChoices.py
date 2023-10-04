import unittest
import re

class TestGenreChoices(unittest.TestCase):
    def test_optionA(self):
        optionA = re.compile(r"Adventure")
        self.assertTrue(optionA.match("Adventure"))
        self.assertFalse(optionA.match("Sci-Fi"))

    def test_optionB(self):
        optionB = re.compile(r"Sci-Fi")
        self.assertTrue(optionB.match("Sci-Fi"))
        self.assertFalse(optionB.match("Fantasy"))

    def test_optionC(self):
        optionC = re.compile(r"Drama")
        self.assertTrue(optionC.match("Drama"))
        self.assertFalse(optionC.match("Horror"))

    def test_optionD(self):
        optionD = re.compile(r"Fantasy")
        self.assertTrue(optionD.match("Fantasy"))
        self.assertFalse(optionD.match("Historical"))

    def test_optionE(self):
        optionE = re.compile(r"Mystery")
        self.assertTrue(optionE.match("Mystery"))
        self.assertFalse(optionE.match("Adventure"))

    def test_optionF(self):
        optionF = re.compile(r"Horror")
        self.assertTrue(optionF.match("Horror"))
        self.assertFalse(optionF.match("Sci-Fi"))

    def test_optionG(self):
        optionG = re.compile(r"Historical")
        self.assertTrue(optionG.match("Historical"))
        self.assertFalse(optionG.match("Fantasy"))

if __name__ == "__main__":
    unittest.main()
