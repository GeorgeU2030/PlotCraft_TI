from pyformlang.cfg import CFG
import random

class GrammarAdventure():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> El jugador despierta en una tienda de campaña en medio de la jungla.
            S -> Al despertar, el jugador se encuentra en una tienda de campaña rodeada de densa vegetación en la jungla.
            S -> Después de un sueño profundo, el jugador se da cuenta de que está en una tienda de campaña en medio de la selva.
        """
        self.gic_inicio_2 = """
            S -> El jugador llega a una aldea tribal oculta en la jungla.
            S -> Tras una larga travesía, el jugador descubre una aldea tribal escondida entre la densa selva.
            S -> Al adentrarse en la jungla, el jugador se topa con una aldea tribal oculta.
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

