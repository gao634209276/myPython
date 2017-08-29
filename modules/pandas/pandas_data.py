
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np


# In[3]:


s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
s


# In[4]:


# s.index就是s的索引
s.index


# In[6]:


# 也可以不指定索引,默认为从0升序的数字
s = pd.Series(np.random.randn(4))
s


# In[8]:


# 数据也可以通过字典,与key与索引对应
d = {'a':0.,'b':1.,'d':3}
s = pd.Series(d,index=list('abcd'))
s


# In[9]:


# 数据如果是一个标量,产生索引对应个数的标量序列
s = pd.Series(5,index=list('abcd'))
s


# In[10]:


# Series对象的特性
# 先创建一个Series
s = pd.Series(np.random.randn(5))
s


# In[11]:


# ndarray的特性,根据坐标查看对应元素
s[4]


# In[12]:


# 通过ndarray的切片的性质,访问子序列
s[:3]


# In[13]:


s[2:5]


# In[16]:


# 也可选择整型组成的list序列
s[[1,3,4]]


# In[17]:


# numpy的函数可以对Series的ndarray对象直接使用
np.sin(s)


# In[18]:


np.exp(s)


# In[19]:


# 以上操作适用的对象,我们称之为类ndarray对象
# Series另一个铁兴是,类dict对象,即可以直接使用字典的方式访问,如下创建一个类字典Series对象
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
s


# In[20]:


# 类dict对象元素访问如下:
s['a']


# In[21]:


# 用dict方法赋值
s['b'] = 3


# In[22]:


# 可以用dict方法直接增加元素
s['g'] = 100
s


# In[23]:


# 用dict方法访问不存在元素,报错
s['f']


# In[25]:


# 可以使用dict的get方法访问元素,如果不存在返回None
print s.get('f')


# In[26]:


# get指定默认值
print s.get('f',0)


# In[28]:


# 标签对齐,穿件连个Series数据:
s1 = pd.Series(np.random.randn(3),index=['a','c','e'])
s2 = pd.Series(np.random.randn(3),index=['a','d','e'])
print '{0}\n\n{1}'.format(s1,s2)


# In[29]:


# 那么如果对以上两组数据相加后,会自定根据标签对齐,如果有一个为NaN,结果为Nan
s1 + s2


# In[31]:


#DataFrame 是一个二维的标签的数组,一个行标签,一个列标签
# 创建DataFrame的基本格式为:
# df = pd.DataFrame(data,index=index,columns=columns)
# 其中index是行标签,columns是列表前,data可以是一下数据:
# 1)由一个numpy数组list,Series构成的字典
# 2)二维numpy数组
# 3)一个Series
# 4)另外一个DataFrame对象

# 例子1:Series构成的字典
d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
    'two' : pd.Series([1,2,3,4], index=['a','b','c','d'])}
df = pd.DataFrame(d)
df


# In[32]:


# 当然在创建DataFrame时候可以直接指定索引
df = pd.DataFrame(d, index = ['d','b','a'])
df


# In[33]:


# 也可指定列名称
df = pd.DataFrame(d,columns=['two','three'])
df


# In[35]:


# 然后看一下有list列表构成的字典元素的创建

# 这里与由Series构成的字段元素有一个区别,就是List的元素个数必须相同
# 因为Pandas没有办法做行标签的对齐操作
d = {'one' : [1,2,3,4],
    'two' : [21,22,23,24]}

df = pd.DataFrame(d)
df


# In[39]:


# 列表数据
# data是一个列表,列表内为元祖,包含各种数据类型
data = [(1,2.2,'Hello'),(2,3.,'World')]
# 可以指定行标签,列标签
df = pd.DataFrame(data, index=['one','two'], columns=list('ABC'))
df


# In[43]:


# 列表中为字典数据
data = [{'a':1, 'b':2}, {'a':5, 'b':10, 'c':20}]
# 创建DataFrame时,列表中字典的key被作为列名称,这里可指定行索引
df = pd.DataFrame(data, index=['A','B'])
df


# In[45]:


# 也可以指定列名称,那么只会显示相应列名称的数据
df = pd.DataFrame(data, index=['A','B'],columns=['a','b','e'])
df


# In[53]:


# 复杂数据结构,字典中key为元祖,value为字典,内部key和value为元祖:标量
d = {('a','b'):{('A','B'):1,('A','C'):2},
     ('a','a'):{('A','C'):3,('A','B'):4},
     ('a','c'):{('A','B'):5,('A','C'):6},
     ('b','a'):{('A','C'):7,('A','B'):8},
     ('b','b'):{('A','D'):9,('A','B'):10},
    }
