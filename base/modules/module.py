# coding=utf-8
# 使用某个模块必须先导入
import math
import sys  # sys模块

# from sys import version
# from sys import *

print math.pi
print sys.version
print sys.executable  # 返回当前运行python的脚本目录
print sys.modules.keys()  # 导入模块的关键字

print dir(sys)
print sys.__doc__
print sys.platform
# dir仅返回属性列表
c = []
d = ['a', 'b']
print dir(c), dir(d)
