#Classification
#loading datasets
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris= datasets.load_iris()
# print(iris.DESCR)
features= iris.data
lebels= iris.target
print(features[0],lebels[0])

#training the classifier
clf=KNeighborsClassifier()
clf.fit(features,lebels)

prediction=clf.predict([[51, 1, 1, 1]])
print(prediction)