# 创建DataFrame时,字典的key作为列名称,这里key为一个元祖,在数据上表现为列二级索引
# 字典的value如果也是字典时,key作为行索引,这里又是个元祖,那么表现为行二级索引
df = pd.DataFrame(d)
df


# In[54]:


# 从Series里创建一个DataFrame
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# 默认情况(即不指定索引),Series中的index为行索引
pd.DataFrame(s)


# In[55]:


# 指定列名称,行索引
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
pd.DataFrame(s,index=list('abc'),columns=['A'])


# In[57]:


#DataFrame特性列选择/增加/删除
# 列选择
# 创建6行4列数据
df = pd.DataFrame(np.random.randn(6,4),columns=['one','two','three','four'])
df


# In[60]:


# 选择一列
df['one']


# In[62]:


# 选择一行
df.loc[1]


# In[63]:


# 赋值
df['three'] = df['one']+df['two']
df


# In[64]:


# 列删除
del df['three']
df


# In[66]:


# 增加列
df['flag'] = df['one'] > 0.2
df


# In[67]:


# 添加新列为标量
df['five'] = 5
df


# In[68]:


# pop方法直接从df中删除掉
df.pop('four')


# In[69]:


df


# In[70]:


# insert插入一列,直接作用在df中,指定列位置,和列数据
df.insert(1,'bar',df['one']+df['two'])
df


# In[73]:


# assign复制df后增加一列返回,不修改df
df.assign(Ratio = df['one'] / df['two'])


# In[74]:


df


# In[75]:


# assign另一个特性可以传入一个函数,这里用lambda函数,参数是df本身
df.assign(Ratio = lambda x:x.one - x.two)


# In[76]:


# 由于assign返回的是一个df,所以可以写成函数链的方式
df.assign(ABRatio = df.one/df.two).assign(BarValue= lambda x : x.ABRatio * x.bar)


# In[77]:


# DataFrame索引和选择
# 选择一列-->df[col]-->Series
# 根据行标签选择一行-->df.loc[label]-->Series
# 根据行位置选择一行-->df.iloc[label]-->Series
# 选择多行-->df[5:10]-->DataFrame
# 根据布尔向量选择多行-->df[bool_vector]-->DataFrame

df = pd.DataFrame(np.random.randint(1,10,(6,4)),index= list('abcdef'),columns=list('ABCD'))
df


# In[78]:


# 通过dict的方法选择一列
df['A']


# In[79]:


# loc选择行
df.loc['a']


# In[80]:


# iloc数字索引
df.iloc[1:4]


# In[81]:


# 字典切片方式
df[1:4]


# In[82]:


# bool变量
df.A >= 6


# In[84]:


# 字典中通过bool变量选择
df[df.A>=6]


# In[85]:


# 数据标签对齐
# 先创建一下的df
df1 = pd.DataFrame(np.random.randn(10,4),index= list('abcdefghij'),columns=list('ABCD'))
df2 = pd.DataFrame(np.random.randn(7,3),index= list('cdefghi'),columns=list('ABC'))


# In[86]:


# 对df1 与df2 相加
df1 + df2


# In[87]:


# 减去一行
df1 -df1.iloc[0]


# In[88]:


# numpy中的函数可以直接作用于dataframe
np.exp(df2)


# In[89]:


# 这是因为df的数据其实就是numpy的ndarray列,可以通过values查看一下数据和类型
df2.values


# In[90]:


type(df2.values)


# In[91]:


# numpy可以直接转换df
# np.asarray(df2)等同于df2.values
np.asarray(df2)


# In[94]:


# Panel是三维带标签的数据,创建过程如下:
# 创建一个字典数据
data = {'Item1' : pd.DataFrame(np.random.randn(4,3)),
       'Item2' : pd.DataFrame(np.random.randn(4,2))}
pn = pd.Panel(data)
pn


# In[95]:


# items第一维度查看索引为Item2的数据是个DataFrame
pn['Item2']


# In[96]:


# items维度所有的索引
pn.items


# In[97]:


# major_axis为坐标轴1,DataFrame里的行标签
pn.major_axis


# In[98]:


# minor_axis:坐标轴2,DataFrame的列标签
pn.minor_axis


# In[100]:


# 通过major_axis坐标索引访问数据
pn.major_xs(1)


# In[101]:


# Panel是可以与DataFrame互相转换的
pn.to_frame()


# In[ ]:




