#
seq="GGTAAGTAAGGCCGTTCCCCC"
valid_bases="GATC"
a=seq.count('A')
c=seq.count('C')
g=seq.count('G')
t=seq.count('T')

base_counts={'G':g,'A':a,'T':t,'C':c}
print "Base counts = " + str(base_counts)

total_length=g+a+t+c
print "Total Length = " + str(total_length)
gc_content=(g+c)/float(total_length) * 100

print "GC Content = " + str(gc_content) + "%"

#print "%S%%" gc_content

