from pyformlang.fst import FST

class RaceFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'C', 'q1', ['N']),
            ('q1', 'H', 'q2', ['I']),
            ('q2', 'E', 'q3', ['S']),
            ('q3', 'V', 'q4', ['S']),
            ('q4', 'R', 'q5', ['A']),
            ('q5', 'O', 'q6', ['N']),
            ('q6', 'L', 'q7', ['']),
            ('q7', 'E', 'q8', ['']),
            ('q8', 'T', 'q9', ['']),
            ('q0', 'N', 'q10', ['T']),
            ('q10', 'I', 'q11', ['O']),
            ('q11', 'S', 'q12', ['Y']),
            ('q12', 'S', 'q13', ['O']),
            ('q13', 'A', 'q14', ['T']),
            ('q14', 'N', 'q9', ['A']),
            ('q0', 'T', 'q15', ['F']),
            ('q15', 'O', 'q16', ['O']),
            ('q16', 'Y', 'q17', ['R']),
            ('q17', 'O', 'q18', ['D']),
            ('q18', 'T', 'q19', ['']),
            ('q19', 'A', 'q9', ['']),
            ('q0', 'F', 'q20', ['C']),
            ('q20', 'O', 'q21', ['H']),
            ('q21', 'R', 'q22', ['E']),
            ('q22', 'D', 'q23', ['V']),
            ('q23', 'epsilon', 'q24', ['R']),
            ('q24', 'epsilon', 'q25', ['O']),
            ('q25', 'epsilon', 'q26', ['L']),
            ('q26', 'epsilon', 'q27', ['E']),
            ('q27', 'epsilon', 'q9', ['T']),
            
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q9')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result