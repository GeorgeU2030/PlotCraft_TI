import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

import unittest

from src.models.automata.AdventureAutomata import AdventureAutomata


class TestAdventureAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = AdventureAutomata()

    def test_jungle_exploration(self):
        self.automata.add_transition(self.automata.q0, "jungle exploration", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)

    def test_himalaya(self):
        self.automata.add_transition(self.automata.q0, "himalaya", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_treasure_hunt(self):
        self.automata.add_transition(self.automata.q0, "treasure hunt", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)

    def test_desert_race(self):
        self.automata.add_transition(self.automata.q0, "desert race", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

if __name__ == "__main__":
    unittest.main()

