# perm_succ.py
# Python 2.7

import numpy as np
import itertools as it

class Permutation:
  def __init__(self, n):
    self.n = n
    self.data = np.arange(n)

  def as_string(self):
    s = "# "
    for i in xrange(self.n):
      s = s + str(self.data[i]) + " "
    s = s + "#"
    return s

  def successor(self):
    res = Permutation(self.n) # result
    res.data = np.copy(self.data)

    left = self.n - 2
    while res.data[left] > res.data[left+1] and left >= 1:
      left -= 1

    if left == 0 and res.data[left] > res.data[left+1]:
      return None

    right = self.n - 1
    while res.data[left] > res.data[right]:
      right -= 1

    res.data[left], res.data[right] = \
                     res.data[right], res.data[left]

    i = left + 1
    j = self.n - 1
    while i < j:
      tmp = res.data[i]
      res.data[i] = res.data[j]
      res.data[j] = tmp
      i += 1; j -= 1
    return res

# =====

print "\nBegin permutation successor demo \n"

n = 3
print "Setting n = " + str(n)
print ""

perm_it = it.permutations(xrange(n))
print "Iterating all permutations using itertools permutations(): "

for p in perm_it:
  print "p = " + str(p)
print ""

p = Permutation(n)
print "Iterating all permutations using custom Permutation class: "
while p is not None:
  print "p = " + p.as_string()
  p = p.successor()

print "\nEnd demo \n"

                  
