#pm ex 2
import sys
x=(int)(sys.argv[1])
if x < 50 and x > 0 :
    print "x is minor"
elif x >= 50 and x < 1000:
    print "major"
else:
    print "severe"
