from pyformlang.cfg import CFG
import random

class GrammarMystery():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room.
            S -> While exploring the main room of this place, I stumble upon an intriguing mystery—an ancient encrypted letter that defies explanation.
            S -> Amidst the dusty relics in the main room of this place, I come across an enigmatic puzzle—an ancient encrypted letter with no apparent solution.
        """
        self.gic_inicio_2 = """
            S -> I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect.
            S -> At the crime scene, I stumble upon a new lead that dramatically alters the course of the investigation—an unidentified fingerprint that doesn't correspond to any known suspect.
            S -> While examining the evidence at the crime scene, I uncover a pivotal clue—a fingerprint that challenges everything we thought we knew, as it doesn't belong to any known suspect.
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
    
    
    