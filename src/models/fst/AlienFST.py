from pyformlang.fst import FST

class AlienFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'U', 'q1', ['C']),
            ('q1', 'S', 'q2', ['H']),
            ('q2', 'A', 'q3', ['I']),
            ('q3', 'epsilon', 'q4', ['N']),
            ('q4', 'epsilon', 'q5', ['A']),
            ('q0', 'C', 'q6', ['F']),
            ('q6', 'H', 'q7', ['R']),
            ('q7', 'I', 'q8', ['A']),
            ('q8', 'N', 'q9', ['N']),
            ('q9', 'A', 'q10', ['C']),
            ('q10', 'epsilon', 'q5', ['E']),
            ('q0', 'F', 'q12', ['E']),
            ('q12', 'R', 'q13', ['N']),
            ('q13', 'A', 'q14', ['G']),
            ('q14', 'N', 'q15', ['L']),
            ('q15', 'C', 'q16', ['A']),
            ('q16', 'E', 'q17', ['N']),
            ('q17', 'epsilon', 'q5', ['D']),
            ('q0', 'E', 'q18', ['U']),
            ('q18', 'N', 'q19', ['S']),
            ('q19', 'G', 'q20', ['A']),
            ('q20', 'L', 'q21', ['']),
            ('q21', 'A', 'q22', ['']),
            ('q22', 'N', 'q23', ['']),
            ('q23', 'D', 'q5', ['']),
            
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q5')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result