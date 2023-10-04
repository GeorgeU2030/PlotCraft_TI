import unittest
import re

class TestHorrorChoices(unittest.TestCase):
    def test_mansionExpressions(self):
        jungleExp1 = re.compile(r"As we explored the abandoned mansion, we felt that our footsteps echoed more than usual, and we decided to venture further")
        jungleExp2 = re.compile(r"Upon entering the eerie lobby of the haunted hotel, a shiver ran down our spines, but we chose to confront our nightmares")

        self.assertTrue(jungleExp1.match("As we explored the abandoned mansion, we felt that our footsteps echoed more than usual, and we decided to venture further"))
        self.assertTrue(jungleExp2.match("Upon entering the eerie lobby of the haunted hotel, a shiver ran down our spines, but we chose to confront our nightmares"))
        self.assertFalse(jungleExp1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(jungleExp2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"The friends decide to explore the mansion further in search of answers and find a secret door in the")
        dev2 = re.compile(r"The friends choose to leave the mansion, feeling that something is watching them like a")
        dev3 = re.compile(r"The friends decide to investigate the oldest rooms of the hotel, where listen scream and some weird facts happen like")
        dev4 = re.compile(r"They choose to leave the hotel due to the intensity of the paranormal experiences they face like")

        self.assertTrue(dev1.match("The friends decide to explore the mansion further in search of answers and find a secret door in the"))
        self.assertTrue(dev2.match("The friends choose to leave the mansion, feeling that something is watching them like a"))
        self.assertFalse(dev1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(dev2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_endExpressions(self):
        end1 = re.compile(r"Upon opening the secret door, they reveal a hidden passage leading to an even more sinister in the place")
        end2 = re.compile(r"The secret door is sealed shut, and they cannot open it, leaving the abandoned mansion behind")
        end3 = re.compile(r"As they exit the mansion, they hear footsteps behind them but see no one, filling them with fear")
        end4 = re.compile(r"They leave the mansion without incident, but a strange shadow looms over them as they walk away")
        end5 = re.compile(r"In one of the rooms, they find evidence of paranormal activity and choose to continue their investigation")
        end6 = re.compile(r"They find nothing unusual in the old rooms and decide to leave the hotel")
        end7 = re.compile(r"As they prepare to leave, a terrifying apparition blocks their way, leaving them trapped in the haunted hotel")
        end8 = re.compile(r"They manage to leave the hotel, terrified, but they feel that something dark is following them as they walk away")

        self.assertTrue(end1.match("Upon opening the secret door, they reveal a hidden passage leading to an even more sinister in the place"))
        self.assertTrue(end2.match("The secret door is sealed shut, and they cannot open it, leaving the abandoned mansion behind"))
        self.assertFalse(end1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(end2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

if __name__ == "__main__":
    unittest.main()
