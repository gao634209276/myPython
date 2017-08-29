# coding: utf-8

# ## 股票数据分析
# 
# 具体详见 https://github.com/kamidox/stock-analysis
# 
# 这里假设数据已经下载下来，并且保存在 yahoo-data 目录下。

# ## 分析波动幅度

# In[1]:


#get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# In[2]:


datadir = 'yahoo-data'
fname = '002001.csv'
data = pd.read_csv(os.path.join(datadir, fname), index_col='Date', parse_dates=True)
data

# In[3]:


## 使用 resample 针对复权收盘价进行重采样
adj_price = data['Adj Close']
adj_price

# In[4]:


resampled = adj_price.resample('m', how='ohlc')
resampled

# In[5]:


(resampled.high - resampled.low) / resampled.low

# ## 增长曲线

# In[6]:


# 600690.ss 000951.sz 002001.sz
stockid = '600690.sz'
stockfile = '600690.csv'

# In[7]:


ds = pd.read_csv(os.path.join('yahoo-data', stockfile), index_col='Date', parse_dates=True)
ds.head()

# In[8]:


adj_price = ds['Adj Close']
adj_price.plot(figsize=(8, 6))

# ### 增长倍数
# 
# #### 最大增长倍数及最大年化复合增长率
# 
# 计算最低价和最高价之间的收盘价比较，以及增长的倍数和年化复全增长率，这个反应的是一个股票最好的情况下的投资收益情况。

# In[9]:


# 最高增长倍数
total_max_growth = adj_price.max() / adj_price.min()
total_max_growth

# In[10]:


# 最大年均复合增长率
min_date = adj_price.argmin()
max_date = adj_price.argmax()
max_growth_per_year = total_max_growth ** (1.0 / (max_date.year - min_date.year))
max_growth_per_year

# ### 当前增长倍数及复合增长率
# 
# 计算上市时的收盘价与当前的收盘价比较，增长的倍数和年化复全增长率。

# In[11]:


# 当前平均增长倍数
total_growth = adj_price.ix[0] / adj_price.ix[-1]
total_growth

# In[12]:


# 年复合增长倍数
old_date = adj_price.index[-1]
now_date = adj_price.index[0]
growth_per_year = total_growth ** (1.0 / (now_date.year - old_date.year))
growth_per_year

# ### 平均年化增长率
# 
# 计算每年的增长率，然后再求平均值。也可以计算每月的增长率，再求平均值，可以看到更短的一些周期变化。

# In[13]:


price_in_years = adj_price.to_period(freq='A').groupby(level=0).first()
price_in_years

# In[14]:


price_in_years.plot(figsize=(8, 6))

# In[15]:


# 这里的关键信息：
# 计算年化收益率时，diff 应该要除以前一年的价格，即在前一年的价格的基础上上涨了多少，而不是在当前年的价格。
diff = price_in_years.diff()
rate_in_years = diff / (price_in_years - diff)
rate_in_years

# In[16]:


rate_in_years.mean()

# In[17]:


rate_in_years.plot(kind='bar', figsize=(8, 6))
X = [0, len(rate_in_years)]
Y = [0, 0]
plt.plot(X, Y, color='red', linestyle='-')


# In[ ]:
