from pyformlang.fst import FST

class MysteryFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'M', 'q1', ['H']),
            ('q1', 'A', 'q2', ['O']),
            ('q2', 'N', 'q3', ['S']),
            ('q3', 'S', 'q4', ['P']),
            ('q4', 'I', 'q5', ['I']),
            ('q5', 'O', 'q6', ['T']),
            ('q6', 'N', 'q7', ['A']),
            ('q7', 'epsilon', 'q8', ['L']),
            ('q0', 'H', 'q9', ['S']),
            ('q9', 'O', 'q10', ['T']),
            ('q10', 'S', 'q11', ['A']),
            ('q11', 'P', 'q12', ['T']),
            ('q12', 'I', 'q13', ['I']),
            ('q13', 'T', 'q14', ['O']),
            ('q14', 'A', 'q15', ['N']),
            ('q15', 'L', 'q8', ['']),
            ('q0', 'S', 'q16', ['H']),
            ('q16', 'T', 'q17', ['O']),
            ('q17', 'A', 'q18', ['T']),
            ('q18', 'T', 'q19', ['E']),
            ('q19', 'I', 'q20', ['L']),
            ('q20', 'O', 'q21', ['']),
            ('q21', 'N', 'q8', ['']),
            ('q0', 'H', 'q22', ['M']),
            ('q22', 'O', 'q23', ['A']),
            ('q23', 'T', 'q24', ['N']),
            ('q24', 'E', 'q25', ['S']),
            ('q25', 'L', 'q26', ['I']),
            ('q26', 'epsilon', 'q27', ['O']),
            ('q27', 'epsilon', 'q8', ['N']),  
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q8')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result