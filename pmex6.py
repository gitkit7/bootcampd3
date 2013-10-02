import sys
def fibonnacci2(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

def fibonacci(n):
  k=1
  i=1
  j=1
  while k < n:
    print i
    print j
    i=i+j
    j=i+j
    k=k+1
  return "done"

num=(int)(sys.argv[1])
print 'num = ',num
print 'Fibonanci series for ',num
fibonacci(num)



for g in range(5):
    fibonnacci2(g)
    
