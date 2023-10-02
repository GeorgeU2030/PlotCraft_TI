from pyformlang.cfg import CFG
import random

class GrammarFantasy():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> We stumbled upon ancient and cryptic inscriptions etched into the stones, symbols that held the secrets to unlocking the magical artifact.
            S -> As we ventured deeper into the forgotten ruins, our eyes fell upon mysterious inscriptions, their hidden meanings pointing us toward the location of the mystical artifact.
            S -> Our journey through the uncharted wilderness took an unexpected turn when we uncovered a series of enigmatic markings on an ancient tablet. 
        """
        self.gic_inicio_2 = """
            S -> Deep within the mystical forest, our path intersected with a remarkable and otherworldly creature. Its presence, imbued with ancient magic.
            S -> Amidst the enchanting foliage of the forest's core, we came face to face with a creature of legends. Its aura radiated with magical knowledge.
            S -> As we ventured deeper into the heart of the enchanted forest, we were unexpectedly greeted by a mystical being, whose innate connection to the ancient magic in our mission
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
    
    
    