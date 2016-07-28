# inversion.py
# Python 2.7

import numpy as np
import scipy.linalg as spla # alternate inv()

def my_close(m1, m2, eps):
  (rows, cols) = np.shape(m1)
  (rows_m1, cols_m1) = np.shape(m1)
  (rows_m2, cols_m2) = np.shape(m2)
  if rows_m1 != rows_m2 or cols_m1 != cols_m2:
    return None

  for i in xrange(rows):
    for j in xrange(cols):
      if abs(m1[i,j] - m2[i,j]) > eps:
        return False
  return True

# =====

print "\nBegin matrix inversion demo \n"

m = np.matrix([[3, 0, 4],
               [2, 5, 1],
               [0, 4, 5]], dtype=np.float64)

print "Matrix m is"
print m
print ""

mi = np.linalg.inv(m)

print "The inverse of m is"
print mi
print ""

idty = np.eye(3)
print "The 3x3 identity matrix idty is"
print idty
print ""

print "Product of mi * m is"
mim = np.dot(mi, m)
print mim
print ""

b1 = np.allclose(mim, idty)
print "Comparing mi * m with idty using np.allclose() gives"
print str(b1)
print ""

b2 = my_close(mim, idty, 1.0e-4)
print "Comparing mi * m with idty using my_close() gives"
print str(b2)

print "\nEnd demo\n"

