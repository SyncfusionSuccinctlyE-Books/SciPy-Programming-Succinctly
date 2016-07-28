# shuffling.py
# Python 2.7

import numpy as np

def my_shuffle(a, seed):
  # shuffle array a in place using Fisher-Yates algorithm
  np.random.seed(seed)
  n = len(a)
  for i in xrange(n):
    r = np.random.randint(i, n)
    a[r], a[i] = a[i], a[r]
  return

# =====

arr = np.arange(10, dtype=np.int64) # [0, 1, 2, .. 9]
orig = np.copy(arr)
print "Array arr is "
print arr
print ""

np.random.shuffle(arr)
print "Array arr after a call to np.random.shuffle(arr) is "
print arr
print ""

print "Resetting array arr"
arr = np.copy(orig)
print "Array arr is "
print arr
print ""

my_shuffle(arr, seed=0)
print "Array arr after call to my_shuffle(arr, seed=0) is "
print arr
print ""
    
print "\nEnd demo \n"  
  
