from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = load_iris()

# 数据拆分
X = iris.data
y = iris.target
print(X)
print(y)
print(iris.feature_names)
print(iris.target_names)
print(iris.keys)
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0, test_size=1/4)

# 训练模型
dt_model = DecisionTreeClassifier(max_depth=4)
dt_model.fit(X_train, y_train)

# 数据可视化
plt.figure(figsize=(15,9))
plot_tree(dt_model,filled=True,feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
