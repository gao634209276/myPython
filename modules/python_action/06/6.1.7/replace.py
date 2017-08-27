#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字符串的替换
centence = "hello world, hello China"
print centence.replace("hello", "hi")
# replace(self, old, new, count=None)
print centence.replace("hello", "hi", 1)
print centence.replace("abc", "hi")