"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

iris = datasets.load_iris()
x = iris.data
y = iris.target

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.21,random_state=44)

scalar = StandardScaler()
X_train,X_test = scalar.fit_transform(X_train),scalar.transform(X_test)

model = SVC(kernel="linear",C=1.0)
model.fit(X_train,Y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,pred)*100
report = classification_report(Y_test,pred,target_names=iris.target_names)
matrix = confusion_matrix(Y_test,pred)
print(accuracy)
print(matrix)
print(report)
"""



from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix 

iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.21 , random_state= 44)

scalar = StandardScaler()
x_train,x_test = scalar.fit_transform(x_train),scalar.transform(x_test)

#model = SVC(kernel="linear",C=1.0)
#k=4 
#model = KNeighborsClassifier(n_neighbors=k)
model = GaussianNB()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred) *100
report = classification_report(y_test,y_pred,target_names=iris.target_names)
matrix = confusion_matrix(y_test,y_pred)

print(accuracy)
print(report)
print(matrix)
































