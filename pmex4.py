human='OS=Homo sapiens'
line_count=0
human_line_count=0
f=open('uniprot_sprot.fasta')
#while (f.readline()):
line=f.readline()
line_count+=1
#  if line.find(human):
  if human in line:
    human_line_count+=1
#    if line_count < 300:
#      print line
print 'line_count = ',line_count
print 'human_line_count = ',human_line_count
f.close()

