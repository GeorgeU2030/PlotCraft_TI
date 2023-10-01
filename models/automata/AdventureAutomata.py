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
        self.q12 = State("q12")
        self.q13 = State("q13")
        self.q14 = State("q14")
        self.q15 = State("q15")
        self.q16 = State("q16")
        self.q17 = State("q17")

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

        self.add_transition(self.q2, "You arrive on a deserted island after discovering an ancient treasure map", self.q12)
        self.add_transition(self.q2, "You arrive on a beautiful tropical island after discovering an ancient treasure map", self.q13)

        # desenlace
        self.add_transition(self.q5, "You explore the jungle and find the waterfall", self.q7)
        self.add_transition(self.q5, "You find traces of an ancient civilization", self.q8)

        self.add_transition(self.q6, "You go down the river and arrive at a mysterious temple", self.q9)
        self.add_transition(self.q6, "You find and join the archaeological expedition", self.q10)


        # -------- treasure hunt

        self.add_transition(self.q12, "Then begin to explore the island in search of clues and buried treasures in island", self.q14)
        self.add_transition(self.q12, "The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by", self.q15)

        self.add_transition(self.q13, "As they explore the island, they discover clues that lead them to secret and lush corners of the island", self.q16)
        self.add_transition(self.q13, "The exploration becomes complicated due to the island's natural dangers, and the treasure hunt is temporarily suspended by", self.q17)

        #finales

        self.add_transition(self.q7, "At the waterfall, you find a treasure and become a legend", self.q11)
        self.add_transition(self.q7, "There, you encounter a tribe and adopt their jungle way of life", self.q11)

        self.add_transition(self.q8, "You return home with valuable artifacts and become an expert", self.q11)
        self.add_transition(self.q8, "You are rescued by a team from civilization and return home", self.q11)

        self.add_transition(self.q9, "You become a renowned jungle explorer", self.q11)
        self.add_transition(self.q9, "You get trapped forever in the temple after falling into a trap", self.q11)

        self.add_transition(self.q10, "You find many treasures on the expedition and become a millionaire", self.q11)
        self.add_transition(self.q10, "You get lost in the jungle forever, becoming a lost legend", self.q11)
         
         # treasure hunt

        self.add_transition(self.q14, "You find a chest with valuable treasures and celebrate their success on the beach", self.q11)
        self.add_transition(self.q14, "Then discover a series of riddles and clues that lead them to another unknown island", self.q11)

        self.add_transition(self.q15, "Then decide to leave the island but remain intrigued by the unresolved mystery", self.q11)
        self.add_transition(self.q15, "You find temporary shelter on the island and learn to survive before embarking on a new journey in search of the treasure", self.q11)

        self.add_transition(self.q16, "Later discover a hidden waterfall with hidden treasures and celebrate their success in the tropical sunlight", self.q11)
        self.add_transition(self.q16, "The clues lead them to a mysterious coral reef where they find ancient artifacts, but also face underwater dangers", self.q11)

        self.add_transition(self.q17, "You decide to go back home, but the island has left a lasting impression on their souls, and they dream of returning someday", self.q11)
        self.add_transition(self.q17, "You find temporary shelter on the island and learn to live in harmony with nature before embarking on new adventures", self.q11)

    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


