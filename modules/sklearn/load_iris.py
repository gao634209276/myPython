# coding=utf-8
# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
from sklearn.datasets import load_iris

# 本文中使用sklearn中的IRIS（鸢尾花）数据集来对特征处理功能进行说明
# 1 导入IRIS数据集
iris = load_iris()

# 特征矩阵
print iris.data

# 目标向量
print iris.target

# 2 数据预处理
# 2.1 无量纲化 <--不属于同一量纲：特征的规格不一样，不能够放在一起比较
# 无量纲化方法有标准化和区间缩放法。

# 2.1.1 标准化
# 标准化的前提是特征值服从正态分布，标准化后，其转换成标准正态分布。
from sklearn.preprocessing import StandardScaler

# 标准化，返回值为标准化后的数据
iris = load_iris()
StandardScaler().fit_transform(iris.data)
# 2.1.2 区间缩放法
# 区间缩放法利用了边界值信息，将特征的取值区间缩放到某个特点的范围，例如[0, 1]等。
from sklearn.preprocessing import MinMaxScaler

# 区间缩放，返回值为缩放到[0, 1]区间的数据
iris = load_iris()
MinMaxScaler().fit_transform(iris.data)
# 2.1.3 标准化与归一化的区别
# 标准化是依照特征矩阵的列处理数据，其通过求z-score的方法，将样本的特征值转换到同一量纲下。
# 归一化是依照特征矩阵的行处理数据，其目的在于样本向量在点乘运算或其他核函数计算相似性时，拥有统一的标准，也就是说都转化为“单位向量”。
# 使用preproccessing库的Normalizer类对数据进行归一化的代码如下：
from sklearn.preprocessing import Normalizer

# 归一化，返回值为归一化后的数据
iris = load_iris()
Normalizer().fit_transform(iris.data)

# 2.2 对定量特征二值化
# 定量特征二值化的核心在于设定一个阈值，大于阈值的赋值为1，小于等于阈值的赋值为0，
from sklearn.preprocessing import Binarizer  # 二值化，阈值设置为3，返回值为二值化后的数据

iris = load_iris()
Binarizer(threshold=3).fit_transform(iris.data)

# 2.3 对定性特征哑编码
# 由于IRIS数据集的特征皆为定量特征，故使用其目标值进行哑编码（实际上是不需要的）
from sklearn.preprocessing import OneHotEncoder

iris = load_iris()
# 哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
OneHotEncoder().fit_transform(iris.target.reshape((-1, 1)))

