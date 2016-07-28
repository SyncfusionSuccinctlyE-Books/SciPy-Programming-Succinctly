# decomposition.py
# Python 2.7

import numpy as np
import scipy.linalg as spla

def my_decomp(m):
  # LU decompose matrix m using Crout's algorithm
  n = len(m)
  toggle = 1 # row swapping parity
  lum = np.copy(m) # result matrix
  perm = np.arange(n) # row permutation info
    
  for j in xrange(n-1):
    max = abs(lum[j,j])
    piv = j
    
    for i in xrange(j+1, n): # find pivot row
      xij = abs(lum[i,j])    
      if (xij > max):
        max = xij
        piv = i
        
    if (piv != j):
      for k in xrange(n): # swap rows j, piv
        t = lum[piv,k]
        lum[piv,k] = lum[j,k]
        lum[j,k] = t
      
      perm[j], perm[piv] = perm[piv], perm[j]
      toggle = -toggle
      
    xjj = lum[j,j]
    if xjj != 0.0:
      for i in xrange(j+1, n):
        xij = lum[i,j] / xjj
        lum[i,j] = xij
        for k in xrange(j+1, n):
          lum[i,k] = lum[i,k] - (xij * lum[j,k])
          
  return (lum, perm, toggle)

#def get_lower(lum):
#  # strictly lower. 1.0s on diagonal
#  lower = np.copy(lum)
#  n = len(lum)
#  for i in xrange(n):
#    for j in xrange(n):
#      if i == j:
#        lower[i,j] = 1.0
#      elif j > i:
#        lower[i,j] = 0.0
#  return lower

#def get_upper(lum):
#  # includes diag elements of lum
#  upper = np.copy(lum)
#  n = len(lum)
#  for i in xrange(n):
#    for j in xrange(n):
#      if j < i:
#        upper[i,j] = 0.0
#  return upper

# =====

print "\nBegin matrix decomposition demo \n"

m = np.matrix([[3., 2., 1., 3.],
               [5., 6., 4., 2.],
               [7., 9., 8., 1.],
               [4., 2., 3., 0.]])

print "Original matrix m = "
print m

print "\nDecomposing m using scipy.linalg.lu() "
(perm, low, upp) = spla.lu(m)

print "\nResult permutation matrix is "
print perm

print "\nResult lower matrix is "
print low

print "\nResult upper matrix is "
print upp

prod = np.dot(low, upp)
print "\nProduct of lower * upper is "
print prod

print "\n----------"

print "\nDecomposing m using my_decomp() "
(lum, perm, t) = my_decomp(m)

print "\nResult row swap parity (+1 / -1) = " + str(t)

print "\nResult permutation array is "
print perm

print "\nResult combined LU matrix = "
print lum

#lower = get_lower(lum)
#print "\nExtracted lower matrix = "
#print lower

#upper = get_upper(lum)
#print "\nExtracted upper matrix = "
#print upper

#prod = np.dot(lower, upper)
#print "\nProduct of lower * upper ="
#print prod

print "\nEnd demo\n"

