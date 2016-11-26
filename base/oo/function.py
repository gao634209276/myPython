# coding=utf-8
# 方法及属性的实现
class woman:
    pass


wangdama = woman()

# 查看一个实例具有哪些属性
print wangdama.__dict__
# 为一个实例添加属性
wangdama.toufa = "huangse"
print wangdama.__dict__
# 为其中一个实例添加了某属性之后，该类中的其他实例的属性不受影响
lidama = woman()
print lidama.__dict__

# 查看一个实例所属类的属性
print wangdama.__class__.__dict__
# 给某个实例所属类添加属性
wangdama.__class__.xiezi = "heise"
print wangdama.__class__.__dict__
# 在修改了其中一个实例的类属性后，查看该实例所属类的其他实例类属性受到影响
print lidama.__class__.__dict__

'''
# 所以我们得出结论：
在单独修改某个实例属性时，其他实例属性不受影响。
若修改类属性，那么该类下所有实例类属性均受影响
'''


# 类中方法创建
class god:
    def a(self):  # 这里的self是必须的，所有的方法，第一个参数必须是self，代表所有实例共享他，不具备其他任何含义
        print "所有人必须明天唱一首歌"


zongguan = god()
zongguan.a()

# 不能直接通过类去调用方法,需要通过实例调用
# god.a()
god().a()


# 隐藏属性与隐藏方法
class school:
    def __jiaoxuefangfa(self):
        print "&^^*&*"


# （__）表示这个方法做了隐藏，隐藏后，在外面无法调用该方法
# 如果我们去掉下划线，我们发现，在外面就可以调用了
# school().__jiaoxuefangfa()

# 类常见的一些专有方法
# 1.__init__，构造函数
class people:
    def hi(self):
        print 8899

    def __init__(self):
        a = "A:how are you?"
        b = "----B:Fine,thankyou"
        print a + b


people()


# 2.__del__,析构函数
class friend:
    def hi(self):
        print 8899

    def __init__(self):
        print "我是init最先调用"

    def __del__(self):
        a = "我是析构函数"
        b = "----对象生命周期结束啦，现在我得删除对象善后啦！"
        print a + b


xiaohang = friend()
xiaohang.hi()
# friend()
# friend().hi()
