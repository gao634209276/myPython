# coding=utf-8

# 导入re库文件
import re

# from re import findall,search,S

secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

# . 匹配任意字符，换行符\n除外
a = 'xy123'
print re.findall('x...', a)
# *匹配前一个字符0次或无限次
print re.findall('x*', a)
# ? 匹配前一个字符0次或1次
print re.findall('x?', a)

'''上面的内容全部都是只需要了解即可，需要掌握的只有下面这一种组合方式(.*?)'''
# .* 贪心算法
print re.findall('xx.*xx', secret_code)
# .*？的使用举例
print re.findall('xx.*?xx', secret_code)
# （）：括号内的数据作为结果返回
d = re.findall('xx(.*?)xx', secret_code)
print d
for each in d:
	print each

s = '''sdfxxhello
xxfsdfxxworldxxasdf'''
# re.S 包括换行符
print re.findall('xx(.*?)xx', s, re.S)

# findall： 匹配所有符合规律的内容，返回包含结果的列表
# Search：匹配并提取第一个符合规律的内容，返回一个正则表达式对象（object)
s2 = 'asdfxxIxx123xxlovexxdfd'
print re.search('xx(.*?)xx123xx(.*?)xx', s2).group(2)
f2 = re.findall('xx(.*?)xx123xx(.*?)xx', s2)
print f2[0][1]

# Sub：替换符合规律的内容，返回替换后的值
s = '123rrrrr123'
output = re.sub('123(.*?)123', '123%d123' % 789, s)
print output

# 演示不同的导入方法,from re import findall,search,S
# info = findall('xx(.*?)xx',secret_code,S)
# for each in info:
#     print each

# 不要使用compile
# pattern = 'xx(.*?)xx'
# new_pattern = re.compile(pattern,re.S)
# output = re.findall(new_pattern,secret_code)
# print output

# 匹配数字
a = 'asdfasf1234567fasd555fas'
b = re.findall('(\d+)', a)
print b
