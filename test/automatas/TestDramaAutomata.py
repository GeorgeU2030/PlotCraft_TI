import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from src.models.automata.DramaAutomata import DramaAutomata
import unittest

class TestDramaAutomata(unittest.TestCase):
    def setUp(self):
        self.automata = DramaAutomata()

    def test_drama(self):
        self.automata.add_transition(self.automata.q0, "drama", self.automata.q1)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q1
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.add_transition(self.automata.q1, "While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar", self.automata.q2)
        self.assertEqual(self.automata.current_state, self.automata.q1)
        self.automata.current_state = self.automata.q2
        self.assertEqual(self.automata.current_state, self.automata.q2)


    def test_start_2(self):
        self.automata.add_transition(self.automata.q1, "Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see", self.automata.q3)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q3
        self.assertEqual(self.automata.current_state, self.automata.q3)

    def test_resolution_1(self):
        self.automata.add_transition(self.automata.q2, "I recognize each other immediately and we start talking, reminiscing about the shared moments in", self.automata.q4)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q4
        self.assertEqual(self.automata.current_state, self.automata.q4)

    def test_resolution_2(self):
        self.automata.add_transition(self.automata.q2, "We look at each other in surprise and hesitate to approach each other, creating tension in", self.automata.q5)
        self.assertEqual(self.automata.current_state, self.automata.q0)
        self.automata.current_state = self.automata.q5
        self.assertEqual(self.automata.current_state, self.automata.q5)


if __name__ == "__main__":
    unittest.main()
