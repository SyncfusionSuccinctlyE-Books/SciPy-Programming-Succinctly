# loadingdata.py
# Python 2.7

import numpy as np

def my_load(fn, sep):
  f = open(fn, "r")

  rows = 0; cols = 0
  for line in f:
    rows += 1
    cols = len(line.strip().split(sep))
  
  result = np.zeros((rows,cols)) # make matrix

  f.seek(0) # back to start of file

  i = 0 # row index
  while True:
    line = f.readline()
    if not line: break
    line = line.strip()
    tokens = line.split(',') # a list
    for j in xrange(cols):
      result[i,j] = np.float64(tokens[j])
    i += 1
  
  f.close()
  return result

# =====

print "\nBegin matrix load demo \n"

fn = r"C:\NumPy\Ch3\datafile.txt"

m = np.loadtxt(fn, delimiter=',')
                                            
print "Matrix loaded using np.loadtxt() = "
print m
print ""

m = my_load(fn, sep=',')
print "Matrix loaded using my_load() = "
print m
print ""

print "\nEnd demo\n"
