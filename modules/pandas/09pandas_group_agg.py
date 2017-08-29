# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# In[2]:


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
				   'key2': ['one', 'two', 'one', 'two', 'one'],
				   'data1': np.random.randint(1, 10, 5),
				   'data2': np.random.randint(1, 10, 5)})
df

# In[6]:


# 选取data1列,按key1索引分组,求平均值
df['data1'].groupby(df['key1']).mean()

# In[7]:


# 可以自己指定key然后group
key = [1, 2, 1, 1, 2]
df['data1'].groupby(key).mean()

# In[10]:


# 可以选取两组列进行goup,生成的是多层索引的Series
df['data1'].groupby([df['key1'], df['key2']]).sum()

# In[11]:


# 直接按索引key1分组,key2会丢掉,生成的是一个DataFrame
df.groupby('key1').sum()

# In[12]:


# 可以根据上面的结果直接选取列
df.groupby('key1').sum()['data1']

# In[15]:


# goup制定两个行索引,同样生成的是两层索引的dataFrame
mean = df.groupby(['key1', 'key2']).mean()['data1']
mean

# In[16]:


# 以上数据类型为array,可以通过unstack生成dataframe
mean.unstack()

# In[17]:


# pandas的groupby是支持python的迭代器协议的,即一下方式:
for name, group in df.groupby('key1'):
	print name
	print group

# In[18]:


# 因为groupby支持迭代器协议,所以可以直接把返回值转换为列表字典
dict(list(df.groupby('key1')))

# In[19]:


# 以上字典的a元素:
dict(list(df.groupby('key1')))['a']

# In[20]:


# DataFrame可以按列分组
# 比如我们按df的列的类型分组
df.dtypes

# In[21]:


# 按列分组需要制定坐标轴
df.groupby(df.dtypes, axis=1).sum()

# In[22]:


# 其他分组方式
# 建立一下DataFrame
df = pd.DataFrame(np.random.randint(1, 10, (5, 5)),
				  columns=['a', 'b', 'c', 'd', 'e'],
				  index=['Alice', 'Bob', 'Candy', 'Dark', 'Emily'])
# 故意df的第二行第2到第4列为NaN,观察对df非数字的处理
df.ix[1, 1:3] = np.NaN
df

# In[26]:


# 创建一个如下的dict,使df可以根据字典mapping的映射关系进行分组
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'orange', 'e': 'blue'}
# 由于字典是按列进行分组的,这里制定axis为1
grouped = df.groupby(mapping, axis=1)

# In[27]:


# 对group求和可以看到一下结果,这里发现NaN的值默认按0处理了
grouped.sum()

# In[28]:


# size可以查看分组的列数
grouped.size()

# In[29]:


# count查看每行在改组中的个数
grouped.count()

# In[30]:


# 通过函数进行分组
# 创建一下DataFrame
df = pd.DataFrame(np.random.randint(1, 10, (5, 5)),
				  columns=['a', 'b', 'c', 'd', 'e'],
				  index=['Alice', 'Bob', 'Candy', 'Dark', 'Emily'])
df


# In[31]:


# 定义一个函数,作为分组计算的参数,分组时是根据该函数的返回值进行分组
# groupby参数函数会接收一个索引参数
def _group_key(idx):
	print idx
	return idx


# 那么分组会按行的index分组
df.groupby(_group_key)

# In[32]:


# size可以看到每个组中只有1行
df.groupby(_group_key).size()


# In[33]:


# 那么我们对函数做一个修改
def _group_key(idx):
	print idx
	return len(idx)


df.groupby(_group_key).size()

# In[34]:


# 上面函数其实可以通过len直接表示:
df.groupby(len).size()

# In[35]:


# 多级索引的分组情况
# 创建一下多级索引的DataFrame
columns = pd.MultiIndex.from_arrays([['China', 'USA', 'China', 'USA', 'China'], ['A', 'A', 'B', 'C', 'B']],
									names=['country', 'index'])
df = pd.DataFrame(np.random.randint(1, 10, (5, 5)), columns=columns)
df

# In[36]:


# 根据一级索引country进行分组
df.groupby(level='country', axis=1).sum()

# In[37]:


# 根据二级索引index分组
df.groupby(level='index', axis=1).sum()

# In[39]:


