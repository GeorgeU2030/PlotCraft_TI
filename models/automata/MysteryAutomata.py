from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class MysteryAutomata(DeterministicFiniteAutomaton):
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
        self.add_transition(self.q0, "mystery", self.q1)

        # inicios
        self.add_transition(self.q1, "I uncover an intriguing enigma that appears to have no explanation, an ancient encrypted letter I found in the main room", self.q2)
        self.add_transition(self.q1, "I discover a new clue that radically changes the direction of the investigation, a fingerprint at the crime scene that doesn't match any known suspect", self.q3)


        # desenlace
        self.add_transition(self.q2, "Upon deciphering the letter, I find a crucial clue leading me to an old diary hidden in the mansion's library, revealing deep secrets in", self.q4)
        self.add_transition(self.q2, "As I delve deeper into the investigation, I confront a mysterious figure in the darkness, an encounter that could change everything in", self.q5)

        self.add_transition(self.q3, "The newly discovered fingerprint leads us to an unknown suspect, a twist that baffles the investigators in", self.q6)
        self.add_transition(self.q3, "The ancient spellbook we find at the crime scene seems to be linked to the mystery, but its contents are incomprehensible in", self.q7)


        #finales

        self.add_transition(self.q4, "The diary's pages unveil dark family secrets previously unknown, bringing me closer to unraveling the mystery", self.q8)
        self.add_transition(self.q4, "The diary only leads to confusion and dead ends, leaving me even more baffled in my quest", self.q8)

        self.add_transition(self.q5, "During the confrontation, I manage to obtain crucial information that brings me closer to solving the mystery", self.q8)
        self.add_transition(self.q5, "The mysterious figure manages to escape, leaving me with no answers and grappling with more questions than before", self.q8)

        self.add_transition(self.q6, "While investigating the new suspect, we unravel a network of shocking secrets that bring us closer to the heart of the mystery", self.q8)
        self.add_transition(self.q6, "The fingerprint leads nowhere and turns out to be false, leaving us once again at a dead end", self.q8)

        self.add_transition(self.q7, "After deciphering the book, we discover a stunning revelation that leads us to the next chapter of the mystery", self.q8)
        self.add_transition(self.q7, "Misuse of the book triggers magical chaos, further complicating the resolution of the mystery", self.q8)
         
        
    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


