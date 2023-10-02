from pyformlang.fst import FST

class FantasyFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'E', 'q1', ['M']),
            ('q1', 'X', 'q2', ['A']),
            ('q2', 'C', 'q3', ['G']),
            ('q3', 'A', 'q4', ['I']),
            ('q4', 'L', 'q5', ['C']),
            ('q5', 'I', 'q6', ['R']),
            ('q6', 'B', 'q7', ['I']),
            ('q7', 'U', 'q8', ['N']),
            ('q8', 'R', 'q9', ['G']),
            ('q0', 'M', 'q10', ['E']),
            ('q10', 'A', 'q11', ['X']),
            ('q11', 'G', 'q12', ['C']),
            ('q12', 'I', 'q13', ['A']),
            ('q13', 'C', 'q14', ['L']),
            ('q14', 'R', 'q15', ['I']),
            ('q15', 'I', 'q16', ['B']),
            ('q16', 'N', 'q17', ['U']),
            ('q17', 'G', 'q9', ['R']), 
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q9')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result