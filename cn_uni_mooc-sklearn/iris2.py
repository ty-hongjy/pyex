from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import graphviz

import os
# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'  
#后面的地址为自己安装graphviz的bin文件的地址
iris = load_iris()

# 数据拆分
X = iris.data
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0, test_size=1/4)

# 训练模型
dt_model = DecisionTreeClassifier(max_depth=4)
dt_model.fit(X_train, y_train)

# 数据可视化
tmp_dot_file = 'decision_tree_tmp.dot'
export_graphviz(dt_model, out_file=tmp_dot_file, feature_names=iris.feature_names, class_names=iris.target_names,filled=True, impurity=False)
with open(tmp_dot_file) as f:
        dot_graph = f.read()
graphviz.Source(dot_graph)

from IPython.display import Image  
# import matplotlib.pyplot as plt
import pydotplus

tmp_dot_file = 'decision_tree_tmp.dot'
export_graphviz(dt_model, out_file=tmp_dot_file, feature_names=iris.feature_names, class_names=iris.target_names,filled=True, impurity=False)
with open(tmp_dot_file) as f:
    dot_graph = f.read()
graph = pydotplus.graph_from_dot_data(dot_graph)
graph.write_pdf('example.pdf')    #保存图像为pdf格式
Image(graph.create_png())   #绘制图像为png格式
