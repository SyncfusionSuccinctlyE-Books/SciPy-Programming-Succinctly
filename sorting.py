# sorting.py
# Python 2.7

import numpy as np
import time

def my_qsort(a):
  quick_sorter(a, 0, len(a)-1)

def quick_sorter(a, lo, hi):
  if lo < hi:
    p = partition(a, lo, hi)
    quick_sorter(a, lo, p-1)
    quick_sorter(a, p+1, hi)

def partition(a, lo, hi):
  piv = a[hi]
  i = lo
  for j in xrange(lo, hi):
    if a[j] <= piv:
      a[i], a[j] = a[j], a[i]
      i += 1
  a[i], a[hi] = a[hi], a[i]
  return i

# =====

print "\nBegin array sorting demo \n"

arr = np.array([4.0, 3.0, 0.0, 2.0, 1.0, 9.0, 7.0, 6.0, 5.0])
print "Original array is "
print arr
print ""

s_arr = np.sort(arr, kind='quicksort')
print "Return result of sorting using np.sort(arr, 'quicksort') is "
print s_arr
print ""
print "Original array after calling np.sort() is "
print arr
print ""

print "Calling my_qsort(arr) "
start_time = time.clock() # record starting time
my_qsort(arr)
end_time = time.clock()
elapsed_time = end_time - start_time

print "Elapsed time = "
print str(elapsed_time) + " seconds"
print ""

print "Original array after calling my_qsort(arr) is "
print arr
print ""

print "\nEnd demo \n"
