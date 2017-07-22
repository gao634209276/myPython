# coding=utf-8
# 函数功能
# 系统自带函数
# 1.实现取字符串长度功能
# 2.字符串切割
a = "hello Python"
print len(a), a.split(" ")
'''
函数格式:
def 函数名（）：
    函数内容;函数内容
    函数内容;函数内容
'''


# 3.自定义函数
def test_func():
	x = 8
	print x


# 函数形参与实参,参数的概念
# print len()
a = "abcdm"
print len(a)


# a,b是形参,1,2是实参
def max(a, b):
	if a > b:
		print a
	else:
		print b


max(1, 3)

'''
# 参数的传递
# 第一中，最简单的传递,同上
# 第二种，赋值传递,如下
'''


def println(a, b=8):
	print a, b


println(1)
println(1, 2)


# 关键参数
def println(a=1, b=6, c=7):
	print a, b, c


println(5)
println(b=7, a=8)
println(5, c=2, b=3)
println(b=4, c=2, a=1)
# 但是要注意，参数不能冲突
# println(b=2, c=3, 2)
