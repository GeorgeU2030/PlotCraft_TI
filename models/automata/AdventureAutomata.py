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

         

    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


