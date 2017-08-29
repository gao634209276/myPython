#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
 __get__,__getattr__和__getattribute都是访问属性的方法，但不太相同。

object.__getattr__(self, name) 
当读取对象的某个属性时，python会自动调用__getattr__()方法.例如，fruit.color将转换为fruit.__getattr__(color).
当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。
常用于:
 1,用作实例属性的获取和拦截
 2,自定义getattribute的时候防止无限递归
 3.同时覆盖掉getattribute和getattr的时候，在getattribute中需要模仿原本的行为抛出AttributeError或者手动调用getattr
 参考:http://python.jobbole.com/84095/
 
object.__getattribute__(self, name) 
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用
（除非显示调用或引发AttributeError异常） 
__getattribute__()的功能与__getattr__()类似，用于获取属性的值.但是__getattribute__()能提供更好的控制，代码更健壮

object.__get__(self, instance, owner) 
如果class定义了它，则这个class就可以称为descriptor。
owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。
（descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）
（所以下文的d是作为C2的一个属性被调用）

__setattr__()
当使用赋值语句对属性进行设置时，python会自动调用__setattr__()方法
"""


class Fruit(object):
	def __init__(self, color="red", price=0):
		self.__color = color
		self.__price = price

	"""
	__getattribute__是访问属性的方法，我们可以通过方法重写来扩展方法的功能。
	对于Python来说，属性或者函数都可以被理解成一个属性，且可以通过__getattribute__获取。
	当获取属性时，直接return object.__getattribute__(self, *args, **kwargs)
	如果需要获取某个方法的返回值时，则需要在函数后面加上一个()即可。如果不加的话，返回的是函数引用地址。
	如:return object.__getattribute__(self,'name')()
	"""

	def __getattribute__(self, name):  # 获取属性的方法
		return object.__getattribute__(self, name)

	def __setattr__(self, name, value):
		self.__dict__[name] = value


if __name__ == "__main__":
	fruit = Fruit("blue", 10)
	print fruit.__dict__.get("_Fruit__color")  # 获取color属性
	fruit.__dict__["_Fruit__price"] = 5
	print fruit.__dict__.get("_Fruit__price")  # 获取price属性
