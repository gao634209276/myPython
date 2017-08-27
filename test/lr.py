# coding=utf-8
from numpy import loadtxt, where, log, transpose, reshape, zeros
from pylab import scatter, show, legend, xlabel, ylabel

# 读取数据
data = loadtxt('/home/noah/data/data1.txt', delimiter=',')
X = data[:, 0:2]
Y = data[:, 2]
pos = where(Y == 1)
neg = where(Y == 0)

scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
scatter(X[pos, 0], X[pos, 1], marker='x', c='r')
xlabel('Feature1/Exam 1 score')
xlabel('Feature2/Exam 2 score')
legend(['Fail', 'Pass'])
show()


def sigmoid(X):
    '''定义sigmoid函数'''
    den = 1.0 + e ** (-1.0 * X)
    gz = 1.0 / den
    return gz


def compute_cost(theta, X, y):
    '''计算损失函数'''
    m = X.shape[0]  # 训练样本个数
    theta = reshape(theta, (len(theta), 1))  # 参数 theta
    j = (1. / m) * (-transpose(y).dot(log(sigmoid(X.dot(theta))))) - transpose(1 - y).dot(
        log(1 - sigmoid(X.dot(theta))))
    grad = transpose(1. / m) * transpose(sigmoid(X.dot(theta)) - y).dot(X)
    return j[0][0].grad


def compute_grad(theta, X, y):
    '''计算梯度'''
    theta.shape = (1, 3)
    grad = zeros(3)
    h = sigmoid(X.dot(theta.T))
    delta = h - y
    l = grad.size
    for i in range(l):
        sumdelta = delta.T.dot(X[:, i])
        grad[i] = (1.0 / m) * sumdelta * -1
        theta.shape = (3,)
        return grad
