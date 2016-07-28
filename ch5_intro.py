# ch5_intro.py
# Python 2.7

import numpy as np
import scipy.linalg as spla
import scipy.misc as sm
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

print '\nBegin "Chapter 5 - Miscellaneous Topics" demo \n'

arr = np.array([3.0, 5.0, 7.0, 8.0, 10.0, 12.0, 15.0])
print "Sorted array arr is "
print arr
print ""

target = 7.0
print "Searching array for " + str(target) + " using np.searchsorted() function "
idx = np.searchsorted(arr, target)
print "Return result = " + str(idx)
print ""

m = np.matrix([[2., 4., 3., 5.],
               [7., 2., 8., 9.],
               [1., 0., 3., 1.],
               [3., 6., 2., 4.]])
print "Matrix m is "
print m
print ""

print "Performing LU decomposition on m using scipy.linalg.lu() "
(perm, low, upp) = spla.lu(m)
print ""

print "Result lower decomposed matrix is "
print low
print ""

arr = np.array([2.2, 5.5, 1.1, 4.4, 3.3])
med = np.median(arr)
print "Median of " + str(arr) + " using np.median() is " + str(med)
print ""

print "Making 100 Normal values with mean = 5.0 and sd = 1.0 using normal() "
# set seed here if you want to get reproducible results
np.random.seed(0)
values = np.random.normal(5.0, 1.0, 100)
print "Constructing array of counts with 3 bins using np.histogram() "
(histo, edges) = np.histogram(values, bins=3)
print "The counts are: "
print histo
print ""

n = 5
d_fact = sm.factorial2(n)
print "Double factorial of " + str(n) + " using misc.factorial2() = " + str(d_fact)
print ""

n = 9
s_gamma = my_special_gamma(9)
print "Gamma of " + str(n/2.0) + " using my_special_gamma() = " + str(s_gamma)
print ""


print "\nEnd demo \n"
