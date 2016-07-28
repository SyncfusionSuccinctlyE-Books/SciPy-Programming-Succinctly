# determinants.py
# Python 2.7

import numpy as np

def extract(m, col):
  # return n-1 x n-1 submatrix w/o row 0 and col 
  n = len(m)
  result = np.zeros((n-1, n-1))
  for i in xrange(1, n):
    k = 0
    for j in xrange(n):
      if j != col:
        result[i-1,k] = m[i,j]
        k += 1
  return result
  
def my_det(m):
  # inefficient and recursive
  n = len(m)
  if n == 1:
    return m[0]
  elif n == 2:
    return (m[0,0] * m[1,1]) - (m[0,1] * m[1,0])
  else:
    sum = 0.0
    for k in xrange(n):
      sign = -1
      if k % 2 == 0:
        sign = +1
      subm = extract(m, k)
      sum = sum + sign * m[0,k] * my_det(subm)
    return sum

# =====

print "\nBegin matrix determinant demo \n"

m = np.matrix([[1., 4., 2., 3.],
               [0., 1., 5., 4.],
               [1., 0., 1., 0.],
               [2., 3., 4., 1.]])

print "Matrix m is "
print m
print ""

d = np.linalg.det(m)
print "Determinant of m using np.linalg.det() is "
print d
print ""

d = my_det(m)
print "Determinant of m using my_det() is "
print d
print ""

print "\nEnd demo \n"

