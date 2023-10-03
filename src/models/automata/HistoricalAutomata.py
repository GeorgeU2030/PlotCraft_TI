from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class HistoricalAutomata(DeterministicFiniteAutomaton):
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
        self.add_transition(self.q0, "historical", self.q1)

        # inicios
        self.add_transition(self.q1, "In the silent hallways of the royal palace, the rumor of a conspiracy that destabilize the city's destiny forever", self.q2)
        self.add_transition(self.q1, "On a dark and ominous night, flames rose over the city's buildings, causing a fire that would consume everything", self.q3)


        # desenlace
        self.add_transition(self.q2, "After a thorough investigation, the brave detectives finally uncovered the conspiracy behind, that shook society in", self.q4)
        self.add_transition(self.q2, "The tragedy of the fire became a tool for political manipulation, with leaders making decisions that would change the fate of", self.q5)

        self.add_transition(self.q3, "Chaos reigned for days as the fire swept through buildings and lives, leaving behind a devastation that seemed impossible in", self.q6)
        self.add_transition(self.q3, "With determination and unity, the city rose from the ashes of the fire, rebuilding its buildings with a rebirth that inspired everyone from", self.q7)


        #finales

        self.add_transition(self.q4, "An informant reveals a plot to overthrow the king, triggering an investigation at the court", self.q8)
        self.add_transition(self.q4, "Although there are suspicions of a conspiracy, no concrete evidence is found, leading to paranoia at the court", self.q8)

        self.add_transition(self.q5, "The plot turns out to be a political maneuver designed to eliminate rivals for the throne", self.q8)
        self.add_transition(self.q5, "Those implicated in the plot are arrested, but it is discovered that they were mere pawns in a larger game", self.q8)

        self.add_transition(self.q6, "The fire ravages a significant portion of the city, causing unprecedented devastation", self.q8)
        self.add_transition(self.q6, "Despite desperate efforts, the fire consumes the city almost entirely", self.q8)

        self.add_transition(self.q7, "After the destruction, the city is rebuilt with a renewed architecture and becomes a symbol of resilience", self.q8)
        self.add_transition(self.q7, "Although the city recovers, the scars of the fire endure in the collective memory of the population", self.q8)
         
        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


