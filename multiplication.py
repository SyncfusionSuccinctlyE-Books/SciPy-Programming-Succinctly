# multiplication.py
# Python 2.7

import numpy as np

def my_mult(a, b):
  (arows, acols) = np.shape(a)
  (brows, bcols) = np.shape(b)
  result = np.zeros((arows, bcols))
  for i in xrange(arows):
    for j in xrange(bcols):
      for k in xrange(acols):
        result[i,j] = result[i,j] + a[i,k] * b[k,j]
  return result

# =====

print "\nBegin matrix multiplication demo \n"

A = np.matrix([[1.0, 2.0, 3.0],
               [4.0, 5.0, 6.0]])

B = np.matrix([[7.0, 8.0],
               [9.0, 10.0],
               [11.0, 12.0]])

C = np.dot(A, B) # NumPy matrix multiplication

D = my_mult(A, B) # slower Python 

print "Matrix A = "
print A
print ""

print "Matrix B = "
print B
print ""

print "Result of dot(A,B) = "
print C
print ""

print "Result of my_mult(A,B) = "
print D
print ""

print "End demo \n"
