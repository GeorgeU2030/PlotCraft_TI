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
        self.add_transition(self.q1, "You wake up in the middle of the jungle", self.q5)
        self.add_transition(self.q1, "You arrive at a hidden village in the jungle", self.q6)

        # desenlace
        self.add_transition(self.q5, "You explore the jungle and find the waterfall", self.q7)
        self.add_transition(self.q5, "You find traces of an ancient civilization", self.q8)

        self.add_transition(self.q6, "You go down the river and arrive at a mysterious temple", self.q9)
        self.add_transition(self.q6, "You find and join the archaeological expedition", self.q10)
        #finales

        self.add_transition(self.q7, "At the waterfall, you find a treasure and become a legend", self.q11)
        self.add_transition(self.q7, "There, you encounter a tribe and adopt their jungle way of life", self.q11)

        self.add_transition(self.q8, "You return home with valuable artifacts and become an expert", self.q11)
        self.add_transition(self.q8, "You are rescued by a team from civilization and return home", self.q11)

        self.add_transition(self.q9, "You become a renowned jungle explorer", self.q11)
        self.add_transition(self.q9, "You get trapped forever in the temple after falling into a trap", self.q11)

        self.add_transition(self.q10, "You find many treasures on the expedition and become a millionaire", self.q11)
        self.add_transition(self.q10, "You get lost in the jungle forever, becoming a lost legend", self.q11)
         

    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


