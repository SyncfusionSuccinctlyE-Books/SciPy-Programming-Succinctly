# ch4_intro.py
# Python 2.7

import numpy as np

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

    res.data[left], res.data[right] = res.data[right], res.data[left]

    i = left + 1
    j = self.n - 1
    while i < j:
      tmp = res.data[i]
      res.data[i] = res.data[j]
      res.data[j] = tmp
      i += 1; j -= 1
    return res

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

print '\nBegin "Chapter 4 - Combinatorics" demo \n'

n = 3
p = Permutation(n)
print "Creating program-defined Permutation object with n = " + str(n)
print ""

num_perms = p.my_fact(n)
print "Total number of permutations using my_factorial() = " + str(num_perms)
print ""

print "Generating all permutation elements using successor(): "
while p is not None:
  print "p = " + p.as_string()
  p = p.successor()
print ""

print "Permutation element [3] computed directly using element() is "
pe = Permutation(n).element(3).as_string()
print pe
print ""

n = 5; k = 3
c = Combination(n, k)
print "Creating program-defined Combination object with n = " + str(n),
print "and k = " + str(k)
print ""

num_combs = c.my_choose(n, k)
print "Total number of combinations using my_choose() = " + str(num_combs)
print ""

print "Generating all combination elements using successor(): "
while c is not None:
  print "c = " + c.as_string()
  c = c.successor()
print ""

print "Combination element [5] computed directly using element() is "
ce = Combination(n, k).element(5).as_string()
print ce
print ""

print "\nEnd demo \n"
