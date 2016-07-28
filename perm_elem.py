# perm_elem.py
# Python 2.7

import numpy as np
import itertools as it
import time

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

  def element(self, idx):
    # if idx >= Permutation.my_fact(self.n):
    #   return None

    result = Permutation(self.n)
    
    factoradic = np.zeros(self.n)
    for j in xrange(1, self.n + 1):
      factoradic[self.n-j] = idx % j
      idx = idx / j

    for i in xrange(self.n):
      factoradic[i] += 1

    result.data[self.n - 1] = 1

    for i in xrange(self.n - 2, -1, -1):
      result.data[i] = factoradic[i]
      for j in xrange(i + 1, self.n):  
        if result.data[j] >= result.data[i]:
          result.data[j] += 1

    for i in xrange(self.n):
      result.data[i] -= 1

    return result;

# =====

def perm_element(n, idx):
  p_it = it.permutations(xrange(n))
  i = 0
  for p in p_it:
    if i == idx:
      return p
      break
    i += 1

# =====

print "\nBegin permutation element demo \n"

n = 20 # 20! = 2,432,902,008,176,640,000
print "Setting n = " + str(n) + "\n"
idx = 1000000000 # not even close to last element

print "Element " + str(idx) + " using itertools.permutations() is "
start_time = time.clock()
pe = perm_element(n, idx)
end_time = time.clock()
elapsed_time = end_time - start_time
print pe 
print "Elapsed time = " + str(elapsed_time) + " seconds "
print ""

p = Permutation(n)
start_time = time.clock()
pe = p.element(idx)
end_time = time.clock()
elapsed_time = end_time - start_time
print "Element " + str(idx) + " using custom Permutation class is "
print pe.as_string()
print "Elapsed time = " + str(elapsed_time) + " seconds "
print ""

print "\nEnd demo \n"
