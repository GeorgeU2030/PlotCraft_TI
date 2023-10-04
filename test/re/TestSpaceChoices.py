import unittest
import re

class TestSpaceChoices(unittest.TestCase):
    def test_aresSpacecraftExpressions(self):
        jungleExp1 = re.compile(r"The Ares spacecraft successfully lifts off from Earth, marking the beginning of an exciting mission")
        jungleExp2 = re.compile(r"During the launch of the Ares spacecraft, technical issues arise that jeopardize the mission")

        self.assertTrue(jungleExp1.match("The Ares spacecraft successfully lifts off from Earth, marking the beginning of an exciting mission"))
        self.assertTrue(jungleExp2.match("During the launch of the Ares spacecraft, technical issues arise that jeopardize the mission"))
        self.assertFalse(jungleExp1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(jungleExp2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"The Ares spacecraft safely lands on Mars, and the crew prepares to explore the planet of")
        dev2 = re.compile(r"En route to the planet, the Ares spacecraft encounters a nearby asteroid and decides to investigate it before continuing to their destination to")
        dev3 = re.compile(r"The crew of the Ares spacecraft works tirelessly to address the technical issues and continue the mission to")
        dev4 = re.compile(r"Despite the technical issues, the crew of the Ares spacecraft decides to press on with the mission and overcome the obstacles and arrive to")

        self.assertTrue(dev1.match("The Ares spacecraft safely lands on Mars, and the crew prepares to explore the planet of"))
        self.assertTrue(dev2.match("En route to the planet, the Ares spacecraft encounters a nearby asteroid and decides to investigate it before continuing to their destination to"))
        self.assertFalse(dev1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(dev2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

    def test_endExpressions(self):
        end1 = re.compile(r"During their exploration of Planet, the crew makes a surprising discovery that could change our understanding of the planet")
        end2 = re.compile(r"The Ares spacecraft crew returns to Earth with valuable data and samples from this planet, contributing to scientific advancements")
        end3 = re.compile(r"The exploration of the asteroid reveals valuable information about the composition of these celestial bodies, which could benefit future space missions")
        end4 = re.compile(r"The crew of the Ares spacecraft documents and studies the asteroid, providing key data for scientific research")
        end5 = re.compile(r"Despite the obstacles, the crew successfully resolves the technical issues and continues their exploration on the planet")
        end6 = re.compile(r"The crew's skills and dedication are put to the test, but they manage to overcome the technical challenges and advance in their mission")
        end7 = re.compile(r"The determination of the crew drives them to overcome challenges and continue the exploration on the planet")
        end8 = re.compile(r"Despite setbacks, the crew maintains their spirit and forges ahead toward the planet with resolve")

        self.assertTrue(end1.match("During their exploration of Planet, the crew makes a surprising discovery that could change our understanding of the planet"))
        self.assertTrue(end2.match("The Ares spacecraft crew returns to Earth with valuable data and samples from this planet, contributing to scientific advancements"))
        self.assertFalse(end1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(end2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

if __name__ == "__main__":
    unittest.main()
