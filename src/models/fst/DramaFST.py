from pyformlang.fst import FST

class DramaFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'P', 'q1', ['B']),
            ('q1', 'A', 'q2', ['A']),
            ('q2', 'R', 'q3', ['R']),
            ('q3', 'I', 'q4', ['C']),
            ('q4', 'S', 'q5', ['E']),
            ('q5', 'epsilon', 'q6', ['L']),
            ('q6', 'epsilon', 'q7', ['O']),
            ('q7', 'epsilon', 'q8', ['N']),
            ('q8', 'epsilon', 'q9', ['A']),
            ('q0', 'B', 'q10', ['P']),
            ('q10', 'A', 'q11', ['A']),
            ('q11', 'R', 'q12', ['R']),
            ('q12', 'C', 'q13', ['I']),
            ('q13', 'E', 'q14', ['S']),
            ('q14', 'L', 'q15', ['']),
            ('q15', 'O', 'q16', ['']),
            ('q16', 'N', 'q17', ['']),
            ('q17', 'A', 'q9', ['']), 
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q9')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result