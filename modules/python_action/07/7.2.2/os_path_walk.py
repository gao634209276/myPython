#!/usr/bin/python
# -*- coding: UTF-8 -*-

# os.path.walk遍历目录
import os
import os.path


def VisitDir(arg, dirname, names):
	for filepath in names:
		print os.path.join(dirname, filepath)


if __name__ == "__main__":
	path = r"D:\developer\python\example\07"
	os.path.walk(path, VisitDir, ())
