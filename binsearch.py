# binsearch.py
# Python 2.7

import numpy as np

def my_bin_search(a, t, eps):
  lo = 0
  hi = len(a)-1
  while lo <= hi:
    mid = (lo + hi) / 2
    if np.isclose(a[mid], t, eps):
      return mid
    elif a[mid] < t:
      lo = mid + 1
    else:
      hi = mid - 1
  return -1

print "\nBegin array binary search demo \n"

arr = np.array([1.0, 3.0, 4.0, 6.0, 8.0, 11.0, 13.0])
print "Array arr is "
print arr
print ""

target = 11.0
# target = 11.0000000000000001 # found by searchsorted()
# target = 11.000000000000001  # not found by searchsorted()

print "Target value to find is " + str(target)
print ""

print "Searching array using np.searchsorted() function "
idx = np.searchsorted(arr, target)
#if idx < len(arr) and arr[idx] == target:
if idx < len(arr) and np.isclose(arr[idx], target, 1.0e-20):
  print "Target found at cell " + str(idx)
else:
  print "Target not found "
print ""

print "Searching array using my_bin_search() function "
idx = my_bin_search(arr, target, 1.0e-5)
if idx == -1:
  print "Target not found "
else:
  print "Target found at cell = " + str(idx)
print ""

print "\nEnd demo \n"
