#we have to calculate the mean of a dataset
#then the distance of mean from every other values of dataset is variance
#variance { stands for how far the data away from mean}
import numpy as np
population= np.random.randn(30)
print("Dataset of population :", population)
sample= np.random.choice(population,20)
print("Dataset of sample :", sample)
result_population= np.var(population)
result_sample= np.var(sample)
print("variance of population data :", result_population)
print("variance of sample data :", result_sample)
# Standard Deviation
# Standard deviation is the squared root of variance
result_population_std = np.std(population)
result_sample_std = np.std(sample)
print("standard deviation of population data :", result_population_std)
print("standard deviation of sample data :", result_sample_std)

#THANK YOU