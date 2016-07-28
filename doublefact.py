# doublefact.py
# Python 2.7

import scipy.misc as sm

def my_double_fact(n):
  #result = 1
  #stop = 2 # for even n
  #if n % 2 == 0:
  #  stop = 1 # odd n
  #for i in xrange(n, stop-1, -2):
  #  result *= i
  #return result
  result = 1
  for i in xrange(n, 0, -2):
    result *= i
  return result

# =====

print "\nBegin double factorial function demo \n"

n = 3
dfact = sm.factorial2(n)
print "Double factorial of " + str(n) + " using misc.factorial2() = "
print str(dfact)
print ""

n = 4
dfact = sm.factorial2(n)
print "Double factorial of " + str(n) + " using misc.factorial2() = "
print str(dfact)
print ""

n = 4
dfact = my_double_fact(n)
print "Double factorial of " + str(n) + " using my_double_fact() = "
print str(dfact)
print ""

print "\nEnd demo \n"
