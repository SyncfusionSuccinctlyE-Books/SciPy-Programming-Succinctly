# permutations.py
# Python 2.7

import numpy as np
import itertools as it
import scipy.special as ss

class Permutation:
  def __init__(self, n):
    self.n = n
    self.data = np.arange(n)

  @staticmethod
  def my_fact(n):
    ans = 1
    for i in xrange(1, n+1):
      ans *= i
    return ans

  @staticmethod
  def my_fact_rec(n):
    if n == 0 or n == 1:
      return 1
    else:
      return n * Permutation.my_fact_rec(n-1)

  def as_string(self):
    s = "# "
    for i in xrange(self.n):
      s = s + str(self.data[i]) + " "
    s = s + "#"
    return s

# =====

print "\nBegin permutation demo \n"

n = 3
print "Setting n = " + str(n)
print ""

num_perms = ss.factorial(n)
print "Using scipy.special.factorial(n) there are ",
print str(num_perms),
print "possible permutation elements"
print ""

print "Making all permutations using itertools.permutations()"
all_perms = it.permutations(xrange(n))
p = all_perms.next()

print "The first itertools permutation is "
print p
print ""

num_perms = Permutation.my_fact_rec(n)
print "Using my_fact(n) there are " + str(num_perms),
print "possible permutation elements"
print ""

print "Making a custom Permutation object "
p = Permutation(n)
print "The first custom permutation element is "
print p.as_string()

print "\nEnd demo \n"
