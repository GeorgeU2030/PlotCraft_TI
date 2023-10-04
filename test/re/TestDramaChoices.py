import unittest
import re

class TestDramaChoices(unittest.TestCase):
    def test_jungleExpressions(self):
        jungleExp1 = re.compile(r"While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar")
        jungleExp2 = re.compile(r"Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see")

        self.assertTrue(jungleExp1.match("While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar"))
        self.assertTrue(jungleExp2.match("Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see"))
        self.assertFalse(jungleExp1.match("We recognize each other immediately and start talking"))
        self.assertFalse(jungleExp2.match("We meet in an unexpected place, such as an extraordinary event or situation"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"I recognize each other immediately and we start talking, reminiscing about the shared moments in")
        dev2 = re.compile(r"We look at each other in surprise and hesitate to approach each other, creating tension in")
        dev3 = re.compile(r"We meet in an unexpected place, such as an extraordinary event or situation, which forces us to interact in")
        dev4 = re.compile(r"We cross paths in an unusual place but do not interact directly at first, Then we met in")

        self.assertTrue(dev1.match("I recognize each other immediately and we start talking, reminiscing about the shared moments in"))
        self.assertTrue(dev2.match("We look at each other in surprise and hesitate to approach each other, creating tension in"))
        self.assertFalse(dev1.match("While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar"))
        self.assertFalse(dev2.match("We meet in an unexpected place, such as an extraordinary event or situation"))

    def test_endExpressions(self):
        end1 = re.compile(r"Both of us decide to spend more time together and revive the friendship or relationship we had")
        end2 = re.compile(r"Despite the recognition, one of us decides to distance themselves, avoiding a resumption of the relationship")
        end3 = re.compile(r"Eventually, we dare to speak and decide to try to heal the wounds of the past")
        end4 = re.compile(r"Each of us goes our separate way, carrying the uncertainty of what could have been")
        end5 = re.compile(r"During the experience, we find the opportunity to apologize and reconcile")
        end6 = re.compile(r"Despite the initial surprise, we choose to ignore each other and continue with our lives")
        end7 = re.compile(r"Over time, curiosity leads us to approach and eventually talk about our past")
        end8 = re.compile(r"Although we share the same space, we decide not to address the past and move forward")

        self.assertTrue(end1.match("Both of us decide to spend more time together and revive the friendship or relationship we had"))
        self.assertTrue(end2.match("Despite the recognition, one of us decides to distance themselves, avoiding a resumption of the relationship"))
        self.assertFalse(end1.match("I recognize each other immediately and start talking, reminiscing about the shared moments in"))
        self.assertFalse(end2.match("We meet in an unexpected place, such as an extraordinary event or situation"))

if __name__ == "__main__":
    unittest.main()
