# coding=utf-8
# 逻辑行与物理行
# 以下是3个物理行
print "abc"
print "789"
print "777"

# 以下是1个物理行，3个逻辑行
print "abc";
print "789";
print "777"

# 以下是1个逻辑行，3个物理行
print '''这里是
由极客学院
提供的Python教程！'''

# 分号使用规则
# 所有的逻辑行后均应使用分号，但以下条件除外
print "123";print "456";
print "777";

# 分号可以省略的条件是指：每个物理行的行末可以省略分号,当然也可以不省略分号。
print "123";print "456"  	# 这里的分号可以省略，也可以不省略
print "777"  				# 这里的分号可以省略，也可以不省略


# 行连接,如果没有使用\,将报错
print "我们是\
好孩子"

# 什么是缩进,print如果有缩进讲将报错
print '123'
# 如何缩进
# 一般情况下，行首应该不留空白

# import sys
# 缩进的方法有两种，可以按空格，也可以按tab键
# if语句的缩进方法
a = 7
if a > 0:
    print "hello"

# while语句的缩进方法
a = 0
while a < 7:
    print a
    a += 1
