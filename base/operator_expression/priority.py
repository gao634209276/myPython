# coding=utf-8

# 优先级的作用
a = 2 + 7 * 8
b = 9 > 7
print a, b
# 优先计算
a = (2 + 5) * 6
b = ((2 + 5) + 5) * 6
print a, b

# 优先级使用实战
# 优先级排行榜第1名——函数调用、寻址、下标
# 优先级排行榜第2名——幂运算**
print 4 * 2 ** 3
# 优先级排行榜第3名——翻转运算~
# 优先级排行榜第4名——正负号
print 2 + 4 * -2  # 我们可以看，正负号的使用方法是紧挨着操作数的，否则会出错，这就说明正负号优先于加减乘除运算
# 优先级排行榜第5名——*、/、%
# 优先级排行榜第6名——+、-
# 优先级排行榜第7名——<<、>>
print 2 + 4 * 2 / 4
print 3 << 2 + 1
# 优先级排行榜第8名——按位&、^、|，其实这三个中也是有优先级顺序的，但是他们处于同一级别，故而不细分
# 优先级排行榜第9名——比较运算符
print 2 * 3 + 5 <= 5 + 1 * 2
# 优先级排行榜第10名——逻辑的not、and、or
# 优先级排行榜第11名——lambda表达式


# 优先级使用规律
# 1、一般情况下是左结合的
print 4 + 6 + 5 * 6 + 6
# 2、出现赋值的时候一般是右结合
a = 8 + 91
print a

# 优先级使用小技巧
# 如果实在分不清哪个优先级高哪个优先级低也没关系，只要用（）改变优先级即可
a = 2 + 3 * 7
b = (2 + 3) * 7
print a
print b
