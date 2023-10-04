import unittest
import re

class TestRaceChoices(unittest.TestCase):
    def test_desertRaceExpressions(self):
        jungleExp1 = re.compile(r"At the start of the desert race, the competitors prepare to face challenges")
        jungleExp2 = re.compile(r"The race begins in the heart of the desert in the night, with the racers ready")

        self.assertTrue(jungleExp1.match("At the start of the desert race, the competitors prepare to face challenges"))
        self.assertTrue(jungleExp2.match("The race begins in the heart of the desert in the night, with the racers ready"))
        self.assertFalse(jungleExp1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(jungleExp2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"The racers encounter a sandstorm that reduces visibility and complicates the race in their")
        dev2 = re.compile(r"During the race, a vehicle gets stuck in a sand dune, requiring assistance from other competitors in their")
        dev3 = re.compile(r"In the middle of the night race, competitors face a sandstorm that challenges their ability to navigate in the darkness in their")
        dev4 = re.compile(r"As they progress in the darkness, the racers discover an alternative route that leads them to an oasis in the middle of the desert in their")

        self.assertTrue(dev1.match("The racers encounter a sandstorm that reduces visibility and complicates the race in their"))
        self.assertTrue(dev2.match("During the race, a vehicle gets stuck in a sand dune, requiring assistance from other competitors in their"))
        self.assertFalse(dev1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(dev2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

    def test_endExpressions(self):
        end1 = re.compile(r"Despite the storm, some racers manage to reach the finish line, showcasing their skill in adverse conditions")
        end2 = re.compile(r"The sandstorm causes delays and challenges, but the race continues with determination")
        end3 = re.compile(r"The racers display sportsmanship by stopping to assist the stuck vehicle, resuming the race together")
        end4 = re.compile(r"Despite the obstacle, the team manages to free the vehicle and continues in the race")
        end5 = re.compile(r"Some racers persevere through the storm, successfully completing the nighttime race")
        end6 = re.compile(r"The sandstorm forces the nighttime race to be halted for safety reasons")
        end7 = re.compile(r"By choosing to explore the oasis, the racers discover a magical place and enjoy a break before returning to the race")
        end8 = re.compile(r"They decide to continue in the nighttime race, avoiding the distraction of the oasis and staying focused on the competition")

        self.assertTrue(end1.match("Despite the storm, some racers manage to reach the finish line, showcasing their skill in adverse conditions"))
        self.assertTrue(end2.match("The sandstorm causes delays and challenges, but the race continues with determination"))
        self.assertFalse(end1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertFalse(end2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))

if __name__ == "__main__":
    unittest.main()
