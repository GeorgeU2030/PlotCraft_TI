import unittest
import re

class TestMysteryChoices(unittest.TestCase):
    def test_mysteryExpressions(self):
        jungleExp1 = re.compile(r"I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room")
        jungleExp2 = re.compile(r"I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect")

        self.assertTrue(jungleExp1.match("I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room"))
        self.assertTrue(jungleExp2.match("I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect"))
        self.assertFalse(jungleExp1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(jungleExp2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"Upon deciphering the letter, I find a crucial clue leading me to an old diary hidden in the mansion's library, revealing deep secrets in")
        dev2 = re.compile(r"As I delve deeper into the investigation, I confront a mysterious figure in the darkness, an encounter that could change everything in")
        dev3 = re.compile(r"The newly discovered fingerprint leads us to an unknown suspect, a twist that baffles the investigators in")
        dev4 = re.compile(r"The ancient spellbook we find at the crime scene seems to be linked to the mystery, but its contents are incomprehensible in")

        self.assertTrue(dev1.match("Upon deciphering the letter, I find a crucial clue leading me to an old diary hidden in the mansion's library, revealing deep secrets in"))
        self.assertTrue(dev2.match("As I delve deeper into the investigation, I confront a mysterious figure in the darkness, an encounter that could change everything in"))
        self.assertFalse(dev1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(dev2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_endExpressions(self):
        end1 = re.compile(r"The diary's pages unveil dark family secrets previously unknown, bringing me closer to unraveling the mystery")
        end2 = re.compile(r"The diary only leads to confusion and dead ends, leaving me even more baffled in my quest")
        end3 = re.compile(r"During the confrontation, I manage to obtain crucial information that brings me closer to solving the mystery")
        end4 = re.compile(r"The mysterious figure manages to escape, leaving me with no answers and grappling with more questions than before")
        end5 = re.compile(r"While investigating the new suspect, we unravel a network of shocking secrets that bring us closer to the heart of the mystery")
        end6 = re.compile(r"The fingerprint leads nowhere and turns out to be false, leaving us once again at a dead end")
        end7 = re.compile(r"After deciphering the book, we discover a stunning revelation that leads us to the next chapter of the mystery")
        end8 = re.compile(r"Misuse of the book triggers magical chaos, further complicating the resolution of the mystery")

        self.assertTrue(end1.match("The diary's pages unveil dark family secrets previously unknown, bringing me closer to unraveling the mystery"))
        self.assertTrue(end2.match("The diary only leads to confusion and dead ends, leaving me even more baffled in my quest"))
        self.assertFalse(end1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(end2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

if __name__ == "__main__":
    unittest.main()
