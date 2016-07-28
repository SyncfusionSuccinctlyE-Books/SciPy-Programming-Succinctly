# matrices.py
# Python 2.7

import numpy as np

def show_matrix(m, dec, wid):
  fmt = "%" + str(wid) + "." + str(dec) + "f"
  (rows, cols) = np.shape(m)
  for i in xrange(rows):
    for j in xrange(cols):
      print fmt % m[i,j],
    print ""  # end of row
  print "" # final newline

# =====

print "\nBegin matrices demo \n"

ma = np.matrix([[1.0, 2.0, 3.0], # 2x3
               [4.0, 5.0, 6.0]])

mb = np.zeros((3, 2), dtype=np.int32) # 3x2

mc = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]) # 2x3

md = np.matrix([[7.0, 8.0, 9.0]]) # 1x3

print "Matrix ma is "
print ma
print ""

print "Matrix mb is "
print mb
print ""

print "N-dimensional array/matrix mc is "
print mc
print ""

print "ma is type " + str(type(ma))
print "mb is type " + str(type(mb))
print "mc is type " + str(type(mc))
print ""

print "Contents of matrix ma using show_matrix(ma, 3, 6) are "
show_matrix(ma, 3, 6)

msum = ma + mc
print "Result of ma + mc = "
print msum
print ""

md = np.matrix([[7.0, 8.0, 9.0]])
mx = ma + md
print "Matrix md is "
print md
print ""
print "Result of ma + md is "
print mx

print "\nEnd demo \n"

