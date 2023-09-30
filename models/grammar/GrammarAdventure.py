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
        self.grammar1 = CFG.from_text(self.gic_inicio_1)
        self.grammar2 = CFG.from_text(self.gic_inicio_2)

    def descgic1(self):
        produccion = random.choice(list(self.grammar1.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic2(self):
        produccion = random.choice(list(self.grammar2.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

