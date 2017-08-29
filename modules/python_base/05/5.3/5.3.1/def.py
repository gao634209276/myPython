#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 函数的定义
# 导入python未来支持的语言特征division(精确除法)，
# 当我们没有在程序中导入该特征时，"/"操作符执行的是截断除法(Truncating Division),
# 当我们导入精确除法之后，"/"执行的是精确除法
from __future__ import division


def arithmetic(x, y, operator):
	result = {
		"+": x + y,
		"-": x - y,
		"*": x * y,
		"/": x / y
	}
	return result.get(operator)  # 返回计算结果


# 函数的调用
print arithmetic(1, 2, "+")
