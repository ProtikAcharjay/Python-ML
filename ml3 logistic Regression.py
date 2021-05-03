#train a logistic regression classsifier to predict whether
# a flower is iris virginica or not?
from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris= datasets.load_iris()
# print(iris.keys())
# dict_keys(['data', 'target', 'frame',_
# 'target_names', 'DESCR', 'feature_names', 'filename'])_
# could be print like this_
# print(iris['data'])
# print(iris.data)
x= iris.data[:, 3:]
y=(iris.target==2).astype(np.int32)

# Training a logistic regression classifier
clf=LogisticRegression()
clf.fit(x,y)
example=clf.predict(([[1.6]]))
print(example)

#using matplotlib to plot the visualization
x_new= np.linspace(0,3,1000).reshape(-1,1)
y_prob= clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:, 1], "g-", )
plt.show()
# print(x,y)