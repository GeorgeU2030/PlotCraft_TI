from pyformlang.fst import FST

class HistoricalFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'R', 'q1', ['A']),
            ('q1', 'O', 'q2', ['T']),
            ('q2', 'M', 'q3', ['E']),
            ('q3', 'A', 'q4', ['N']),
            ('q4', 'epsilon', 'q5', ['A']),
            ('q5', 'epsilon', 'q6', ['S']),
            ('q0', 'A', 'q7', ['P']),
            ('q7', 'T', 'q8', ['A']),
            ('q8', 'E', 'q9', ['R']),
            ('q9', 'N', 'q10', ['I']),
            ('q10', 'A', 'q11', ['S']),
            ('q11', 'S', 'q6', ['']),
            ('q0', 'p', 'q13', ['R']),
            ('q13', 'A', 'q14', ['O']),
            ('q14', 'R', 'q15', ['M']),
            ('q15', 'I', 'q16', ['A']),
            ('q16', 'S', 'q6', ['']),
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q6')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result