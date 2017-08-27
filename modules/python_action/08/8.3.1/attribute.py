#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
由于Python的特殊性，全局成员变量是共享的，
所以类的实例不会为它专门分配内容空间，类似于static，
"""


# 定义类的属性
class Fruit:
	price = 0  # 类的属性,所有的实例都共享此变量，即不单独为每个实例分配

	def __init__(self):
		# self.price += 1 # 通过实例本上修改price,不会修改类共享price
		# Fruit.price += 1  # 通过类修改price每次初始化一个实例都会使类静态共享变量price增1
		# print "init price ", self.price
		self.color = "red"  # 实例属性
		zone = "China"  # 局部变量


if __name__ == "__main__":
	print Fruit.price
	apple = Fruit()
	print apple.color
	# apple.price += 10
	# print "apple's price:" + str(apple.price)  # 通过实例本上修改对应的变量,不会修改到共享变量的值
	Fruit.price = Fruit.price + 10
	print "apple's price:" + str(apple.price)  # 修改共享变量值以后,所有实例对应的该共享变量都会相应被修改
	banana = Fruit()
	print "banana's price:" + str(banana.price)

	apple.price += 10
	print "apple's price:" + str(apple.price)
	test = Fruit()
	print "test's price:" + str(test.price)

"""
类的成员函数默认都相当于是public的，但是默认开头为__的为私有变量，
虽然是私有，但是我们还可以通过一定的手段访问到，即Python不存在真正的私有变量。
例如:__priValue = 0 # 会自动变形为"_类名__priValue"的成员变量  
"""


# 访问私有属性
class Fruit:
	def __init__(self):
		self.__color = "red"  # 私有属性


if __name__ == "__main__":
	apple = Fruit()
	print apple._Fruit__color
