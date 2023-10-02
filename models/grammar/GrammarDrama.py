from pyformlang.cfg import CFG
import random

class GrammarDrama():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar.
            S -> Strolling down the busy city street, I suddenly noticed a familiar figure in the distance.
            S -> As I walked along the crowded urban avenue, I caught sight of someone I thought I knew.
        """
        self.gic_inicio_2 = """
            S -> Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see.
            S -> In the midst of the crowd at the outdoor concert, my gaze met with someone I hadn't anticipated encountering.
            S -> Surrounded by the audience at the open-air performance, my eyes connected with an unexpected face.
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
    
    
    