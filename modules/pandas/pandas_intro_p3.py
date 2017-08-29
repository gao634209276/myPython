# coding: utf-8

# In[1]:


# 设置为 inline 风格
# get_ipython().magic(u'matplotlib inline')
# 包导入
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[7]:


tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
					['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
tuples

# In[8]:


# 对tuple创建多索引,first对应tuple的key,second对应value
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index

# In[10]:


# 随机产生8行2列数据,使用有tuple产生的二级索引
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df

# In[12]:


# 列索引转换为行索引,此时A,B转换为第三层索引,把原来8x2转换为16x1
stacked = df.stack()
stacked

# In[14]:


# unstack()可以重新转换回去,如果再次调用,会把第二层索引转换为列索引
stacked.unstack().unstack()

# In[15]:


df = pd.DataFrame({
	'A': ['one', 'one', 'two', 'three'] * 3,
	'B': ['A', 'B', 'C'] * 4,
	'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
	'D': np.random.randn(12),
	'E': np.random.randn(12)
})
df

# In[16]:


# 数据透视,即只看其中一部分数,比如以A,B为行索引,C为列索引,查看D的数据分布
df.pivot_table(values=['D'], index=['A', 'B'], columns=['C'])
# 通过A,B,C三个维度透视D,可以发现表格中部分为NaN


# In[17]:


# 在举个例子,我们以A为行索引,C为列索引,透视 E 的数据
df.pivot_table(values=['E'], index=['A'], columns=['C'])

# In[22]:


# 那么上面的数据到底是如何得到的呢,拿上面透视表A=one,C=bar的E,
# 我们先在df中过滤出A中为one的数据,然后对C分组算平均值
df[df.A == 'one'].groupby('C').mean()

# In[24]:


# pandas提供了非常强大的时间处理函数
# 通过date_range创建600组单位到s的时间序列
rng = pd.date_range('20160301', periods=600, freq='s')
rng

# In[26]:


# 创建从0到500长度为600的序列,索引为时间序列rng
s = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
s

# In[27]:


# resample重新采样,间隔为2分钟,并进行求和
s.resample('2Min', how='sum')
# s.resample('2Min',how='mean') # 求平均值


# In[29]:


# period_range,Q表示季度
rng = pd.period_range('2000Q1', '2016Q1', freq='Q')
rng

# In[31]:


# to_timestamp 转换为日期的格式
rng.to_timestamp()

# In[32]:


pd.Timestamp('20160301') - pd.Timestamp('20160201')

# In[33]:


pd.Timestamp('20160301') + pd.Timedelta(days=5)

# In[36]:


# 类别数据
# 如下一只学生信息数据
df = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6],
				   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'd']})
df

# In[39]:


# 对df添加一个类别 category
df['grade'] = df.raw_grade.astype('category')
df

# In[40]:


# grade的数据类型是: 类别category
df.grade

# In[41]:


# 查看grade的类别种类
df.grade.cat.categories

# In[42]:


# 把对应的三种类别重命名
df.grade.cat.categories = ['very good', 'good', 'bad']
df

# In[43]:


# 根据grade进行排序
df.sort_values(by='grade', ascending=True)

# In[49]:


# pandas 另一个强大的功能是直接可以对数据进行可视化
# 创建一组随机数,长度为1000,以时间序列为索引,从20000年1月1日
s = pd.Series(np.random.randn(1000), index=pd.date_range('20000101', periods=1000))
s

# In[46]:


# 对数据求和
s = s.cumsum()
s

# In[48]:


# 使用plot()划出数据
s.plot()

# In[50]:


# pandas 可以对数据进行读写,从磁盘中读取和保存数据到磁盘
# 创建100行4列的随机数的DataFrame,列索引为ABCD
df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df

# In[52]:


# 把数据保存的磁盘
df.to_csv('data.csv')
# et_ipython().magic(u'ls')

# In[53]:


# get_ipython().magic(u'less data.csv')

# In[54]:


# 从磁盘中读取数据,索引默认自动添加,这里由于保存的数据中包含索引列,这里在参数中制定索引列
pd.read_csv('data.csv', index_col=0)


# In[ ]:
