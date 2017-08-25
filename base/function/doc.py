# coding=utf-8
# 文档字符串,紧临函数定义,三引号包括,第一行简单解释,第二行空行,第三行参数,返回值,具体功能等解释
from pydoc import help


def d(i, j):
    """这个函数实现一个乘法运算。

    函数会返回一个乘法运算的结果。"""
    k = i * j
    return k


print d.__doc__

help(d)
