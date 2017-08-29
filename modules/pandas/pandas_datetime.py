# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# In[2]:


from datetime import datetime
from datetime import timedelta

# In[5]:


# 回顾python的时间模块
now = datetime.now()
now

# In[6]:


now.year, now.month, now.day

# In[7]:


# 创建连个时间,求间隔
date1 = datetime(2016, 4, 20)
date2 = datetime(2016, 4, 16)
delta = date1 - date2
delta

# In[8]:


# 间隔的时间
delta.days

# In[9]:


# 间隔的秒
delta.total_seconds()

# In[10]:


date2 + delta

# In[11]:


# 日期加上一个时间间隔
date2 + timedelta(4.5)

# In[12]:


# 创建一个到分钟的时间
date = datetime(2016, 3, 20, 8, 30)

# In[13]:


# str直接转化时间为str格式,
str(date)

# In[15]:


# 可以通过时间函数strftime制定格式化格式
date.strftime("%Y/%m/%d %H:%M:%S")

# In[16]:


# 从字符串转化为时间格式
datetime.strptime('2016-03-20 09:30', '%Y-%m-%d %H:%M')

# In[18]:


# Pandas的时间序列
dates = [datetime(2016, 3, 1), datetime(2016, 3, 2), datetime(2016, 3, 3), datetime(2016, 3, 4)]
s = pd.Series(np.random.randn(4), index=dates)
s

# In[19]:


# 数据结构:日期索引的类型 DatetimeIndex
type(s.index)

# In[21]:


# 日期索引的元素类型为 Timestamp
type(s.index[0])

# In[22]:


# 生成一个时间序列,周期默认以天为单位
pd.date_range('20160320', '20160330')

# In[25]:


# 可以通过设置周期生成时间序列
pd.date_range('20160320', periods=10)

# In[26]:


# 可以通过设置周期生成时间序列,包含时间的形式
pd.date_range('20160320 16:32:38', periods=10)

# In[27]:


# 如果不需要时间,通过正则化去掉
pd.date_range('20160320 16:32:38', periods=10, normalize=True)

# In[28]:


# 可以通过设置周期生成时间序列,设置单位 (如:M月份,W星期,BM每个月最后一个工作日,4H每4小时)
pd.date_range('20160320', periods=10, freq='M')

# In[4]:


# Period在Pandas中表示时期
p = pd.Period(2010)
p

# In[5]:


# 默认单位年,表示2012年一整年
p + 2

# In[6]:


# 可以设置单位M(频率)
p = pd.Period(2010, freq='M')
p + 2

# In[7]:


# period_range生成一组时期序列,设置periods为时期个数
pd.period_range('2016-01', periods=10, freq='M')

# In[8]:


# 可以通过起始时期和终止时期创建一组时期序列
pd.period_range('2016-01', '2016-12', freq='M')

# In[9]:


# Q表示季度
pd.period_range('2016Q1', periods=10, freq='Q')

# In[10]:


# 时期的转化
a = pd.Period(2016)

# In[11]:


# 转化为以月为单位,默认从时期最后一个被设置的单位时期开始
a.asfreq('M')

# In[12]:


# 可以设置转化的起始时期
a.asfreq('M', how='start')

# In[14]:


# 将小单位转为大单位
p = pd.Period('2016-04', freq='M')
p

# In[15]:


# 转化为年,默认从当前单位时期所在的设置单位时期开始
p.asfreq('A-DEC')

# In[16]:


# 通过A-MAR设置为从当前单位时期所在设置单位时期的后一个时期开始
p.asfreq('A-MAR')

# In[17]:


# 
p = pd.Period('2016Q4', 'Q-JAN')

# In[18]:


#
p.asfreq('M', how='start'), p.asfreq('M', how='end')

# In[19]:


# 获取该季度 倒数第二个工作日 下午4点20分
(p.asfreq('B') - 1).asfreq('T') + 16 * 60 + 20

# In[21]:


# Pandas 重采样
# 高频率-->低频率-->降采样:5分钟股票交易数据转换为日交易数据
# 低频率-->高频率-->升采样:
# 其他重采样: 每周三(W-WED)砖汉为每周五(W-FRI)

# 创建一下时间序列,这里index通过date_range生成实际上是一个时间戳的时间序列
s = pd.Series(np.random.randn(5), index=pd.date_range('2016-04-01', periods=5, freq='M'))
s

# In[22]:


