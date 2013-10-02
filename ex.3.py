#exercise 3
#take a list of 3 words off command line
#print words sepaerated by commas
#final word preceded by and
#in sorted order
#Capitalize the first letter of first word

import sys
words = sys.argv[1:]
# step 2: sort the list
words.sort()
# step 3: get the last word
last_word = words[-1]
# step 4: make a new list without the last word
all_but_last_word = words[:-1]
# step 5: join the sentence together using commas
sentence = ', '.join(all_but_last_word)
# step 6: add "and" and the final word
sentence += ', and ' + last_word + '.'
# step 7: output the result
sentence = sentence[0].upper() + sentence[1:]
print sentence

