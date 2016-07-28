# gamma.py
# Python 2.7

import scipy.special as ss
import math

def my_special_gamma(n):
  # return gamma(n/2)
  if n % 2 == 0: # n/2 is an integer
    return math.factorial(n / 2 - 1)
  else:
    root_pi = math.sqrt(math.pi)
    return root_pi * ss.factorial2(n-2) / math.pow(2.0, (n-1) / 2.0)

# =====

print "\nBegin gamma function demo \n"

n = 3
n_fact = math.factorial(n)
print "Factorial of " + str(n) + " = " + str(n_fact)

n = 4
n_fact = math.factorial(n)
print "Factorial of " + str(n) + " = " + str(n_fact)
print ""

n = 5
n_gamma = ss.gamma(n)
print "Gamma of " + str(n) + " using special.gamma() = "
print str(n_gamma)
print ""

n = 4.5
n_gamma = ss.gamma(n)
print "Gamma of " + str(n) + " using special.gamma() = "
print str(n_gamma)
print ""

n = 9
s_gamma = my_special_gamma(n)
print "Gamma of " + str(n) + "/2 using my_special_gamma() = "
print str(s_gamma)
print ""

print "\nEnd demo \n"
