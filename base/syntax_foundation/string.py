# coding=utf-8
# 单引号,单引号内可以使用双引号
c1 = '2ght'
print c1
c2 = 'It is a "dog"!'
print c2

# 双引号,双引号内可以使用单引号
c1 = "2ght"
print c1
c2 = "It's a dog!"
print c2

# 三引号,三引号的字符串可以换行
c1 = """he
she
my
you are
hello"""
print c1

# 转义符
print 'It\'s a dog!'
print "hello boy\nhello boy"

# 自然字符串
print "hello boy\nhello boy"
print r"hello boy\nhello boy"

# 字符串的重复
print "hello gilr\n" * 20

# 子字符串
# 索引运算符从0开始索引
# 切片运算符[a:b]是指从第a下标开始到第b-1下标。同样第一位的下标为0.
c1 = "jikexueyuan"
c2 = c1[0]
c3 = c1[7]
c4 = c1[:2]
c5 = c1[2:]
c6 = c1[4:7]
print c6
