import unittest
import re

class TestFantasyChoices(unittest.TestCase):
    def test_jungleExpressions(self):
        jungleExp1 = re.compile(r"We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact")
        jungleExp2 = re.compile(r"In the heart of the enchanted forest, we encountered a magical creature whose wisdom and guidance would be crucial in our mission")

        self.assertTrue(jungleExp1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertTrue(jungleExp2.match("In the heart of the enchanted forest, we encountered a magical creature whose wisdom and guidance would be crucial in our mission"))
        self.assertFalse(jungleExp1.match("The heroes uncover ancient clues that lead them to the first challenge in their quest for the"))
        self.assertFalse(jungleExp2.match("The heroes ally with a magical creature that guides them through an enchanted forest in search of the next clue for the"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"The heroes uncover ancient clues that lead them to the first challenge in their quest for the")
        dev2 = re.compile(r"The heroes encounter a powerful enemy also seeking the artifact, triggering an epic showdown for the")
        dev3 = re.compile(r"The heroes ally with a magical creature that guides them through an enchanted forest in search of the next clue for the")
        dev4 = re.compile(r"The heroes discover an ancient spellbook containing crucial hints about the location of the")

        self.assertTrue(dev1.match("The heroes uncover ancient clues that lead them to the first challenge in their quest for the"))
        self.assertTrue(dev2.match("The heroes encounter a powerful enemy also seeking the artifact, triggering an epic showdown for the"))
        self.assertFalse(dev1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertFalse(dev2.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))

    def test_endExpressions(self):
        end1 = re.compile(r"They successfully solve the first challenge and move on to the next step of their adventure")
        end2 = re.compile(r"They fail to solve the first challenge and must rethink their strategy before proceeding")
        end3 = re.compile(r"They defeat the enemy and continue their quest with determination")
        end4 = re.compile(r"The enemy overpowers them and gains an advantage in the race for the artifact")
        end5 = re.compile(r"The magical creature becomes a valuable ally, sharing crucial knowledge")
        end6 = re.compile(r"The magical creature betrays them, leading them into a deadly trap in the enchanted forest")
        end7 = re.compile(r"They use the magic from the book to advance in their quest, gaining an advantage over their rivals")
        end8 = re.compile(r"The misuse of the book triggers a magical disaster that puts them in grave danger")

        self.assertTrue(end1.match("They successfully solve the first challenge and move on to the next step of their adventure"))
        self.assertTrue(end2.match("They fail to solve the first challenge and must rethink their strategy before proceeding"))
        self.assertFalse(end1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertFalse(end2.match("The heroes uncover ancient clues that lead them to the first challenge in their quest for the"))

if __name__ == "__main__":
    unittest.main()
