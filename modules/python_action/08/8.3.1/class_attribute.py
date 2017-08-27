#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
	def __init__(self):
		self.__color = "red"


"""
Python是面向对象的编程语言，也支持类继承。
如下Apple(Fruit)表示Apple继承了Fruit
issubclass(a,b)可以测试继承关系
在python中，每个类有一个__bases__属性，列出其基类
如下 Apple.__bases__为(<class __main__.Fruit at 0x7fe2bf1c4b48>,)
如果多继承,会打印所有基类
"""


class Apple(Fruit):  # Apple继承了Fruit
	pass


if __name__ == "__main__":
	fruit = Fruit()
	apple = Apple()
	print Apple.__bases__  # 输出基类组成的元组
	print apple.__dict__  # 输出属性组成的字典
	print apple.__module__  # 输出类所在的模块名
	print apple.__doc__  # 输出doc文档
