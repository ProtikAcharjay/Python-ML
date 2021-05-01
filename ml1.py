import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
diabetes= datasets.load_diabetes()
# print(diabetes.keys())
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
# print(diabetes.DESCR)
# for one liner result or regression use the line below
# diabetes_x=diabetes.data[:, np.newaxis,2]
diabetes_x=diabetes.data
diabetes_x_train= diabetes_x[:-30]
diabetes_x_test= diabetes_x[-30:]
diabetes_y_train= diabetes.target[:-30]
diabetes_y_test= diabetes.target[-30:]

model= linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predict= model.predict(diabetes_x_test)

print("Mean squared error is : ", mean_squared_error(diabetes_y_test,diabetes_y_predict))

print("weights: ", model.coef_)
print("intercept: ", model.intercept_)

#for ploting and show the graph
# plt.scatter(diabetes_x_test, diabetes_y_test)
# plt.plot(diabetes_x_test,diabetes_y_predict)
# plt.show()

# previous results::
# Mean squared error is :  3035.0601152912695
# weights:  [941.43097333]
# intercept:  153.39713623331698