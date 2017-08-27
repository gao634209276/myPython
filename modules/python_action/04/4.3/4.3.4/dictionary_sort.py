#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 调用sorted()排序
dict = {"a": "apple", "b": "grape", "c": "orange", "d": "banana"}
print dict
# 按照key排序
print sorted(dict.items(), key=lambda d: d[0])
# 按照value排序
print sorted(dict.items(), key=lambda d: d[1])

# 字典的浅拷贝(引用同一个字典)
dict = {"a": "apple", "b": "grape"}
dict2 = {"c": "orange", "d": "banana"}
dict2 = dict.copy()
print dict2

# 字典的深拷贝(新的字典)
import copy

dict = {"a": "apple", "b": {"g": "grape", "o": "orange"}}
dict2 = copy.deepcopy(dict)
dict3 = copy.copy(dict)
dict2["b"]["g"] = "orange"
print dict
dict3["b"]["g"] = "orange"
print dict
