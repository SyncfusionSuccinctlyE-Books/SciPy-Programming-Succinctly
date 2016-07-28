# searching.py
# Python 2.7

import numpy as np

def my_search(a, x, eps):
  for i in xrange(len(a)):
    if np.isclose(a[i], x, eps):
      return i
  return -1

# =====

print "\nBegin array search demo \n"

arr = np.array([7.0, 9.0, 5.0, 1.0, 5.0, 8.0])

print "Array arr is "
print arr
print ""

target = 5.0
print "Target value is "
print target
print ""

found = target in arr
print "Search result using 'target in arr' syntax = " + str(found)
print ""

result = np.where(arr == target)
print "Search result using np.where(arr == target) is "
print result
print ""

idx = my_search(arr, target, 1.0e-6)
print "Search result using my_search() = "
print idx
print ""

print "\nEnd demo \n"
