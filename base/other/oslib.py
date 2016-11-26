# coding=utf-8
# os模块
import os

# 获取操作系统平台
print os.name

# 获取工作目录
print os.getcwd()

# 获取某个目录下的所有文件名
print os.listdir("./")

# 运行一个shell命令
os.system("java")

# 删除某个文件
# os.remove("../../file/file.txt")

# 判断一个地方是文件夹还是文件
print os.path.isfile("../../file")
print os.path.isdir("../../file")

# 把一个路径拆分为目录+文件名的形式。
print os.path.split("/home/hadoop/Documents/workspaces/pycharm/myPython/other/oslib.py")
print os.path.split("/home/hadoop/Documents/workspaces/pycharm/myPython")
# print os.path.split("C:/python27/")
