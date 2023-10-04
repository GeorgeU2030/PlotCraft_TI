import unittest
import re

class TestHistoricalChoices(unittest.TestCase):
    def test_palaceExpressions(self):
        jungleExp1 = re.compile(r"In the silent hallways of the royal palace, the rumor of a conspiracy that destabilize the city's destiny forever")
        jungleExp2 = re.compile(r"On a dark and ominous night, flames rose over the city's buildings, causing a fire that would consume everything")

        self.assertTrue(jungleExp1.match("In the silent hallways of the royal palace, the rumor of a conspiracy that destabilize the city's destiny forever"))
        self.assertTrue(jungleExp2.match("On a dark and ominous night, flames rose over the city's buildings, causing a fire that would consume everything"))
        self.assertFalse(jungleExp1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(jungleExp2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"After a thorough investigation, the brave detectives finally uncovered the conspiracy behind, that shook society in")
        dev2 = re.compile(r"The tragedy of the fire became a tool for political manipulation, with leaders making decisions that would change the fate of")
        dev3 = re.compile(r"Chaos reigned for days as the fire swept through buildings and lives, leaving behind a devastation that seemed impossible in")
        dev4 = re.compile(r"With determination and unity, the city rose from the ashes of the fire, rebuilding its buildings with a rebirth that inspired everyone from")

        self.assertTrue(dev1.match("After a thorough investigation, the brave detectives finally uncovered the conspiracy behind, that shook society in"))
        self.assertTrue(dev2.match("The tragedy of the fire became a tool for political manipulation, with leaders making decisions that would change the fate of"))
        self.assertFalse(dev1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(dev2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

    def test_endExpressions(self):
        end1 = re.compile(r"An informant reveals a plot to overthrow the king, triggering an investigation at the court")
        end2 = re.compile(r"Although there are suspicions of a conspiracy, no concrete evidence is found, leading to paranoia at the court")
        end3 = re.compile(r"The plot turns out to be a political maneuver designed to eliminate rivals for the throne")
        end4 = re.compile(r"Those implicated in the plot are arrested, but it is discovered that they were mere pawns in a larger game")
        end5 = re.compile(r"The fire ravages a significant portion of the city, causing unprecedented devastation")
        end6 = re.compile(r"Despite desperate efforts, the fire consumes the city almost entirely")
        end7 = re.compile(r"After the destruction, the city is rebuilt with a renewed architecture and becomes a symbol of resilience")
        end8 = re.compile(r"Although the city recovers, the scars of the fire endure in the collective memory of the population")

        self.assertTrue(end1.match("An informant reveals a plot to overthrow the king, triggering an investigation at the court"))
        self.assertTrue(end2.match("Although there are suspicions of a conspiracy, no concrete evidence is found, leading to paranoia at the court"))
        self.assertFalse(end1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertFalse(end2.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))

if __name__ == "__main__":
    unittest.main()
