# ch2_intro.py
# Python 2.7

import numpy as np

print '\nBegin "Chapter 2 - Arrays" demo \n'

print "Creating NumPy array aa using array() "
aa = np.array([3.3, 5.5, 2.2, 1.1, 4.4])
print "Array aa is "
print aa
print ""

print "Determining array aa cell type "
dt = np.dtype(aa[0])
print "Cell type is "
print dt.name
print ""

print "Creating NumPy array zz using zeros() "
zz = np.zeros(5)
print "Array zz is "
print zz
print ""

print "Creating array ii using arange() "
ii = np.arange(7)
print "Array ii is "
print ii
print ""

print "Searching array aa for target value 1.1 using where() "
result = np.where(aa == 1.1)
print "Return result is "
print result
print ""

print "Sorting array aa into array ss using sort() "
ss = np.sort(aa, kind='quicksort')
print "Sorted array ss is "
print ss
print ""

print "Randomizing array ss in-place using shuffle() "
np.random.seed(99)
np.random.shuffle(ss)
print "Array ss is "
print ss
print ""

print "\nEnd demo \n"
