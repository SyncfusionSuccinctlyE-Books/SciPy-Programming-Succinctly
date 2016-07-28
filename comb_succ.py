# comb_succ.py
# Python 2.7

import numpy as np
import itertools as it

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

  def successor(self):
    if self.data[0] == self.n - self.k:
      return None
    
    res = Combination(self.n, self.k)
    for i in xrange(self.k):
      res.data[i] = self.data[i]

    i = self.k - 1
    while i > 0 and res.data[i] == self.n - self.k + i:
      i -= 1

    res.data[i] += 1

    for j in xrange(i, self.k - 1):
      res.data[j+1] = res.data[j] + 1

    return res

# =====

print "\nBegin combination successor demo \n"

n = 5
k = 3
print "Setting n = " + str(n) + " k = " + str(k)
print ""

print "Iterating through all elements using itertools.combinations()"
comb_iter = it.combinations(xrange(n), k)
for c in comb_iter:
  print "c = " + str(c)
print ""

print "Iterating through all elements using custom Combination class"
c = Combination(n, k)
while c is not None:
  print "c = " + c.as_string()
  c = c.successor()
print ""

print "\nEnd demo \n"
