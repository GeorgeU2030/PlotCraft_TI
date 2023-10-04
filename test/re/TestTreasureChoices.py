import unittest
import re

class TestTreasureChoices(unittest.TestCase):
    def test_treasureIslandExpressions(self):
        jungleExp1 = re.compile(r"You arrive on a deserted island after discovering an ancient treasure map")
        jungleExp2 = re.compile(r"You arrive on a beautiful tropical island after discovering an ancient treasure map")

        self.assertTrue(jungleExp1.match("You arrive on a deserted island after discovering an ancient treasure map"))
        self.assertTrue(jungleExp2.match("You arrive on a beautiful tropical island after discovering an ancient treasure map"))
        self.assertFalse(jungleExp1.match("While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar"))
        self.assertFalse(jungleExp2.match("Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"Then begin to explore the island in search of clues and buried treasures in island")
        dev2 = re.compile(r"The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by")
        dev3 = re.compile(r"As they explore the island, they discover clues that lead them to secret and lush corners of the island")
        dev4 = re.compile(r"The exploration becomes complicated due to the island's natural dangers, and the treasure hunt is temporarily suspended by")

        self.assertTrue(dev1.match("Then begin to explore the island in search of clues and buried treasures in island"))
        self.assertTrue(dev2.match("The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by"))
        self.assertFalse(dev1.match("While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar"))
        self.assertFalse(dev2.match("Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see"))

    def test_endExpressions(self):
        end1 = re.compile(r"You find a chest with valuable treasures and celebrate their success on the beach")
        end2 = re.compile(r"Then discover a series of riddles and clues that lead them to another unknown island")
        end3 = re.compile(r"Then decide to leave the island but remain intrigued by the unresolved mystery")
        end4 = re.compile(r"You find temporary shelter on the island and learn to survive before embarking on a new journey in search of the treasure")
        end5 = re.compile(r"Later discover a hidden waterfall with hidden treasures and celebrate their success in the tropical sunlight")
        end6 = re.compile(r"The clues lead them to a mysterious coral reef where they find ancient artifacts, but also face underwater dangers")
        end7 = re.compile(r"You decide to go back home, but the island has left a lasting impression on their souls, and they dream of returning someday")
        end8 = re.compile(r"You find temporary shelter on the island and learn to live in harmony with nature before embarking on new adventures")

        self.assertTrue(end1.match("You find a chest with valuable treasures and celebrate their success on the beach"))
        self.assertTrue(end2.match("Then discover a series of riddles and clues that lead them to another unknown island"))
        self.assertFalse(end1.match("While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar"))
        self.assertFalse(end2.match("Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see"))

if __name__ == "__main__":
    unittest.main()
