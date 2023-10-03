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
       

        self.current_state = self.q0
        # estado inicial
        self.initial_state = self.q0

        # transiciones entre estados - tematica
        self.add_transition(self.q0, "alien", self.q1)
        self.add_transition(self.q0, "space", self.q2)

        # inicios
        self.add_transition(self.q1, "Alien spacecraft descend upon Earth, causing panic and confusion among the population", self.q3)
        self.add_transition(self.q1, "The human resistance joins forces in an effort to repel the alien invasion", self.q4)

        self.add_transition(self.q2, "The Ares spacecraft successfully lifts off from Earth, marking the beginning of an exciting mission", self.q10)
        self.add_transition(self.q2, "During the launch of the Ares spacecraft, technical issues arise that jeopardize the mission", self.q11)


        # desenlace
        self.add_transition(self.q3, "The alien spaceships descend upon Earth, causing panic and bewilderment among the population of", self.q5)
        self.add_transition(self.q3, "The aliens make contact and reveal their intentions, demanding Earth's resources or threatening catastrophic consequences in", self.q6)

        self.add_transition(self.q4, "Humanity organizes to confront the alien threat and fights valiantly in", self.q7)
        self.add_transition(self.q4, "The aliens intensify their offensive, causing devastation on Earth specially in", self.q8)


        # -------- space

        self.add_transition(self.q10, "The Ares spacecraft safely lands on Mars, and the crew prepares to explore the planet of", self.q12)
        self.add_transition(self.q10, "En route to the planet, the Ares spacecraft encounters a nearby asteroid and decides to investigate it before continuing to their destination to", self.q13)

        self.add_transition(self.q11, "The crew of the Ares spacecraft works tirelessly to address the technical issues and continue the mission to", self.q14)
        self.add_transition(self.q11, "Despite the technical issues, the crew of the Ares spacecraft decides to press on with the mission and overcome the obstacles and arrive to", self.q15)

        
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

        self.add_transition(self.q12, "During their exploration of Planet, the crew makes a surprising discovery that could change our understanding of the planet", self.q9)
        self.add_transition(self.q12, "The Ares spacecraft crew returns to Earth with valuable data and samples from this planet, contributing to scientific advancements", self.q9)

        self.add_transition(self.q13, "The exploration of the asteroid reveals valuable information about the composition of these celestial bodies, which could benefit future space missions", self.q9)
        self.add_transition(self.q13, "The crew of the Ares spacecraft documents and studies the asteroid, providing key data for scientific research", self.q9)

        self.add_transition(self.q14, "Despite the obstacles, the crew successfully resolves the technical issues and continues their exploration on the planet", self.q9)
        self.add_transition(self.q14, "The crew's skills and dedication are put to the test, but they manage to overcome the technical challenges and advance in their mission", self.q9)

        self.add_transition(self.q15, "The determination of the crew drives them to overcome challenges and continue the exploration on the planet", self.q9)
        self.add_transition(self.q15, "Despite setbacks, the crew maintains their spirit and forges ahead toward the planet with resolve", self.q9)

        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


