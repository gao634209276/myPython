#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
__str__()用于表示对象代表的含义，返回一个字符串.
实现了__str__()方法后，可以直接使用print语句输出对象，
也可以通过函数str()触发__str__()的执行.这样就把对象和字符串关联起来，便于某些程序的实现，可以用这个字符串来表示某个类
"""


class Fruit:  # 为Fruit类定义了文档字符串
	'''Fruit类'''

	def __str__(self):  # 定义对象的字符串表示
		return self.__doc__


if __name__ == "__main__":
	fruit = Fruit()
	print str(fruit)  # 调用内置函数str()触发__str__()方法，输出结果为:Fruit类
	print fruit  # 直接输出对象fruit,返回__str__()方法的值，输出结果为:Fruit类
