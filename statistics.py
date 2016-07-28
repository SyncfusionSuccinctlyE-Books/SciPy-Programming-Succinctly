# statistics.py
# Python 2.7

import numpy as np
import math

def my_corr(x, y):
  n = len(x)
  mx = np.mean(x)
  my = np.mean(y)
  
  num = 0.0
  for i in xrange(n):
    num += (x[i] - mx) * (y[i] - my)
  ssx = 0.0
  ssy = 0.0
  for i in xrange(n):
    ssx += math.pow(x[i] - mx, 2)
    ssy += math.pow(y[i] - my, 2)
  
  denom = math.sqrt(ssx) * math.sqrt(ssy)
  return num / denom
  
# =====

print "\nBegin statistics demo \n"

ability = np.array([0., 1., 3., 4., 4., 6.])
payrate = np.array([15., 15., 25., 20., 30., 33. ])

print "ability array = "
print ability
print ""

print "payrate array = "
print payrate
print ""

ma = np.median(ability)
print "The median ability score is "
print ma
print ""

s_sd = np.std(payrate, ddof=1)
print "The sample standard deviation of payrates is "
print s_sd
print ""

pr = np.corrcoef(ability, payrate)
print "Pearson r calculated using np.corrcoef() = "
print pr
print ""

pr = my_corr(ability, payrate)
print "Pearson r calculated using my_corr() = "
print "%1.8f" % pr

print "\nEnd demo \n"
