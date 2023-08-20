import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
print(stats.poisson.pmf(7,7))

## Task 3:
print(stats.poisson.cdf(4,7))

## Task 4:
print(1 - stats.poisson.cdf(8,7))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(7, size = 365)

## Task 6:
print(year_defects[0:20])
## Task 7:

print(7*365)

## Task 8:
total_defects = 0
for num_of_defects in year_defects:
  total_defects += num_of_defects
print(total_defects)

## Task 9:
print(year_defects.mean())

## Task 10:
print(year_defects.max())

## Task 11:
print(1-stats.poisson.cdf(15,7))


### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(.9,lam))

# Task 13

over90 =0
for amount in year_defects:
  if amount >= 10:
    over90 += 1
print("The number of days with 10 or more defects is {num}, the probability of observing such a day is:".format(num = over90))

print(over90/len(year_defects))
