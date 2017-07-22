# coding=utf-8
# 字典：
# 字典是无序的，它不能通过偏移来存取，只能通过键来存取。
# 字典 = {'key': value}
# key：类似我们现实的钥匙，而value则是锁。一个钥匙开一个锁
# 特点：
# 内部没有顺序，通过键来读取内容，可嵌套，方便我们组织多种数据结构，并且可以原地修改里面的内容，
# 属于可变类型。
# 组成字典的键必须是不可变的数据类型，比如，数字，字符串，元组等，列表等可变对象不能作为键.
# 1 创建字典。{}, dict()
info = {'name': 'lilei', 'age': 20}
# info = dict(name='lilei', age=20)
# 2 添加内容 a['xx'] = 'xx'
# 比如
info['phone'] = 'iphone5'

# 3 修改内容 a['xx'] = 'xx',
info['phone'] = 'htc'
# update 参数是一个字典的类型，他会覆盖相同键的值
info.update({'city': 'beijing', 'phone': 'nokia'})
# htc 变成了nokia了

# 4 删除 del, clear, pop
del info['phone']
# 删除某个元素
info.clear()
# 删除字典的全部元素
info.pop('name')
# 5 in 和 has_key() 成员关系操作 比如：
# 1 phone in info
# 2 info.has_key('phone')
#
# 6 keys(): 返回的是列表，里面包含了字典的所有键
# values():返回的是列表，里面包含了字典的所有值
# items：生成一个字典的容器：[()]
# 7 get：从字典中获得一个值
info.get('name')
info.get('age2', '22')
