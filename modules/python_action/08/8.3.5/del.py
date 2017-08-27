#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python中没有专用的构造和析构函数，但是一般可以在__init__和__del__分别完成初始化和删除操作，可用这个替代构造和析构。
类的成员函数默认都相当于是public的，但是默认开头为__的为私有变量，
虽然是私有，但是我们还可以通过一定的手段访问到，即Python不存在真正的私有变量。

由于Python的特殊性，全局成员变量是共享的，所以类的实例不会为它专门分配内容空间，类似于static，
"""


class Fruit:
	def __init__(self, color):  # 初始化属性__color
		self.__color = color
		print self.__color

	def __del__(self):  # 析构函数
		self.__color = ""
		print "free ..."

	def grow(self):
		print "grow ..."


if __name__ == "__main__":
	color = "red"
	fruit = Fruit(color)  # 带参数的构造函数
	fruit.grow()
# del fruit                           # 执行析构函数
