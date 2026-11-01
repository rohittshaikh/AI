from sklearn import datasets 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.21,random_state=44)


model = DecisionTreeClassifier(max_depth=3 , random_state=44)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)*100

print(accuracy)
plot_tree(model , feature_names = iris.feature_names , class_names = iris.target_names)

plt.show()

