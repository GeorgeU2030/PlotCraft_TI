from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class FantasyAutomata(DeterministicFiniteAutomaton):
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
        self.add_transition(self.q0, "fantasy", self.q1)

        # inicios
        self.add_transition(self.q1, "We stumbled upon mysterious inscriptions that would lead us to the first challenge in our quest for the magical artifact", self.q2)
        self.add_transition(self.q1, "In the heart of the enchanted forest, we encountered a magical creature whose wisdom and guidance would be crucial in our mission", self.q3)


        # desenlace
        self.add_transition(self.q2, "The heroes uncover ancient clues that lead them to the first challenge in their quest for the", self.q4)
        self.add_transition(self.q2, "The heroes encounter a powerful enemy also seeking the artifact, triggering an epic showdown for the", self.q5)

        self.add_transition(self.q3, "The heroes ally with a magical creature that guides them through an enchanted forest in search of the next clue for the", self.q6)
        self.add_transition(self.q3, "The heroes discover an ancient spellbook containing crucial hints about the location of the", self.q7)


        
        #finales

        self.add_transition(self.q4, "They successfully solve the first challenge and move on to the next step of their adventure", self.q8)
        self.add_transition(self.q4, "They fail to solve the first challenge and must rethink their strategy before proceeding", self.q8)

        self.add_transition(self.q5, "They defeat the enemy and continue their quest with determination", self.q8)
        self.add_transition(self.q5, "The enemy overpowers them and gains an advantage in the race for the artifact", self.q8)

        self.add_transition(self.q6, "The magical creature becomes a valuable ally, sharing crucial knowledge", self.q8)
        self.add_transition(self.q6, "The magical creature betrays them, leading them into a deadly trap in the enchanted forest", self.q8)

        self.add_transition(self.q7, "They use the magic from the book to advance in their quest, gaining an advantage over their rivals", self.q8)
        self.add_transition(self.q7, "The misuse of the book triggers a magical disaster that puts them in grave danger", self.q8)
         
        
        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


