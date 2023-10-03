from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class HorrorAutomata(DeterministicFiniteAutomaton):
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
        self.add_transition(self.q0, "horror", self.q1)

        # inicios
        self.add_transition(self.q1, "As we explored the abandoned mansion, we felt that our footsteps echoed more than usual, and we decided to venture further", self.q2)
        self.add_transition(self.q1, "Upon entering the eerie lobby of the haunted hotel, a shiver ran down our spines, but we chose to confront our nightmares", self.q3)


        # desenlace
        self.add_transition(self.q2, "The friends decide to explore the mansion further in search of answers and find a secret door in the", self.q4)
        self.add_transition(self.q2, "The friends choose to leave the mansion, feeling that something is watching them like a", self.q5)

        self.add_transition(self.q3, "The friends decide to investigate the oldest rooms of the hotel, where listen scream and some weird facts happen like", self.q6)
        self.add_transition(self.q3, "They choose to leave the hotel due to the intensity of the paranormal experiences they face like", self.q7)


        #finales

        self.add_transition(self.q4, "Upon opening the secret door, they reveal a hidden passage leading to an even more sinister in the place", self.q8)
        self.add_transition(self.q4, "The secret door is sealed shut, and they cannot open it, leaving the abandoned mansion behind", self.q8)

        self.add_transition(self.q5, "As they exit the mansion, they hear footsteps behind them but see no one, filling them with fear", self.q8)
        self.add_transition(self.q5, "They leave the mansion without incident, but a strange shadow looms over them as they walk away", self.q8)

        self.add_transition(self.q6, "In one of the rooms, they find evidence of paranormal activity and choose to continue their investigation", self.q8)
        self.add_transition(self.q6, "They find nothing unusual in the old rooms and decide to leave the hotel", self.q8)

        self.add_transition(self.q7, "As they prepare to leave, a terrifying apparition blocks their way, leaving them trapped in the haunted hotel", self.q8)
        self.add_transition(self.q7, "They manage to leave the hotel, terrified, but they feel that something dark is following them as they walk away", self.q8)
         
        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


