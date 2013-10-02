def base_count(sequence, base):
    # returns the number of times base X occurs
    # in the sequence    
    count=0;
    print 'sequence=',sequence
    for n in range(len(sequence)):
        print 'freq=',sequence.find(base)
        if sequence.find(base) > 0:
            count=count+1
    return count

    
def gc_content(sequence):
    # returns the GC content of the sequence
    return
    
seq='ACGTGTGCAAGTAC'
mybase='A'
base_count=base_count(seq,mybase)
print 'base_count = ',base_count
