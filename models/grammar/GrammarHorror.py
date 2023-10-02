from pyformlang.cfg import CFG
import random

class GrammarHorror():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> As we explored the abandoned mansion, we felt that our footsteps echoed more than usual, and we decided to venture further into the enveloping darkness.
            S -> The eerie atmosphere inside the abandoned mansion sent chills down our spines as we cautiously moved deeper into the darkness.
            S -> An unsettling feeling washed over us as we stepped into the desolate mansion, and we steeled ourselves for what horrors we might uncover.
        """
        self.gic_inicio_2 = """
           S -> Upon entering the eerie lobby of the haunted hotel, a shiver ran down our spines, but we chose to confront our worst nightmares and check the oldest rooms.
           S -> The chilling atmosphere in the haunted hotel's lobby sent a shiver down our spines, but we steeled ourselves to confront our deepest fears and explore the oldest rooms.
           S -> As we stepped into the unsettling lobby of the haunted hotel, a sense of dread washed over us, but our determination to face our worst nightmares led us to investigate the oldest rooms.
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
    
    
    