# 将Timestamp时间序列转换为Period时间序列
s.to_period()

# In[24]:


# 创建一下时间序列,周期是以天为单位
ts = pd.Series(np.random.randn(5), index=pd.date_range('2016-12-29', periods=5, freq='D'))
ts

# In[25]:


# 默认转换的单位是以天为单位
ts.to_period()

# In[26]:


# 修改转换单位
pts = ts.to_period(freq='M')
pts

# In[27]:


# 转换后的索引是重复的
pts.index

# In[28]:


# 根据索引进行group
pts.groupby(level=0).sum()

# In[29]:


# 将Period转换为Timestamp的时间序列
# 默认基于时期的起始时间转换,这里经过两次会造成时间精度丢失的情况
pts.to_timestamp()

# In[30]:


# 可以设置Period的终止时间转换为Timestamp
pts.to_timestamp(how='end')

# In[32]:


# 创建时间序列索引的序列,数据为0到50之间共60个,时间序列索引以分钟为单位
ts = pd.Series(np.random.randint(0, 50, 60), index=pd.date_range('2016-04-25 09:30', periods=60, freq='T'))
ts

# In[33]:


# 将序列根据索引重新采样
# 每5分钟采样一次,将5分钟内的数据求和
ts.resample('5min', how='sum')

# In[34]:


# 设置重采样统计显示的时期序列按结束日期显示
ts.resample('5min', how='sum', label='right')

# In[35]:


# 统计 open(开盘)high(最高)low(最低)close(收盘)
ts.resample('5min', how='ohlc')

# In[37]:


# 通过groupby 重采样
ts = pd.Series(np.random.randint(0, 50, 100), index=pd.date_range('2016-03-01', periods=100, freq='D'))
ts

# In[38]:


# 通过月份重采样
# 这里lambda中的参数为索引
ts.groupby(lambda x: x.month).sum()

# In[39]:


# 将时间戳序列转换为时期的序列
# 这里的index是PeriosIndex
ts.groupby(ts.index.to_period('M')).sum()

# In[40]:


# 生成两条数据,索引为timestamp的时间序列,单位为每周五(为时期结束)
df = pd.DataFrame(np.random.randint(1, 50, 2), index=pd.date_range('2016-04-22', periods=2, freq='W-FRI'))
df

# In[41]:


# 如果重采样以天为单位,在不存在的时间戳的值为NaN
df.resample('D')

# In[42]:


# 可以通过fill_method填充空值,ffill为向前插值
df.resample('D', fill_method='ffill')

# In[43]:


# 限制插值填充的取值范围
df.resample('D', fill_method='ffill', limit=3)

# In[44]:


# 转换到每周一时间序列
df.resample('W-MON', fill_method='ffill')

# In[46]:


# 创建时间序列,以月为单位
df = pd.DataFrame(np.random.randint(2, 30, (24, 4)), index=pd.period_range('2015-01', '2016-12', freq='M'),
				  columns=list('ABCD'))
df

# In[47]:


# 重采样以年为单位,A表示 annual(年),DEC为12月份
# 默认降采样的值为均值
df.resample('A-DEC')

# In[48]:


# 可以通过how修改聚合函数
df.resample('A-DEC', how='sum')

# In[49]:


# 通过每年三月份重采样
df.resample('A-MAR', how='sum')

# In[50]:


# 时间日期的升采样
pdf = df.resample('A-DEC', how='mean')
pdf

# In[51]:


# 对pdf以季度来采样
pdf.resample('Q-DEC')

# In[53]:


pdf.resample('Q-DEC', fill_method='ffill')

# In[56]:


# 几个可以下载股票历史数据的网站
# https://cn.investing.com/
# https://finance.yahoo.com/
# 002001.csv
# 这里Date列实际上不是时间日期格式
df = pd.read_csv('002001.csv', index_col='Date')
df

# In[58]:


# 通过设置解析选项,使Pandas尽量解析为对应数据类型
df = pd.read_csv('002001.csv', index_col='Date', parse_dates=True)
df

# In[61]:


type(df.index)

# In[66]:


# 对数据的Adj CLose列进行降采样,以每周三为开始日期,进行ohlc统计
wdf = df['Adj Close'].resample('W-FRI', how='ohlc')
wdf

# In[67]:


# 添加df的交易量采样
wdf['volume'] = df['Volume'].resample('W-FRI', how='sum')
wdf


# In[ ]:
