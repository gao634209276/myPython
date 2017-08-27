# coding=utf-8
## 1.内置list方法。
a = "asd"
list(a)

# 返回一个列表，参数是可迭代对象。里面输出的内容还是保持了传入的可迭代对象的元素和顺序。
# 如果参数为空，则返回一个空的列表
## 2.xrange和range的具体区别。
# 2.1 xrange的用法：
# xrange(开始，结束，步长)
# xrange
# 它生成一个xrange对象。
# 比如我们
a = xrange(1, 10)
print type(a)
print a[0]

# 2.2 比较
# range: 直接生成一个列表对象。
# range: 它是生成一个xrange对象.
# xrange的用法：
# 1 当我们需要操作一个非常大的数据，而且内存比较吃紧的时候，我们可以用xrange来操作省内存。
# 2 xrange一般用在循环里面，比如我们只需要操作部分数据的话，而不是返回全部元素来完成操作，推荐用xrange, 效率更高。
# 比如：
for m in range(1000):
	if m == 10:
		print 'sss'
		break

for m in xrange(1000):

	if m == 10:
		print 'sss'
		break

## 3.列表推导式之再应用。
# 3.1 可以做很多例子只要你有想法，例
# 3.1.2 取出1 - 100的所有值的平方。
print [x * x for x in range(100)]
# 3.1.3 里面生成东西不只是数字。
# 生成字符串
print ['the %s' % d for d in xrange(10)]
# 生成元组
print [(x, y) for x in range(2) for y in range(2)]
# 生成字典
# 举例
dict([(x, y) for x in range(3) for y in range(2)])
## 4 翻来覆去之再谈引用
a = ['i', 'am', 'lilei']
b = a
a[2] = 'laowang'
print b
# 这里b的值是什么？
del b
print a  # a是什么值

## 5 小技巧之再议删除 a = []
# 1 del a 删除列表对象的引用
# 2 del a[:] 清空列表对象里的元素
