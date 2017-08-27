#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = -1
y = 99
if(x >= 0):
    if(x > 0):          #嵌套的if语句
        y = 1
    else:
        y = 0
else:
    y = -1
print "y =", y

# 错误的嵌套语句
x = -1
y = 99
if(x <> 0):
    if(x > 0):          #嵌套的if语句
        y = 1
else:
    y = 0
print "y =", y