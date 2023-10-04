import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.SciFiAutomata import SciFiAutomata

import unittest

class TestSciFiAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = SciFiAutomata()

    def test_start_1(self):
        self.automata.add_transition(self.automata.q0, "alien", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "Alien spacecraft descend upon Earth, causing panic and confusion among the population", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_start_2(self):
        self.automata.add_transition(self.automata.q0, "space", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)


    def test_start_4(self):
        self.automata.add_transition(self.automata.q1, "The human resistance joins forces in an effort to repel the alien invasion", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)


if __name__ == "__main__":
    unittest.main()
