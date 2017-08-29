# coding: utf-8

# In[1]:


get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np

# In[3]:


# 线型图io
# 创建一个时间序列索引的序列
ts = pd.Series(np.random.randn(1000), index=pd.date_range('2000/1/1', periods=1000))
# 统计
ts = ts.cumsum()
# 描述
ts.describe()

# In[4]:


# 画出线型图
ts.plot()

# In[6]:


# 设置参数title
ts.plot(title='cumsum')
# ts.plot(title='cumsum');


# In[7]:


# 设置风格
ts.plot(title='cumsum', style='red')

# In[8]:


# 设置比例
ts.plot(title='cumsum', style='red', figsize=(8, 6))

# In[9]:


# 对于二维数组DataFrame
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.describe()

# In[10]:


# 对二维数据画图,可以根据铭牌识别列名
df.plot()

# In[11]:


# 对每列单独画出子图
df.plot(subplots=True)

# In[12]:


# 对每列单独画出子图,调整比例
df.plot(subplots=True, figsize=(6, 12))

# In[13]:


# 对每列单独画出子图,调整比例,y轴同步
df.plot(subplots=True, figsize=(6, 12), sharey=True)

# In[15]:


# 对数据增加一个递增的id
df['ID'] = np.arange(len(df))
df.describe()

# In[17]:


# 画图指定x轴为id,y轴为A和C列
df.plot(x='ID', y=['A', 'C'])

# In[23]:


# 柱状图
# 创建一下DataFrame,rand随机正数
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
df

# In[24]:


# 先针对一行画柱状图
df.ix[0].plot(kind='bar')

# In[25]:


# 所有行画柱状图
df.plot.bar()

# In[26]:


# 堆叠柱状图
df.plot.bar(stacked=True)

# In[27]:


# 堆叠柱状图,水平方向
df.plot.barh(stacked=True)

# In[28]:


# 直方图
# 创建一个DF
df = pd.DataFrame({'a': np.random.randn(1000) + 1,
				   'b': np.random.randn(1000),
				   'c': np.random.randn(1000) - 1,
				   },
				  columns=['a', 'b', 'c'])
df

# In[29]:


# 选择A列画直方图
# 直方图是一种展示数据频数/率的特殊的柱状图，也就是说，y 轴是频数/率的度量，既可以是频数（计数）也可以是频率（占比）。
df['a'].hist()

# In[30]:


# “hist”方法默认将连续票价划分为 10 个区间，通过设置参数“bins”来设定区间个数（或者说设定直方图的宽度）
df['a'].hist(bins=20)

# In[31]:


# 对所有列单独画直方图,保持x,y轴共用
df.plot.hist(subplots=True, sharex=True, sharey=True)

# In[33]:


# 对所有列单独画直方图 子图,保持x,y轴共用,设置区间个数
df.plot.hist(subplots=True, sharex=True, sharey=True, bins=50)

# In[34]:


# 对所有列话直方图(合并)
df.plot.hist()

# In[35]:


# 上面是没有叠加是被遮挡到的,这里可以设置一个透明值
df.plot.hist(alpha=0.3)

# In[37]:


# 这样重叠的部分显示出来了,然而十分难看,可以设置为叠加视图stacked
df.plot.hist(stacked=True)

# In[38]:


# 和直方图类似，密度图也描述了数据的分布情况，可以看成将直方图区间无限细分后形成的平滑曲线
# 'kde' 表示“kernel density estimate”。
df['a'].plot.kde()

# In[39]:


# 所有列的概率密度图
df.plot.kde()

# In[40]:


# 决定概率密度中心点位置和形状宽窄的两个性质是均值和方差
# 查看所有列的均值
df.mean()

# In[41]:


# 方差
df.std()

# In[42]:


# 散布图
# 在探索变量之间的关系时,可以绘制散点图
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df

# In[43]:


# 对a,b为x,y轴画散布图
# DataFrame 结构的数据并没有相应的绘制散点图的方法，必须使用 matplotlib 的“scatter”函数
df.plot.scatter(x='a', y='b');

# In[44]:


# 在数据量比较大的时候,可以根据散布图分布关注两个变量的相关性
# 例如如下DataFrame
df = pd.DataFrame({'a': np.concatenate([np.random.normal(0, 1, 200), np.random.normal(6, 1, 200)]),
				   'b': np.concatenate([np.random.normal(10, 2, 200), np.random.normal(0, 2, 200)]),
				   'c': np.concatenate([np.random.normal(10, 4, 200), np.random.normal(0, 4, 200)]), })
df

# In[45]:


# 可以通过散布图进行直观的观察a,b变量关系
df.plot.scatter(x='a', y='b');

# In[46]:


# 可以通过散布图进行直观的观察a,c变量关系
df.plot.scatter(x='a', y='c');

# In[47]:


# 可以通过散布图进行直观的观察b,c变量关系
df.plot.scatter(x='b', y='c');

# In[48]:


# 饼状图
s = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
s

# In[49]:


# 默认形状为椭圆形
s.plot.pie()

# In[51]:


# 设置正方形
s.plot.pie(figsize=(6, 6))

# In[52]:


# 显示百分比,设置标签
s.plot.pie(figsize=(6, 6), labels=['AA', 'BB', 'CC', 'DD'], autopct='%0.2f')


# In[ ]:
