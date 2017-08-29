
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[3]:


# 查看一下Series索引
s = pd.Series(np.random.randn(5),index=list('abcde'))
s.index


# In[4]:


# 索引的属性name
s.index.name = 'alpha'
s


# In[5]:


# DataFrame是索引分为行索引和列索引
df = pd.DataFrame(np.random.randn(4,3),columns=['one','two','three'])
# 行索引
df.index


# In[6]:


# 列索引
df.columns


# In[8]:


# 行索引和列索引的name属性
df.index.name = 'row'
df.columns.name = 'col'
df


# In[9]:


# 重复的索引
s = pd.Series(np.arange(6),index=list('abdbda'))
s


# In[10]:


# 在获取a索引的值时候
s['a']


# In[11]:


# 判断索引是否是唯一的
s.index.is_unique


# In[12]:


# 返回索引的唯一
s.index.unique()


# In[13]:


# 重复索引的处理,可以用groupby,聚合处理可以如mean,avage等
s.groupby(s.index).sum()


# In[29]:


# 多级索引可以把高纬度的数据用二维数据表示,多级索引的创建如下:
a = [['a','a','a','b','b','b','c','c','c'],[1,2,3,1,2,3,1,2,3]]
# zip把a内部的两个list组装为tuple的list
t = list(zip(*a))
t


# In[30]:


# 通过以上元祖构成的list可以构建一个多级索引
index = pd.MultiIndex.from_tuples(t, names=['level1','vevel2'])
index


# In[33]:


# 通过以上的多级索引创建一个多级索引的序列
s = pd.Series(np.random.randn(9),index=index)
s


# In[34]:


# 选取一级索引
s['b']


# In[35]:


# 一级索引切片多选
s['b':'c']


# In[36]:


# 一级索引通过列表选取
s[['a','c']]


# In[37]:


# 二级索引选取
s[:,2]


# In[6]:


# 创建一个复制的索引
df = pd.DataFrame(np.random.randint(1,10,(4,3)),
                 index=[['a','a','b','b'],[1,2,1,2]],
                 columns=[['one','one','two'],['blue','red','blue']])
df.index.names = ['row-1','row-2']
df.columns.name = ['col-1','col-2']
df


# In[5]:


# 行,列二级索引,选取
df.loc['a']


# In[7]:


# 选取行索引a的数据,类型是DataFrame
type(df.loc['a'])


# In[8]:


# 选取第二级索引
df.loc['a',1].index


# In[9]:


df.loc['a',1]


# In[11]:


# 索引的交换
df2 = df.swaplevel('row-1','row-2')
df2


# In[12]:


df


# In[13]:


# 可以对索引排序,0表示一级索引
df2.sortlevel(0)


# In[14]:


df2.sortlevel(1)


# In[15]:


# dataFrame求和,level=0指根据一级索引求和
df.sum(level=0)


# In[16]:


df.sum(level=1)


# In[17]:


# 把列数据转换为索引数据
df = pd.DataFrame({
    'a': range(7),
    'b': range(7,0,-1),
    'c': ['one','one','one','two','two','two','two'],
    'd': [0,1,2,0,1,2,3]
})
df


# In[19]:


# 把c列作为索引
df.set_index('c')


# In[21]:


# 把c,d数额为二级索引
df2 = df.set_index(['c','d'])


# In[22]:


# reset_index会转换回来索引
df2.reset_index()


# In[23]:


# 可以对索引排序
df2.reset_index().sort_index('columns')


# In[ ]:




