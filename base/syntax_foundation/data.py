# coding=utf-8
# 列表
students = ["小明", "小华", "小李", "小娟", "小云"]
print students[3]
students[3] = "小月"
print students[3]

# 元组
students = ("小明", "小军", "小强", "小武", "小龙")
print students[1]
# students[1] = "小云"  # 元祖不能修改,只能读取
# print students[1]

# 集合
a = set("abcnmaaaaggsng")
b = set("cdfm")
x = a & b  # 交集
y = a | b  # 并集
z = a - b  # 差集
new = set(a)  # 去除重复元素
print a, b, x, y, z, new

# 字典
k = {"姓名": "韦玮", "籍贯": "桂林"}
print k["籍贯"]

# 添加字典里面的项目
k["爱好"] = "音乐"
print k["姓名"]
print k["爱好"]
