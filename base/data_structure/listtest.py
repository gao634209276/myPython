# coding=utf-8
nameList = ['Alex', 'DongXu', 'Jack', 'Jessie']
nameList.insert(2, 'FeiFei')
nameList.append("OldBoy")
print nameList
print nameList.count("Alex")
print nameList.index("FeiFei")
nameList.remove("FeiFei")
print nameList
nameList.reverse()

extend = ["hello", "world"]
nameList.extend(extend)
del nameList[1]
print nameList

print nameList.pop(2)
print nameList
## 当我们需要操作一个非常大的数据，而且内存比较持剑的时候，



a = xrange(1, 10)  # 生成一个xrange对象
b = range(1, 10)  # 直接生成一个列表
print a
print b

# 课程内容
# 列表：
# 1 有序的集合
# 2 通过偏移来索引，从而读取数据
# 3 支持嵌套
# 4 可变的类型
# 1 切片：
a = [1, 2, 3, 4, 5, 6, 7]

# 正向索引
# 反向索引
# 默认索引
## 2 添加操作：
# + 生成一个新的列表
# Extend 接受参数并将该参数的每个元素都添加到原有的列表中，原地修改列表而不是新建列表
# Append:添加任意对象到列表的末端
# Insert: 插入任意对象到列表中，可以控制插入位置。


## 3 修改：
# 修改列表本身只需要直接赋值操作就行。
A = [1, 2, 3]
A[0] = 'haha'

## 4 删除操作：
# Del ：我们通过索引删除指定位置的元素。
# Remove：移除列表中指定值的第一个匹配值。如果没找到的话，会抛异常。
# Pop：返回最后一个元素，并从list中删除它。
## 5 成员关系：
# In not in我们可以判断一个元素是否在列表里。
# 返回一个bool类型，元素在列表里返回true，否则返回fasle.
#
# 6 列表推导式： [expr for iter_var in iterable]
# 1 首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。
# 比如我们要生成一个包含1到10的列表

[x for x in range(1, 11)]
range(1, 11)
# [expr for iter_var in iterable if cond_expr]
# 2 加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。
# 要生成包含1到10的所有奇数列表。
range(1, 11, 2)
[x for x in range(1, 11) if x % 2 == 1]
# 7 排序翻转：sort, reverse

a = [33, 11, 22, 44]
# 这个方式直接修改原列表。他的返回值为none，所以
b = a.sort()
print b
# 输出的内容是None
# 我们直接输出a列表变量
# list的reverse函数：反转一个list, 他的返回值为none
# 比如上面的列表a
b = a.reverse()
print b
# 输出的内容是None
# 直接看a列表变量能看到翻转的效果。
