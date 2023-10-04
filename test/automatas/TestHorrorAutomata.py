import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.HorrorAutomata import HorrorAutomata

import unittest

class TestHorrorAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = HorrorAutomata()

    def test_horror(self):
        self.automata.add_transition(self.automata.q0, "horror", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "As we explored the abandoned mansion, we felt that our footsteps echoed more than usual, and we decided to venture further", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)

    def test_start_2(self):
        self.automata.add_transition(self.automata.q1, "Upon entering the eerie lobby of the haunted hotel, a shiver ran down our spines, but we chose to confront our nightmares", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_resolution_1(self):
        self.automata.add_transition(self.automata.q2, "The friends decide to explore the mansion further in search of answers and find a secret door in the", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

    def test_resolution_2(self):
        self.automata.add_transition(self.automata.q2, "The friends choose to leave the mansion, feeling that something is watching them like a", self.automata.q5)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q5
        self.assertEqual(self.automata.current_state, self.automata.q5)


if __name__ == "__main__":
    unittest.main()
