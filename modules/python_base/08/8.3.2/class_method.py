#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.
1.定义方式
	通的类方法getColor(self)需要通过self参数隐式的传递当前类对象的实例
		self和cls的区别不是强制的，只是PEP8中一种编程风格，
		slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数。
		即通常用self来传递当前类对象的实例，cls传递当前类对象。
	@classmethod修饰的方法 getPrice(cls):需要通过cls参数传递当前类对象。
	@staticmethod修饰的方法定义与普通函数是一样的。
	@staticmethod是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。
2.绑定对象
	通的类方法绑定类实例(self)
	@classmethod修饰的方法绑定类本身(cls)
	@staticmethod没有参数绑定
3.调用方式
	通的类方法可通过实例对象调用,如果用类直接调用会参数错误
	另外也可以通过类显示传递实例为参数调用,如下:Fruit.getColor(apple)
	@classmethod修饰的方法,实例对象和类均可调用
	@staticmethod修饰的方法没有限制
"""


class Fruit:
	price = 0

	def __init__(self):
		self.__color = "red"

	def getColor(self):
		print self.__color

	"""
	@classmethod 在python中的概念为装饰器,类似于java,scala中的注解,在js中也有装饰器的概念,这个是相通的
	装饰器的意思为:把一个函数当做参数然后返回一个替代版函数。
	这里@classmethod 等同于 getPrice=staticmethod(getPrice)
		这里执行过程是先把getPrice作为参数在classmethod中经过一些操作,
		然后有返回getPrice方法,再执行getPrice方法的内容
	也就是说对修饰的函数做了一层封装
	"""

	@classmethod  # 类方法
	def getPrice(cls):
		print cls.price

	def __getPrice(self):
		self.price = self.price + 10
		print self.price

	""" 
	类方法是给类用的，类在使用时会将类本身当做参数传给类方法的第一个参数，
	python为我们内置了函数classmethod来把类中的函数定义成类方法
	"""
	count = classmethod(__getPrice)  # 类方法


if __name__ == "__main__":
	apple = Fruit()
	apple.getColor()
	Fruit.getColor(apple)
	Fruit.count()
	banana = Fruit()
	Fruit.count()
	Fruit.getPrice()
