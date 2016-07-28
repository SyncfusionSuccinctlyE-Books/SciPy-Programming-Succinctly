# ch3_intro.py
# Python 2.7

import numpy as np

print '\nBegin "Chapter 3 - Matrices" demo \n'

print "Creating 2x3 matrix m using matrix() "
m = np.matrix([[1.1, 2.2, 3.3],[4.4, 5.5, 6.6]])
print "Matrix m is "
print m
print ""

# file data.txt is
# 5.5,2.2,6.6
# 4.4,3.3,8.8
# 1.1,7.7,9.9

print "Loading 3x3 matrix x from data file using loadtxt() "
x = np.loadtxt(r"C:\NumPy\Ch3\data.txt", delimiter=',')
print "Matrix x is "
print x
print ""

print "Multiplying m * x using dot() "
mx = np.dot(m, x)
print "Result matrix mx is "
print mx
print ""

print "Generating the transpose of matrix m using transpose() "
mt = np.transpose(m)
print "Result matrix mt is "
print mt
print ""

print "Finding the determinant of matrix x using linalg.det() "
d = np.linalg.det(x)
print "The determinant is " + str(d)
print ""

print "Finding the inverse of matrix x using linalg.inv() "
xi = np.linalg.inv(x)
print "Result matrix xi is "
print xi
print ""

print "\nEnd demo \n"
