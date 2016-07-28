# quick_ref.py                            # SciPy Programming Succinctly 
# Python 2.7

import numpy as np                        # arrays, matrices, functions
import scipy.linalg as spla               # determinant, inverse, etc.
import scipy.special as ss                # advanced functions like gamma
import scipy.constants as sc              # math constants like e
import scipy.integrate as si              # functions for integration
import scipy.optimize as so               # functions for optimization
import itertools as it                    # permutations, combinations
import time                               # for timing

class Permutation:                        # custom class using an array
  def __init__(self, n):                  # constructor
    self.n = n
    self.data = np.arange(n)              # [0, 1, 2, . . (n-1)]

  def as_string(self):                    # instance method
    s = "# "
    for i in xrange(self.n):              # traverse an array            
      s += str(self.data[i]) + " "
    return s + "#"

  @staticmethod
  def my_fact(n):                         # static method
    result = 1                            # iterative rather than recursive
    for i in xrange(1, n+1):              # recursion supported in Python
      result *= i                         #  but usually not a good idea
    return result 

# ----------------------------------
def show_matrix(m, decimals):             # standalone function
  (rows, cols) = np.shape(m)              # matrix dimensions as tuple
  for i in rows:                          # traverse a matrix
    for j in cols:
      print "%." + str(dec) % m[i,j]
    print ""
# ----------------------------------

print "\nBegin quick examples \n"

arr_a = np.array([3.0, 2.0, 0.0, 1.0])    # create array of float64
arr_b = np.zeros(4, dtype=np.int32)       # create int array [0, 0, 0, 0]
b = 1.0 in arr_a                          # search array using "in": True
result = np.where(arr_a == 1.0)           # result is (array([3]),)
arr_s = np.sort(arr_a, kind="quicksort")  # sort array: [0.0, 1.0, 2.0, 3.0]
arr_r = arr_s[::-1]                       # reverse: [3.0, 2.0, 1.0, 0.0]

np.random.seed(0)                         # set seed for reproducibility
np.random.shuffle(arr_r)                  # randomize content order

arr_ref = arr_a                           # copy array by reference
arr_d = np.copy(arr_a)                    # copy array by value
arr_v = arr_a.view()                      # copy by view reference
arr_e = arr_a + arr_b                     # add arrays

m_a = np.matrix([[1.0, 2.0], [3.0, 4.0]]) # matrix-style 2x2 matrix
m_b = np.array([[8, 7], [6, 5]])          # ndarray-style 2x2 matrix
m_c = np.zeros((2,2), dtype=np.int32)     # ndarray 2x2 matrix all 0s
try:                                      # try-except
  m = np.loadtxt("foo.txt")               # matrix from file
except Exception:
  print "Unable to open file"

m_e = m_a.transpose()                     # matrix transposition
d = spla.det(m_a)                         # matrix determinant
m_i = np.linalg.inv(m_a)                  # matrix inverse

m_idty = np.eye(2)                        # identity 2x2 matrix
m_m = np.dot(m_a, m_i)                    # matrix multiplication
b = np.allclose(m_m, m_idty, 1.0e-5)      # matrix equality by value

m_x = m_a + np.array([5.0, 8.0])          # broadcasting
 
p_it = it.permutations(xrange(3))         # permutations iterator
start_t = time.clock()                    # timing
for p in p_it:
  print p
end_t = time.clock()
elap = end_t - start_t
print "elapsed = " + str(elap) + "secs"   # string concatenation
  
pc = Permutation(3)                       # instantiate a custom class
print pc.as_string()                      # instance method call
nf = Permutation.my_fact(3)               # static method call

arr = np.array([1.0, 3.0, 5.0, 7.0])      # a sorted array
ii = np.searchsorted(arr, 2.0)            # binary search
if ii < len(arr_s) and arr_s[ii] == 2.0:  # somewhat tricky return
  print "2.0 found"

(perm, low, upp) = spla.lu(m_a)           # matrix LU decomposition
med = np.median(arr_a)                    # statistics function
rv = np.random.normal(0.0, 1.0)           # random variable generation
g = ss.gamma(3.5)                         # advanced math function

print "\nEnd quick reference \n"
