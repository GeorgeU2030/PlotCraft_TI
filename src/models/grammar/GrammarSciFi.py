from pyformlang.cfg import CFG
import random

class GrammarSciFi():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> In a united effort, the human resistance rallies to fend off the alien invasion.
            S -> The human race bands together, striving to repel the alien invaders in a coordinated effort.
            S -> United in purpose, humanity joins forces to push back the extraterrestrial onslaught.
        """
        self.gic_inicio_2 = """
            S -> Alien spacecraft descend from the skies, creating panic and confusion among the population.
            S -> The Earth is plunged into chaos as extraterrestrial ships touch down, instilling fear and bewilderment in people.
            S -> Panic and bewilderment grip the world as alien vessels land on Earth, causing widespread chaos.
        """
        self.gic_inicio_3 = """
            S -> The Ares spacecraft, a marvel of modern engineering, successfully lifts off from Earth, marking the beginning of an exciting mission to explore the mysteries of the cosmos.
            S -> Amid cheers and applause, the Odyssey mission, a testament to human innovation, launches from our planet, carrying the dreams and ambitions of humanity into the vast and uncharted realms of space.
            S -> With a thunderous roar, the Prometheus spacecraft embarks on its historic journey, venturing beyond our home planet and into the great expanse of the universe.
        """
        
        self.gic_inicio_4 = """
            S -> During the launch of the Ares spacecraft, a hushed silence fills the control room as technical issues suddenly arise, casting doubt over the success of the mission.
            S -> In the critical moments of the Ares spacecraft launch, unexpected technical problems surface, sending shockwaves through the team of scientists and engineers.
            S -> As the countdown to the Ares spacecraft launch reaches its climax, unforeseen technical glitches threaten to derail the entire mission.
        """
        
        self.grammar1 = CFG.from_text(self.gic_inicio_1)
        self.grammar2 = CFG.from_text(self.gic_inicio_2)
        self.grammar3 = CFG.from_text(self.gic_inicio_3)
        self.grammar4 = CFG.from_text(self.gic_inicio_4)
        

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
    
    