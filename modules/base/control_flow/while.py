# coding=utf-8
# 控制流
# 控制流功能
# 要实现：重复执行3段同样的程序

# 方式一,直接顺序重复三次：
# 方式二：
for k in range(0, 3):
	i = 0
	print i
	i += 1
print i  # 再比如，要实现：如果小明吃了饭了，输出小明很乖，如果小明没吃饭，输出小明不乖的功能。
# 平常情况按顺序执行的话，无法实现这样的功能，我们可以用控制流中的分支结构
xiaoming = "eat"
if xiaoming == "eat":
	print "小明很乖"
else:
	print "小明不乖"

# 控制流的类型有三种，一种是顺序结构，一种是分支结构，一种是循环结构
# 分支结构
a = 7
if a == 8:
	print "She"
else:
	print "He"
# 循环结构
a = 7
while a:
	print "helloo"
	a -= 1