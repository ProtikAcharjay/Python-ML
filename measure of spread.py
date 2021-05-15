import numpy as np
n= np.random.randint(1,55,11)
print("dataset array is", n)
#measures of spread
# Range
result= np.max(n)- np.min(n)
print("The range is: ", result)

#Quartile....q1(25%)...q2(50%)= is always median....q3(75%)

dataset=[8,9,2,10,3,5,7,12,15]
Q1= np.percentile(dataset,25)
print(Q1)
Q2= np.percentile(dataset,50)
print(Q2)
Q3= np.percentile(dataset,75)
print(Q3)
#interquartile range
iqr= Q3 - Q1
print("interquartile: ", iqr)