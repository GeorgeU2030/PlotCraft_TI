from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class DramaAutomata(DeterministicFiniteAutomaton):
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
        self.add_transition(self.q0, "drama", self.q1)

        # inicios
        self.add_transition(self.q1, "While walking along the bustling city avenue, I spotted someone in the distance who seemed familiar", self.q2)
        self.add_transition(self.q1, "Amidst the crowd gathering at the open-air concert, I locked eyes with someone I didn't expect to see", self.q3)


        # desenlace
        self.add_transition(self.q2, "I recognize each other immediately and we start talking, reminiscing about the shared moments in", self.q4)
        self.add_transition(self.q2, "We look at each other in surprise and hesitate to approach each other, creating tension in", self.q5)

        self.add_transition(self.q3, "We meet in an unexpected place, such as an extraordinary event or situation, which forces us to interact in", self.q6)
        self.add_transition(self.q3, "We cross paths in an unusual place but do not interact directly at first, Then we met in", self.q7)


        
        #finales

        self.add_transition(self.q4, "Both of us decide to spend more time together and revive the friendship or relationship we had", self.q8)
        self.add_transition(self.q4, "Despite the recognition, one of us decides to distance themselves, avoiding a resumption of the relationship", self.q8)

        self.add_transition(self.q5, "Eventually, we dare to speak and decide to try to heal the wounds of the past", self.q8)
        self.add_transition(self.q5, "Each of us goes our separate way, carrying the uncertainty of what could have been", self.q8)

        self.add_transition(self.q6, "During the experience, we find the opportunity to apologize and reconcile", self.q8)
        self.add_transition(self.q6, "Despite the initial surprise, we choose to ignore each other and continue with our lives", self.q8)

        self.add_transition(self.q7, "Over time, curiosity leads us to approach and eventually talk about our past", self.q8)
        self.add_transition(self.q7, "Although we share the same space, we decide not to address the past and move forward", self.q8)
         
        
        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


