import numpy
import statistics

dataset1= [1,3,8,9,11,15,17]

#Mean
mean1= numpy.mean(dataset1)
print("Mean using numpy: ", mean1)
mean2= statistics.mean(dataset1)
print("Mean using statistics: ", mean2)

#Median
median1= numpy.median(dataset1)
print("Median using numpy: ", median1)
median2= statistics.median(dataset1)
print("Median using statistics: ", median2)

#We can't get mode using numpy
#There are statistics and scipy.stats library for doing that
#Mode
import scipy.stats
#statistics is already imported before
dataset2= [1,5,7,4,6,9,8,7,2,4,6,22,7,7,8,3,7]
mode1= statistics.mode(dataset2)
print("Mode using statistics: ", mode1)
mode2= scipy.stats.mode(dataset2)
print("Mode using Scipy.stats: ", mode2)
#using scipy.stats will also show how much frequency the mode have
