from pyformlang.fst import FST

class AdventureFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'I', 'q1', ['V']),
            ('q1', 'G', 'q2', ['I']),
            ('q2', 'U', 'q3', ['C']),
            ('q3', 'A', 'q4', ['T']),
            ('q4', 'Z', 'q5', ['O']),
            ('q5', 'U', 'q6', ['R']),
            ('q6', 'epsilon', 'q7', ['I']),
            ('q7', 'epsilon', 'q8', ['A']),
            ('q0', 'V', 'q1', ['I']),
            ('q1', 'I', 'q2', ['G']),
            ('q2', 'C', 'q3', ['U']),
            ('q3', 'T', 'q4', ['A']),
            ('q4', 'O', 'q5', ['Z']),
            ('q5', 'R', 'q6', ['U']),
            ('q6', 'I', 'q7', ['']),
            ('q7', 'A', 'q8', ['']),
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q8')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result