# -*- coding: utf-8 -*-
# 主成分分析 降维
import pandas as pd

# 参数初始化
inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xls'  # 降维后的数据

data = pd.read_excel(inputfile, header=None)  # 读入数据

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
pca.components_  # 返回模型的各个特征向量
pca.explained_variance_ratio_  # 返回各个成分各自的方差百分比
#########################################################
# 前三个总和 0.97372012837096455
pca.explained_variance_ratio_[:3].sum()
# 则取前3个主成分,n_components表示要保留的主成分个数n
pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)  # 用它老降低维度
pca.inverse_transform(low_d)  # 必要时可以用inverse_transform复原数据
print low_d
