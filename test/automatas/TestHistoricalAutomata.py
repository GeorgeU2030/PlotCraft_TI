import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.HistoricalAutomata import HistoricalAutomata
import unittest

class TestHistoricalAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = HistoricalAutomata()

    def test_historical(self):
        self.automata.add_transition(self.automata.q0, "historical", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "In the silent hallways of the royal palace, the rumor of a conspiracy that destabilized the city's destiny forever", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)

    def test_start_2(self):
        self.automata.add_transition(self.automata.q1, "On a dark and ominous night, flames rose over the city's buildings, causing a fire that would consume everything", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_resolution_1(self):
        self.automata.add_transition(self.automata.q2, "After a thorough investigation, the brave detectives finally uncovered the conspiracy behind, that shook society in", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

    def test_resolution_2(self):
        self.automata.add_transition(self.automata.q2, "The tragedy of the fire became a tool for political manipulation, with leaders making decisions that would change the fate of", self.automata.q5)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q5
        self.assertEqual(self.automata.current_state, self.automata.q5)


if __name__ == "__main__":
    unittest.main()
