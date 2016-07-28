# structure.py
# Python 2.7

import numpy as np

def make_x(n):
  result = np.zeros((n,n))
  for i in xrange(n):
    for j in xrange(n):
      if i == j or (i + j == n-1):
        result[i,j] = 1.0
  return result

def main():
  print "\nBegin program structure demo \n"

  try:
    n = 5
    print "X matrix with size n = " + str(n) + " is "
    mx = make_x(n)
    print mx
    print ""

    n = -1
    print "X matrix with size n = " + str(n) + " is "
    mx = make_x(n)
    print mx
    print ""
  except Exception, e:
    print "Error: " + str(e)

  print "\nEnd demo \n"

if __name__ == "__main__":
  main()
