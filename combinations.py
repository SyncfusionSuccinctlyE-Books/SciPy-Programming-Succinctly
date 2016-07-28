# combinations.py
# Python 2.7

import numpy as np
import itertools as it
import scipy.special as ss

class Combination:
  # n == order, k == subset size
  def __init__(self, n, k):
    self.n = n
    self.k = k
    self.data = np.arange(self.k)

  def as_string(self):
    s = "^ "
    for i in xrange(self.k):
      s = s + str(self.data[i]) + " "
    s = s + "^"
    return s

  @staticmethod
  def my_choose(n, k):
    if n < k: return 0
    if n == k: return 1;
    
    delta = k
    imax = n - k
    if k < n-k:
      delta = n-k
      imax = k

    ans = delta + 1
    for i in xrange(2, imax+1):
      ans = (ans * (delta + i)) / i
    return ans

# =====

print "\nBegin combinations demo \n"

n = 5
k = 3
print "Setting n = " + str(n) + " k = " + str(k)
print ""

num_combs = ss.comb(n, k)
print "n choose k using scipy.comb() is ",
print num_combs
print ""

print "Making all combinations using itertools.combinations() "
all_combs = it.combinations(xrange(n), k)

c = all_combs.next()
print "First itertools combination element is " 
print c
print ""

num_combs = Combination.my_choose(n, k)
print "n choose k using my_choose(n, k) is ",
print num_combs
print ""

print "Making a custom Combination object "
c = Combination(n, k)
print "The first custom combination element is "
print c.as_string()

print "\nEnd demo \n"
