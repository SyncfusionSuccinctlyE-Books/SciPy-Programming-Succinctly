# distributions.py
# Python 2.7

import numpy as np
import math          # for custom Gaussian class
import random        # for custom Gaussian class
# import matplotlib.pyplot as plt

class Gaussian:
  # generate using Box-Muller algorithm
  def __init__(self, mean, sd, seed):
    self.mean = mean
    self.sd = sd
    self.rnd = random.Random(seed)

  def next(self):
    two_pi = 2.0*3.14159265358979323846
    u1 = self.rnd.random()  # [0.0 to 1.0)
    while u1 < 1.0e-10:
      u1 = self.rnd.random()
    u2 = self.rnd.random()
    z = math.sqrt(-2.0 * math.log(u1)) * math.cos(two_pi * u2)
    return z * self.sd + self.mean
  
# =====

print "\nBegin distributions demo \n"

np.random.seed(0)
mean = 0.0
std = 1.0
n = 100

print "Setting mean = " + str(mean)
print "Setting std  = " + str(std)
print ""

print "Generating " + str(n) + " Normal values "
values = np.zeros(n)
for i in xrange(n):
  x = np.random.normal(mean, std)
  values[i] = x

print "Normally distributed random values are: "
print values
print ""

bins = 5
print "Constructing histogram data using " + str(bins) + " bins "
(histo, edges) = np.histogram(values, bins=5)

print "Count of values in each bin: "
print histo
print ""

print "The beginning and end values of each bin: "
print edges
print ""

print "Generating 5 values using custom Gaussian class: " 
g = Gaussian(0.0, 1.0, 0)
for i in xrange(5):
  x = g.next()
  print "%1.5f" % x,
print ""

print "\nEnd demo \n"

#plt.hist(values, bins=9)
#plt.show()

