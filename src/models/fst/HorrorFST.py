from pyformlang.fst import FST

class HorrorFST:
    def __init__(self):
        self.fst = FST()
        self.build_fst()

    def build_fst(self):
        self.fst.add_transitions([
            ('q0', 'R', 'q1', ['B']),
            ('q1', 'O', 'q2', ['A']),
            ('q2', 'O', 'q3', ['S']),
            ('q3', 'M', 'q4', ['E']),
            ('q4', 'epsilon', 'q5', ['M']),
            ('q5', 'epsilon', 'q6', ['E']),
            ('q6', 'epsilon', 'q7', ['N']),
            ('q7', 'epsilon', 'q8', ['T']),
            ('q0', 'B', 'q9', ['R']),
            ('q9', 'A', 'q10', ['O']),
            ('q10', 'S', 'q11', ['O']),
            ('q11', 'E', 'q12', ['M']),
            ('q12', 'M', 'q13', ['']),
            ('q13', 'E', 'q14', ['']),
            ('q14', 'N', 'q15', ['']),
            ('q15', 'T', 'q8', ['']),
            ('q0', 'G', 'q16', ['D']),
            ('q16', 'H', 'q17', ['E']),
            ('q17', 'O', 'q18', ['M']),
            ('q18', 'S', 'q19', ['O']),
            ('q19', 'T', 'q8', ['N']),
            ('q0', 'D', 'q20', ['G']),
            ('q20', 'E', 'q21', ['H']),
            ('q21', 'M', 'q22', ['O']),
            ('q22', 'O', 'q23', ['S']),
            ('q23', 'N', 'q8', ['T']),
            ('q0', 'C', 'q24', ['E']),
            ('q24', 'A', 'q25', ['X']),
            ('q25', 'R', 'q26', ['O']),
            ('q26', 'N', 'q27', ['R']),
            ('q27', 'A', 'q28', ['C']),
            ('q28', 'G', 'q29', ['I']),
            ('q29', 'E', 'q30', ['S']),  
            ('q30', 'epsilon', 'q8', ['M']), 
            ('q0', 'E', 'q31', ['C']),
            ('q31', 'X', 'q32', ['A']),
            ('q32', 'O', 'q33', ['R']),
            ('q33', 'R', 'q34', ['N']),
            ('q34', 'C', 'q35', ['A']),
            ('q35', 'I', 'q36', ['G']),
            ('q36', 'S', 'q37', ['E']),  
            ('q37', 'M', 'q8', ['']),   
        ])
        self.fst.add_start_state('q0')
        self.fst.add_final_state('q8')

    def transform(self, input_text):
        result = list(map(lambda x: "".join(x), list(self.fst.translate(input_text))))
        return result