# Pandas的聚合
# 先创建一下DataFrame
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
				   'key2': ['one', 'two', 'one', 'two', 'one'],
				   'data1': np.random.randint(1, 10, 5),
				   'data2': np.random.randint(1, 10, 5)})
df

# In[40]:


# 常用的内置聚合函数
# 根据key1进行分组,求和sum
df.groupby('key1').sum()

# In[42]:


# 平均值聚合
df.groupby('key1').mean()

# In[43]:


# 最小值
df.groupby('key1').min()

# In[44]:


# 最大值
df.groupby('key1').max()

# In[45]:


# 描述
df.groupby('key1').describe()

# In[46]:


# 自定义聚合函数
grouped = df.groupby('key1')


# In[47]:


# 定义聚合函数返回列中最大与最小值的差
def peak_range(s):
	print type(s)
	return s.max() - s.min()


grouped.agg(peak_range)

# In[49]:


# 一次性应用多个聚合函数
grouped.agg(['std', 'mean', 'sum', peak_range])

# In[50]:


# 对于自定义的函数返回的df列名可以用元祖方式如下:
grouped.agg(['std', 'mean', 'sum', ('range', peak_range)])

# In[52]:


# 对不同的列运用不同的聚合函数
# 需要运用到字典
d = {'data1': ['mean', ('range', peak_range)], 'data2': 'sum'}
grouped.agg(d)

# In[53]:


# 对于group.agg返回的行索引可通过reset_index修改
grouped.agg(d).reset_index()

# In[54]:


# 当然对于不把index作为索引,可以通过group时候强制设置:
df.groupby('key1', as_index=False).agg(d)

# In[55]:


# DataFrame高级
# 对于一下df要求讲聚合后的值追加为一个新的列,在每一行后,那么先使用传统的方式实现:
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
				   'key2': ['one', 'two', 'one', 'two', 'one'],
				   'data1': np.random.randint(1, 10, 5),
				   'data2': np.random.randint(1, 10, 5)})
df

# In[57]:


# 先进行聚合并修改列名称
k1_mean = df.groupby('key1').mean().add_prefix('mean_')
k1_mean

# In[58]:


# 通过merge函数合并完成追加聚合数据
pd.merge(df, k1_mean, left_on='key1', right_index=True)

# In[60]:


# DataFrame可以通过一个简单的操作 transform 完成以上需求
k1_mean = df.groupby('key1').transform(np.mean).add_prefix('mean_')
k1_mean

# In[61]:


# 然后通过添加列方式完成操作
df[k1_mean.columns] = k1_mean
df

# In[63]:


# 例子,通过自定义函数调用transform
# 定义一下df
df = pd.DataFrame(np.random.randint(1, 10, (5, 5)),
				  columns=['a', 'b', 'c', 'd', 'e'],
				  index=['Alice', 'Bob', 'Candy', 'Dark', 'Emily'])
df


# In[66]:


# 定义函数返回数据与均值的差
def demean(s):
	return s - s.mean()


key = ['one', 'one', 'two', 'one', 'two']
demeaned = df.groupby(key).transform(demean)
demeaned

# In[67]:


# 可以通过讲以上结果数据求均值为0进行验证
demeaned.groupby(key).mean()

# In[68]:


# 分组apply方法的使用
# 先定义一个df
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
				   'key2': ['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
				   'data1': np.random.randint(1, 10, 10),
				   'data2': np.random.randint(1, 10, 10)})
df


# In[69]:


# 定义聚合函数,默认按data1列分组,按该列降序排列,输出前n行
def top(g, n=2, column='data1'):
	return g.sort_values(by=column, ascending=False)[:n]


top(df)

# In[70]:


# 通过分组运算后,在通过top处理,就使用到了apply()函数
df.groupby('key1').apply(top)

# In[71]:


# apply中的参数可以传递运算函数(如这里的top参数n和column)
df.groupby('key1').apply(top, n=3, column='data2')

# In[74]:


# 分组运算简单案例:

# 构建的数据过程:
states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'Califormia', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
data
# 在East和West两个组中,出现了NaN的数据,要求把NaN的数据用各组中的均值替代


# In[75]:


# 处理方案:使用apply函数解决
# 先得East和West的均值
data.groupby(group_key).mean()

# In[79]:


# 实际上可以通过apply一次完成
data.groupby(group_key).apply(lambda g: g.fillna(g.mean()))


# In[ ]:
