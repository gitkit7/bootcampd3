class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def base_count(self, base):
        return self.sequence.count(base)
    
    def gc_content(self):
        g=self.base_count('G')
        c=self.base_count('C')
        return float(g+c)/len(self.sequence)

        
    # extra credit
    def reverse_complement(self):
        # reverse the sequence,
        # then change G<->C, A<->T
        comlements = {'G':'C',
                      'C:'G',
                      'A':'T',
                      'T':'A'}
        rev_c=""
        rev_c = complements[base] + rev_c
        
