from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class AdventureAutomata(DeterministicFiniteAutomaton):
    def __init__(self):
        super().__init__()
        self.transitions = {}
        # estados
        self.q0 = State("q0")
        self.q1 = State("q1")
        self.q2 = State("q2")
        self.q3 = State("q3")
        self.q4 = State("q4")
        self.q5 = State("q5")
        self.q6 = State("q6")
        self.q7 = State("q7")
        self.q8 = State("q8")
        self.q9 = State("q9")
        self.q10 = State("q10")
        self.q11 = State("q11")

        self.current_state = self.q0
        # estado inicial
        self.initial_state = self.q0

        # transiciones entre estados - tematica
        self.add_transition(self.q0, "jungle exploration", self.q1)
        self.add_transition(self.q0, "himalaya", self.q3)
        self.add_transition(self.q0, "treasure hunt", self.q2)
        self.add_transition(self.q0, "desert race", self.q4)

        # inicios
        self.add_transition(self.q1, "Despiertas en medio de la jungla", self.q5)
        self.add_transition(self.q1, "Llegas a una aldea oculta en la jungla", self.q6)

        # desenlace
        self.add_transition(self.q5, "Exploras la jungla y encuentras la cascada", self.q7)
        self.add_transition(self.q5, "Encuentras rastros de una antigua de la civilizacion", self.q8)

        self.add_transition(self.q6, "Te vas por el río y llegas a un misterioso templo", self.q9)
        self.add_transition(self.q6, "Encuentras y te unes a la expedicion arqueologica", self.q10)

        #finales

        self.add_transition(self.q7, "En la cascada encuentras un tesoro y te conviertes en una leyenda", self.q11)
        self.add_transition(self.q7, "alli encuentras una tribu y adoptas su estilo de vida en la jungla", self.q11)

        self.add_transition(self.q8, "Regresas a casa con artefactos valiosos y te conviertes en un experto", self.q11)
        self.add_transition(self.q8, "Eres rescatado por un equipo de la civilizacion y regresas a casa", self.q11)

        self.add_transition(self.q9, "Te conviertes en un renombrado explorador de la jungla", self.q11)
        self.add_transition(self.q9, "En el templo quedas atrapado por siempre al caer en una trampa", self.q11)

        self.add_transition(self.q10, "Encuentras muchos tesoros en la expedicion y eres millonario", self.q11)
        self.add_transition(self.q10, "Te pierdes en la jungla para siempre, convirtiendote en una leyenda perdida", self.q11)
         

    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


