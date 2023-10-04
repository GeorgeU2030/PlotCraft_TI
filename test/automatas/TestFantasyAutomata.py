import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.FantasyAutomata import FantasyAutomata
import unittest


class TestFantasyAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = FantasyAutomata()

    def test_fantasy(self):
        self.automata.add_transition(self.automata.q0, "fantasy", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)

    def test_start_2(self):
        self.automata.add_transition(self.automata.q1, "In the heart of the enchanted forest, we encountered a magical creature whose wisdom and guidance would be crucial in our mission", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_resolution_1(self):
        self.automata.add_transition(self.automata.q2, "The heroes uncover ancient clues that lead them to the first challenge in their quest for the", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

    def test_resolution_2(self):
        self.automata.add_transition(self.automata.q2, "The heroes encounter a powerful enemy also seeking the artifact, triggering an epic showdown for the", self.automata.q5)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q5
        self.assertEqual(self.automata.current_state, self.automata.q5)

if __name__ == "__main__":
    unittest.main()
