from pyformlang.cfg import CFG
import random

class GrammarAdventure():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> The player wakes up in a tent in the middle of the jungle.
            S -> Upon waking up, the player finds themselves in a tent surrounded by dense vegetation in the jungle.
            S -> After a deep sleep, the player realizes they are in a tent in the middle of the jungle.
        """
        self.gic_inicio_2 = """
            S -> The player arrives at a hidden tribal village in the jungle.
            S -> After a long journey, the player discovers a hidden tribal village nestled within the dense jungle.
            S -> As the player ventures into the jungle, they come across a hidden tribal village.
        """
        self.gic_inicio_3 = """
            S -> Upon the serendipitous discovery of an ancient treasure map, you embark on a thrilling expedition, culminating in your arrival on a deserted island.
            S -> As you uncover the secrets hidden within an age-old treasure map, your epic journey unfolds, eventually leading you to the shores of a secluded and uninhabited island.
            S -> Your destiny takes a fateful turn when you stumble upon the dusty parchment of an ancient treasure map, setting in motion a grand adventure.
        """
        self.gic_inicio_4 = """
            S -> As the sun sets over the vast ocean, painting the sky with shades of orange and pink, you step onto the shore of a beautiful and remote tropical island. 
            S -> With the ancient treasure map clutched in your hand, you set foot on the untouched sands of a breathtaking tropical island. The sun's warm rays caress your skin
            S -> Your journey in search of adventure and riches has brought you to the edge of the world, where a pristine tropical island awaits your exploration. 
        """
        self.gic_inicio_5 = """
            S -> A team of brave explorers, fueled by their unwavering spirit of adventure and a deep passion for discovery, embarks on an ambitious expedition to the majestic Himalayas.
            S -> In a remote corner of the world, far from the comforts of civilization, a group of intrepid explorers, each carrying dreams as vast as the mountains they're about to scale.
            S -> With mountaineering gear meticulously prepared and their resolve steeled against the challenges that lie ahead, a courageous team of adventurers commences an epic expedition.
        """
        self.gic_inicio_6 = """
            S -> A group of nature enthusiasts and friends, bound by their love for the great outdoors and a sense of camaraderie, embarks on an exciting journey through the majestic Himalayas.
            S -> Amidst laughter and shared excitement, a close-knit group of nature enthusiasts and friends sets out on an unforgettable journey through the rugged terrain of the Himalayas.
            S -> With backpacks filled with curiosity and hearts brimming with adventure, a group of lifelong friends and nature enthusiasts begins a remarkable journey through the Himalayas.
        """
        self.gic_inicio_7="""
        S -> At the start of the desert race, the competitors prepare to face challenges that will test their skills and endurance.
        S -> The racers, adrenaline pumping through their veins, gear up for the desert competition, fully aware that they're about to confront adversity in the unforgiving dunes.
        S -> As the desert race commences, participants get ready to tackle the upcoming obstacles, knowing that only the most determined will emerge victorious in this grueling test of mettle.
        """
        self.gic_inicio_8="""
        S -> The race begins in the heart of the desert in the night, with the racers ready to embark on a thrilling journey through the darkness.
        S -> Under the desert night sky, the race kicks off with the competitors poised for an adrenaline-pumping adventure through the vast sands.
        S -> As the desert race starts in the depths of the night, racers prepare to navigate the challenging terrain, knowing that the darkness will be their ultimate test.
        """
        self.grammar1 = CFG.from_text(self.gic_inicio_1)
        self.grammar2 = CFG.from_text(self.gic_inicio_2)
        self.grammar3 = CFG.from_text(self.gic_inicio_3)
        self.grammar4 = CFG.from_text(self.gic_inicio_4)
        self.grammar5 = CFG.from_text(self.gic_inicio_5)
        self.grammar6 = CFG.from_text(self.gic_inicio_6)
        self.grammar7 = CFG.from_text(self.gic_inicio_7)
        self.grammar8 = CFG.from_text(self.gic_inicio_8)

    def descgic1(self):
        produccion = random.choice(list(self.grammar1.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic2(self):
        produccion = random.choice(list(self.grammar2.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic3(self):
        produccion = random.choice(list(self.grammar3.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

    def descgic4(self):
        produccion = random.choice(list(self.grammar4.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic5(self):
        produccion = random.choice(list(self.grammar5.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

    def descgic6(self):
        produccion = random.choice(list(self.grammar6.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

    def descgic7(self):
        produccion = random.choice(list(self.grammar7.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

    def descgic8(self):
        produccion = random.choice(list(self.grammar8.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
