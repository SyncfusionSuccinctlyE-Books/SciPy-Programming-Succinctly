# transposition.py
# Python 2.7

import numpy as np

def my_transpose(m):
  (rows, cols) = np.shape(m)
  result = np.zeros((rows, cols))
  for i in xrange(rows):
    for j in xrange(cols):
      result[j,i] = m[i,j]
  return result

# =====

print "\nBegin matrix transposition demo \n"

m = np.matrix([[1., 2., 3.],
               [4., 5., 6.],
               [7., 8., 9.]])

print "Matrix m = "
print m
print ""

mt = m.transpose()
print "Transpose from m.transpose() function = "
print mt
print ""

mt = np.transpose(m)
print "Transpose from np.transpose(m) function = "
print mt
print ""

mt = m.T
print "Transpose from m.T property  = "
print mt
print ""

mt = my_transpose(m)
print "Transpose from my_transpose() function = "
print mt
print ""

print "\nEnd demo \n"
