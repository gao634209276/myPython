# coding=utf-8
# 全局变量与局部变量


# 作用域
# i作用域在func中,外部print无效
def func():
    i = 8


# print i, j   # j的作用域从12行开始,先print无效
j = 9
print j


# 局部变量
def func2(a):
    i = 7
    print "func2内部", i


i = 9
# 这里输出的i是7和9
func2(i)
print "func2外部", i


# 全局变量,global全局声明
def func3():
    global i
    i = 7
    print "func3内部global", i


# i=9
func3()
# i = 9
print "func3外部:", i
