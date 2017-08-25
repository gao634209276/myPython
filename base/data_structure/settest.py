# encoding=utf-8
## 二 集合：集合是没有顺序的概念。所以不能用切片和索引操作。
# 1 创建集合。set():可变的 不可变的frozenset()：
# 2 添加操作： add，update
# 3 删除 remove
# 4 成员关系 in, not in
# 6 交集，并集，差集 & | -
# 7 set去重 列表内容元素重复
##可变集合

info = set('abc')
info.add('python')  ##添加单个对象到集合里
print info
info.update('python')  ##把对象里的每个元素添加到集合里
print info
info.remove('python')
print info

##不可变集合
t = frozenset('haha')  ##不能进行添加，修改和删除的操作。

##成员操作 in,not in
print 'a' in info
print 'h' in t
print 'jay' not in info

##判断2个集合是否相等，之和元素本身有关，和顺序无关。
print set('abc') == set('cba')

##并集,交集，差集
print set('abc') | set('cbdef')  ##并集
print set('abc') & set('cbdef')  ##交集
print set('abc') - set('cbdef')  ##差集


# for循环
liststr = ['haha', 'gag', 'hehe', 'haha']
m = []
for i in liststr:
	if i not in m:
		m.append(i)
print m
m = set(liststr)
print list(m)
