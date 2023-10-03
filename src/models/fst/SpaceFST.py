from pyformlang.fst import FST

class SpaceFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'M', 'q1', ['V']),
            ('q1', 'A', 'q2', ['E']),
            ('q2', 'R', 'q3', ['N']),
            ('q3', 'T', 'q4', ['U']),
            ('q4', 'E', 'q5', ['S']),
            ('q0', 'V', 'q6', ['U']),
            ('q6', 'E', 'q7', ['R']),
            ('q7', 'N', 'q8', ['A']),
            ('q8', 'U', 'q9', ['N']),
            ('q9', 'S', 'q5', ['O']),
            ('q0', 'U', 'q10', ['J']),
            ('q10', 'R', 'q11', ['U']),
            ('q11', 'A', 'q12', ['P']),
            ('q12', 'N', 'q13', ['I']),
            ('q13', 'O', 'q14', ['T']),
            ('q14', 'epsilon', 'q15', ['E']),
            ('q15', 'epsilon', 'q5', ['R']),
            ('q0', 'J', 'q16', ['M']),
            ('q16', 'U', 'q17', ['A']),
            ('q17', 'P', 'q18', ['R']),
            ('q18', 'I', 'q19', ['T']),
            ('q19', 'T', 'q20', ['E']),
            ('q20', 'E', 'q21', ['']),
            ('q21', 'R', 'q5', ['']),  
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q5')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result