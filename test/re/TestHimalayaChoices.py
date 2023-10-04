import unittest
import re

class TestHimalayaChoices(unittest.TestCase):
    def test_himalayaExpressions(self):
        jungleExp1 = re.compile(r"A team of brave explorers embarks on an expedition to the majestic Himalayas")
        jungleExp2 = re.compile(r"A group of nature enthusiasts and friends embarks on a journey through the Himalayas")

        self.assertTrue(jungleExp1.match("A team of brave explorers embarks on an expedition to the majestic Himalayas"))
        self.assertTrue(jungleExp2.match("A group of nature enthusiasts and friends embarks on a journey through the Himalayas"))
        self.assertFalse(jungleExp1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertFalse(jungleExp2.match("The heroes uncover ancient clues that lead them to the first challenge in their quest for the"))

    def test_developmentExpressions(self):
        dev1 = re.compile(r"As they ascend the high peaks, they face natural challenges such as snowstorms and")
        dev2 = re.compile(r"Their expedition becomes complicated due to fatigue and extreme weather")
        dev3 = re.compile(r"While traveling through the mountains, they discover ancient monasteries and form friendships with the community")
        dev4 = re.compile(r"The journey becomes challenging due to altitude and adapting to the environment, leading them to make crucial")

        self.assertTrue(dev1.match("As they ascend the high peaks, they face natural challenges such as snowstorms and"))
        self.assertTrue(dev2.match("Their expedition becomes complicated due to fatigue and extreme weather"))
        self.assertFalse(dev1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertFalse(dev2.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))

    def test_endExpressions(self):
        end1 = re.compile(r"They reach one of the highest summits, feeling the satisfaction of conquest and the breathtaking panoramic view of the mountains")
        end2 = re.compile(r"Despite not reaching the summit, the experience strengthens their bond as a team and fills them with awe for the majesty of the Himalayas")
        end3 = re.compile(r"They decide to return safely, recognizing that safety comes first, but with the determination to return in the future")
        end4 = re.compile(r"Their adventure in the Himalayas changes them profoundly, inspiring them to explore other corners of the world and appreciate the beauty of nature")
        end5 = re.compile(r"They visit a Buddhist monastery and are warmly welcomed, learning about the spirituality and culture of the Himalayas")
        end6 = re.compile(r"They join a local celebration and take part in spiritual practices that enrich their experience")
        end7 = re.compile(r"Although they decide to return earlier than planned, they deeply value their experience in the Himalayas and their connection with nature")
        end8 = re.compile(r"Their adventure in the Himalayas inspires them to lead a more mindful and environmentally respectful lifestyle")

        self.assertTrue(end1.match("They reach one of the highest summits, feeling the satisfaction of conquest and the breathtaking panoramic view of the mountains"))
        self.assertTrue(end2.match("Despite not reaching the summit, the experience strengthens their bond as a team and fills them with awe for the majesty of the Himalayas"))
        self.assertFalse(end1.match("We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact"))
        self.assertFalse(end2.match("The heroes uncover ancient clues that lead them to the first challenge in their quest for the"))

if __name__ == "__main__":
    unittest.main()
