#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 在类中实现__call__()方法，可以在对象创建时直接返回__call__()的内容.使用该方法可以模拟静态方法
class Fruit:
	class Growth:  # 内部类
		# __init()__的作用是创造某个类的一个实例。
		# __init()__函数的意义等同于类的构造器（同理，__del()__等同于类的析构函数）
		# def __init__(self):
		# 	print "init ..."

		# __call()__的作用是使实例能够像函数一样被调用，同时不影响实例本身的生命周期（__call()__不影响一个实例的构造和析构）
		# 假设x是X类的一个实例。那么调用x.__call(1,2)__等同于调用x(1,2)。这个实例本身在这里相当于一个函数。
		# __call()__可以用来改变实例的内部成员的值。
		def __call__(self):
			print "grow ..."

	# grow原本为Growth的实例,由于Growth实现了__call__,
	# 所以这里的grow可以在外部类中像函数一般本调用,而Growth()可以看做内部类的静态函数
	grow = Growth()  # 返回__call__的内容


if __name__ == '__main__':
	# 通过Fruit调用grow(),触发内部类__call__
	Fruit.grow()

	# 通过Fruit的实例调用grow(),触发内部类__call__
	fruit = Fruit()
	fruit.grow()
