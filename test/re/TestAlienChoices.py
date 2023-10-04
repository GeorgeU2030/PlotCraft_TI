import unittest
import re

class TestAlienChoices(unittest.TestCase):
    def test_jungleExpressions(self):
        jungleExp1 = re.compile(r"Alien spacecraft descend upon Earth, causing panic and confusion among the population")
        jungleExp2 = re.compile(r"The human resistance joins forces in an effort to repel the alien invasion")

        self.assertTrue(jungleExp1.match("Alien spacecraft descend upon Earth, causing panic and confusion among the population"))
        self.assertTrue(jungleExp2.match("The human resistance joins forces in an effort to repel the alien invasion"))
        self.assertFalse(jungleExp1.match("The aliens make contact and reveal their intentions"))
        self.assertFalse(jungleExp2.match("Humanity organizes to confront the alien threat"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"The alien spaceships descend upon Earth, causing panic and bewilderment among the population of")
        dev2 = re.compile(r"The aliens make contact and reveal their intentions, demanding Earth's resources or threatening catastrophic consequences in")
        dev3 = re.compile(r"Humanity organizes to confront the alien threat and fights valiantly in")
        dev4 = re.compile(r"The aliens intensify their offensive, causing devastation on Earth specially in")

        self.assertTrue(dev1.match("The alien spaceships descend upon Earth, causing panic and bewilderment among the population of"))
        self.assertTrue(dev2.match("The aliens make contact and reveal their intentions, demanding Earth's resources or threatening catastrophic consequences in"))
        self.assertFalse(dev1.match("Alien spacecraft descend upon Earth, causing panic and confusion among the population"))
        self.assertFalse(dev2.match("Humanity organizes to confront the alien threat"))

    def test_endExpressions(self):
        end1 = re.compile(r"World leaders convene experts and scientists to analyze the ships and communicate with the aliens")
        end2 = re.compile(r"The civilian population seeks refuge and watches in awe as the military prepares to defend against the invasion")
        end3 = re.compile(r"World leaders attempt negotiations with the aliens to avoid conflict, while some challenge their authority")
        end4 = re.compile(r"Humanity prepares to resist the alien invasion, uniting forces to protect their planet")
        end5 = re.compile(r"An epic battle unfolds against the alien invaders, where humans display their bravery and determination")
        end6 = re.compile(r"Scientists discover a weakness in alien technology and work on a plan to defeat the invaders")
        end7 = re.compile(r"Humanity suffers significant losses but manages to resist and defend their planet against the alien invasion")
        end8 = re.compile(r"Despite their bravery, humanity faces overwhelming difficulties and seeks a desperate solution to halt the invasion")

        self.assertTrue(end1.match("World leaders convene experts and scientists to analyze the ships and communicate with the aliens"))
        self.assertTrue(end2.match("The civilian population seeks refuge and watches in awe as the military prepares to defend against the invasion"))
        self.assertFalse(end1.match("The aliens make contact and reveal their intentions"))
        self.assertFalse(end2.match("Humanity organizes to confront the alien threat"))

if __name__ == "__main__":
    unittest.main()
