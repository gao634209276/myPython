# coding=utf-8
# 异常的引发
# 1/用raise引发一个系统的错误类
i = 8
print i
if i > 7:
    print 9


# raise NameError  # 手动引发错误
#    print 10


# 2/自定义一个异常并用raise引发
class RhhError(Exception):  # 按照命名规范，以Error结尾，并且自定义异常需要继承Exception类
    def __init__(self):
        Exception.__init__(self)


try:
    i = 8
    if i > 7:
        raise RhhError()
except RhhError, a:  # a是RhhError的一个实例,任意名称均可以
    print "RhhError:错了就是错了"


# 3/自定义一个多参数的异常并用raise引发，比如我们可以定义一个异常，当x>2或者x+y>7的时候都会引发该异常
class HhhError(Exception):
    def __init__(self, x, y):
        Exception.__init__(self, x, y)
        self.x = x
        self.y = y


try:
    x = 3
    y = 5
    if x > 2 or x + y > 7:
        raise HhhError(x, y)
except HhhError:
    print "HhhError: x必须小鱼等于2且x+y小于等于7"
    print "现在x为" + str(x) + "现在的y是: " + str(y)