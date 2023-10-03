from pyformlang.cfg import CFG
import random

class GrammarHistorical():
    
    def __init__(self):
        self.gic_inicio_1 = """
           S -> In the hushed corridors of the royal palace, whispers of a conspiracy lurk in the shadows, threatening to destabilize the kingdom and alter the course of the court forever.
           S -> Within the silent halls of the royal court, murmurs of a plot loom in obscurity, poised to disrupt the realm and reshape the destiny of the court.
           S -> Amidst the opulent chambers of the palace, rumors of a clandestine scheme echo softly, hinting at a turbulent upheaval that could rewrite the annals of court history.
        """
        self.gic_inicio_2 = """
           S -> As the night fell, flames engulfed the city, unleashing a devastating inferno.
           S -> In the midst of darkness, a raging fire consumed the city, leaving destruction in its wake.
           S -> The city was plunged into chaos as a fierce conflagration tore through its streets, a cataclysmic event that would be remembered for generations.
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
    
    
    