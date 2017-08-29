# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# In[2]:


s = pd.Series([1, 3, 5, 6, 8], index=list('acefh'))
s

# In[3]:


# Series索引
s.index

# In[4]:


# 增加一些行
s.reindex(list('abcdefgh'))

# In[5]:


# 可以设置新增大索引值默认值
s.reindex(list('abcdefgh'), fill_value=0)

# In[6]:


# ffill如果索引的值为NaN,取前一个值填充
s.reindex(list('abcdefgh'), method='ffill')

# In[8]:


# 对dataFrame是相似的
df = pd.DataFrame(np.random.randn(4, 6), index=list('ADFH'), columns=['one', 'two', 'three', 'four', 'five', 'six'])
df

# In[9]:


df.reindex(index=list('ABCDEFGH'))

# In[13]:


# 对新增的索引设置默认值
df2 = df.reindex(index=list('ABCDEFGH'), fill_value=0)

# In[14]:


# 修改df数据
df.loc['A']['one'] = 100
df

# In[15]:


# df2 是从df重新索引的,是df复制一份数据,修改df,df2不影响
df2

# In[16]:


# 对DataFrame列进行重新索引
df.reindex(columns=['one', 'three', 'five', 'seven'])

# In[17]:


# 对新增列设置默认值
df.reindex(columns=['one', 'three', 'five', 'seven'], fill_value=0)

# In[18]:


# 注意:增加列时候,ffill方法不生效
df.reindex(columns=['one', 'three', 'five', 'seven'], method='ffill')

# In[19]:


# bfill为向后填充,比如填充index
df.reindex(index=list('ABCDEFGH'), method='bfill')

# In[20]:


# 丢弃数据
# 丢弃一行
df.drop('A')

# In[21]:


# 丢弃一列,默认axis为0,即行数据,选择列时候指定为1
df.drop(['two', 'four'], axis=1)

# In[23]:


# 按列进行运算
df = pd.DataFrame(np.arange(12).reshape(4, 3), index=['one', 'two', 'three', 'four'], columns=list('ABC'))
df

# In[25]:


# apply默认按列运算,axis=0,参数为一个函数,这里用lambda表达式
df.apply(lambda x: x.max() - x.min())

# In[26]:


# 如果按行,添加参数axis=1
df.apply(lambda x: x.max() - x.min(), axis=1)


# In[27]:


# 可以查看apply文档
# get_ipython().magic(u'pinfo df.apply')


# In[28]:


# 定义一个函数,返回一个序列
def min_max(x):
	return pd.Series([x.min(), x.max()], index=['min', 'max'])


df.apply(min_max)
#  df.apply(min_max,axis=1)


# In[29]:


# applymap操作
df = pd.DataFrame(np.random.randn(4, 3), index=['one', 'two', 'three', 'four'], columns=list('ABC'))
df

# In[32]:


# 与apply不同的是applymap操作作用的是dataframe中的每一个元素
# formatter = lambda x: '%.03f' % x
formatter = '{0:.03f}'.format
df.applymap(formatter)

# In[40]:


# 排序与排名
df = pd.DataFrame(np.random.randint(1, 10, (4, 3)), columns=['one', 'two', 'three'], index=list('ABCD'))
# 按值排序
df.sort_values(by='one', ascending=False)

# In[41]:


# 排名
s = pd.Series([3, 6, 2, 6, 4])
# rank 相同名次用均值表示
s.rank()
# 默认method为均值
# df.rank(method='average')


# In[42]:


# 指定排名first方法,表示相同名次时候第一个出现的为前一名
s.rank(method='first')

# In[43]:


df

# In[46]:


# dataFrame排名,结果中的数值为名次
df.rank(method='first')

# In[47]:


# 数据的唯一性
# 创建一下索引
s = pd.Series(list('abbcdabacad'))
s

# In[48]:


# value_counts统计次数
s.value_counts()

# In[49]:


# unique为去重
s.unique()

# In[51]:


# 序列中是否为指定值其中之一
s.isin(['a', 'b', 'c'])


# In[ ]:
