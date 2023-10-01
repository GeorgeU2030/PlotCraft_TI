from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class SciFiAutomata(DeterministicFiniteAutomaton):
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
        self.q18 = State("q18")
        self.q19 = State("q19")
        self.q20 = State("q20")
        self.q21 = State("q21")
        self.q22 = State("q22")
        self.q23 = State("q23")
        self.q24 = State("q24")
        self.q25 = State("q25")
        self.q26 = State("q26")
        self.q27 = State("q27")
        self.q28 = State("q28")
        self.q29 = State("q29")

        self.current_state = self.q0
        # estado inicial
        self.initial_state = self.q0

        # transiciones entre estados - tematica
        self.add_transition(self.q0, "alien", self.q1)
        self.add_transition(self.q0, "space", self.q2)

        # inicios
        self.add_transition(self.q1, "Alien spacecraft descend upon Earth, causing panic and confusion among the population", self.q3)
        self.add_transition(self.q1, "The human resistance joins forces in an effort to repel the alien invasion", self.q4)

        self.add_transition(self.q2, "You arrive on a deserted island after discovering an ancient treasure map", self.q12)
        self.add_transition(self.q2, "You arrive on a beautiful tropical island after discovering an ancient treasure map", self.q13)


        # desenlace
        self.add_transition(self.q3, "The alien spaceships descend upon Earth, causing panic and bewilderment among the population of", self.q5)
        self.add_transition(self.q3, "The aliens make contact and reveal their intentions, demanding Earth's resources or threatening catastrophic consequences in", self.q6)

        self.add_transition(self.q4, "Humanity organizes to confront the alien threat and fights valiantly in", self.q7)
        self.add_transition(self.q4, "The aliens intensify their offensive, causing devastation on Earth specially in", self.q8)


        # -------- space

        self.add_transition(self.q12, "Then begin to explore the island in search of clues and buried treasures in island", self.q14)
        self.add_transition(self.q12, "The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by", self.q15)

        self.add_transition(self.q13, "As they explore the island, they discover clues that lead them to secret and lush corners of the island", self.q16)
        self.add_transition(self.q13, "The exploration becomes complicated due to the island's natural dangers, and the treasure hunt is temporarily suspended by", self.q17)

        
        #finales

        self.add_transition(self.q5, "World leaders convene experts and scientists to analyze the ships and communicate with the aliens", self.q9)
        self.add_transition(self.q5, "The civilian population seeks refuge and watches in awe as the military prepares to defend against the invasion", self.q9)

        self.add_transition(self.q6, "World leaders attempt negotiations with the aliens to avoid conflict, while some challenge their authority", self.q9)
        self.add_transition(self.q6, "Humanity prepares to resist the alien invasion, uniting forces to protect their planet", self.q9)

        self.add_transition(self.q7, "An epic battle unfolds against the alien invaders, where humans display their bravery and determination", self.q9)
        self.add_transition(self.q7, "Scientists discover a weakness in alien technology and work on a plan to defeat the invaders", self.q9)

        self.add_transition(self.q8, "Humanity suffers significant losses but manages to resist and defend their planet against the alien invasion", self.q9)
        self.add_transition(self.q8, "Despite their bravery, humanity faces overwhelming difficulties and seeks a desperate solution to halt the invasion", self.q9)
         
         # finales space

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
    
   

    


