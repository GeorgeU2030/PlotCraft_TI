import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.MysteryAutomata import MysteryAutomata

import unittest

class TestMysteryAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = MysteryAutomata()

    def test_mystery(self):
        self.automata.add_transition(self.automata.q0, "mystery", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)

    def test_start_2(self):
        self.automata.add_transition(self.automata.q1, "I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_resolution_1(self):
        self.automata.add_transition(self.automata.q2, "Upon deciphering the letter, I find a crucial clue leading me to an old diary hidden in the mansion's library, revealing deep secrets in", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

    def test_resolution_2(self):
        self.automata.add_transition(self.automata.q2, "As I delve deeper into the investigation, I confront a mysterious figure in the darkness, an encounter that could change everything in", self.automata.q5)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q5
        self.assertEqual(self.automata.current_state, self.automata.q5)


if __name__ == "__main__":
    unittest.main()
