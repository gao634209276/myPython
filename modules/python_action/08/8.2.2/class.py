#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 类的创建
class Fruit:
	"""
	首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。
	self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
	self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗，不要搞另类，大家会不明白的。
	self指的是类实例对象本身(注意：不是类本身)。
	"""

	def grow(self):
		print "Fruit grow ..."


"""
__name__ 是当前模块名，当模块被直接运行时模块名为 __main__。
这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
"""
if __name__ == "__main__":
	fruit = Fruit()
	fruit.grow()
