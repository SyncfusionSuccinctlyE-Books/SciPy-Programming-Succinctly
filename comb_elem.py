# comb_elem.py
# Python 2.7

import numpy as np          # to make custom Combination class
import itertools as it      # has combinations iterator
import scipy.special as ss  # has comb() aka choose() function
import time                 # to time performance

class Combination:
  def __init__(self, n, k):
    self.n = n
    self.k = k
    self.data = np.arange(k)

  def as_string(self):
    s = "^ "
    for i in xrange(self.k):
      s = s + str(self.data[i]) + " "
    s = s + "^"
    return s

  @staticmethod
  def my_choose(n,k):
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

  def element(self, idx):
    maxM = Combination.my_choose(self.n, self.k) - 1

    ans = np.zeros(self.k, dtype=np.int64)
    a = self.n
    b = self.k
    x = maxM - idx
    for i in xrange(self.k):
      ans[i] = self.my_largestV(a, b, x)
      x = x - Combination.my_choose(ans[i], b)
      a = ans[i]
      b -= 1

    for i in xrange(self.k):
      ans[i] = (self.n - 1) - ans[i]

    result = Combination(self.n, self.k)
    for i in xrange(self.k):
      result.data[i] = ans[i]
    return result

  def my_largestV(self, a, b, x):
    v = a - 1
    while Combination.my_choose(v, b) > x:
      v -= 1
    return v

# =====

def comb_element(n, k, idx):
  comb_it = it.combinations(xrange(n), k)
  i = 0
  for c in comb_it:
    if i == idx:
      return c
      break
    i += 1
  return None

# =====

print "\nBegin combination element demo \n"

n = 100
k = 8
print "Setting n = " + str(n) + " k = " + str(k)
ces = ss.comb(n, k)
print "There are " + str(ces) + " different combinations \n"

idx = 100000000

print "Element " + str(idx) + " using itertools.combinations() is "
start_time = time.clock()
ce = comb_element(n, k, idx)
end_time = time.clock()
elapsed_time = end_time - start_time
print ce 
print "Elapsed time = " + str(elapsed_time) + " seconds "
print ""

c = Combination(n, k)
start_time = time.clock()
ce = c.element(idx)
end_time = time.clock()
elapsed_time = end_time - start_time
print "Element " + str(idx) + " using custom Combination class is "
print ce.as_string()
print "Elapsed time = " + str(elapsed_time) + " seconds "
print ""

print "\nEnd demo \n"
