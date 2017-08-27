#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __new__和__init__具有不同的功能。并且对于python的新类和旧类而言功能也不同。
# Python中的类分为新类和旧类。旧类是Python3之前的类，旧类并不是默认继承object类，而是继承type类。
# 旧类: class oldStyleClass:  pass # inherits from 'type'
# 新类:class newStyleClass(object): pass # explicitly inherits from 'object'
# 在Python3中所有的类均默认继承object，所以并不需要显式地指定object为基类。
# 以object为基类可以使得所定义的类具有新类所对应的方法（methods）和属性（properties）。
# Python的旧类中实际上并没有__new__方法。因为旧类中的__init__实际上起构造器的作用。旧类构造实例并不会调用__new__方法。
# Python的新类允许用户重载__new__和__init__方法，且这两个方法具有不同的作用。
# __new__作为构造器，起创建一个类实例的作用。
# 而__init__作为初始化器，起初始化一个已被创建的实例的作用。
class Singleton(object):
	__instance = None  # 定义实例

	# __init__是用来初始化一个实例的（initializer）
	# __init__所接收的第一个参数是self
	# 当我们调用__init__的时候，实例已经存在，因此__init__接受self作为第一个参数并对该实例进行必要的初始化操作
	def __init__(self):
		pass

	# __new__在__init__之前调用
	# __new__是用来创造一个类的实例的（constructor）
	# __new__所接收的第一个参数是cls,这是因为当我们调用__new__的时候，该类的实例还并不存在（也就是self所引用的对象还不存在），
	# 所以需要接收一个类作为参数，从而产生一个实例。
	def __new__(cls, *args, **kwd):  # __new__在__init__之前调用
		if Singleton.__instance is None:  # 生成唯一实例
			Singleton.__instance = object.__new__(cls, *args, **kwd)
		return Singleton.__instance
