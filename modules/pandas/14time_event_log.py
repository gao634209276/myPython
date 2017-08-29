# coding: utf-8

# ## 时间事件日志
# 
# 个人时间统计工具。要点：
# 
# * 使用 dida365.com 来作为 GTD 工具
# * 使用特殊格式记录事件类别和花费的时间，如： “*[探索发现] 体验 iMac 开发环境 [3h]*”
# * 导出数据
# * 分析数据

# ### 读取数据
# 
# 分析并读取数据

# In[1]:


# get_ipython().magic(u'matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

# In[2]:


from matplotlib.font_manager import FontManager
import subprocess


def get_support_chinese_font():
	fm = FontManager()
	mat_fonts = set(f.name for f in fm.ttflist)

	output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
	print '*' * 10, '系统可用的中文字体', '*' * 10
	print output
	zh_fonts = set(f.split(',', 1)[0] for f in output.split('\n'))
	available = mat_fonts & zh_fonts

	print '*' * 10, '可用的中文字体', '*' * 10
	for f in available:
		print f
	return available


# In[3]:


from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# In[4]:


def _date_parser(dstr):
	return pd.Timestamp(dstr).date()


data = pd.read_csv('data/dida365.csv', header=3, index_col='Due Date', parse_dates=True, date_parser=_date_parser)
data.head()

# ### 数据清洗
# 
# * 只关心己完成或己达成的事件，即 `status != 0` 的事件
# * 只需要 `List Name` 和 `Title` 字段

# In[5]:


df = data[data['Status'] != 0].loc[:, ['List Name', 'Title']]
df.head()

# ### 数据解析
# 
# 解析事件类别和和花费的时间

# In[6]:


import re


def parse_tag(value):
	m = re.match(r'^(\[(.*?)\])?.*$', value)
	if m and m.group(2):
		return m.group(2)
	else:
		return '其他'


def parse_duration(value):
	m = re.match(r'^.+?\[(.*?)([hm]?)\]$', value)
	if m:
		dur = 0
		try:
			dur = float(m.group(1))
		except e:
			print('parse duration error: \n%s' % e)
		if m.group(2) == 'm':
			dur = dur / 60.0
		return dur
	else:
		return 0


titles = df['Title']
df['Tag'] = titles.map(parse_tag)
df['Duration'] = titles.map(parse_duration)
df.head()

# In[7]:


df.count()

# In[8]:


start_date = df.index.min().date()
start_date

# In[9]:


end_date = df.index.max().date()
end_date

# ### 数据分析
# 
# #### 时间总览
# 
# 平均每天投资在自己身上的时间是多少？-> *全部时间 / 总天数*

# In[10]:


end_date - start_date

# In[11]:


df['Duration'].sum()

# In[12]:


df['Duration'].sum() / (end_date - start_date).days

# #### 精力分配

# In[13]:


tag_list = df.groupby(['Tag']).sum()
tag_list

# In[14]:


tag_list['Duration'].plot(kind='pie', figsize=(8, 8), fontsize=16, autopct='%1.2f%%')

# #### 专注力
# 
# 长时间学习某项技能的能力

# In[15]:


programming = df[df['Tag'] == '编程']
programming.head()

# In[16]:


programming.resample('m', how='sum').to_period(freq='m').plot(kind='bar', figsize=(8, 8), fontsize=16)

# #### 连续时间的精力分配
# 
# 以时间为横轴，查看精力分配。

# In[17]:


# 为什么不直接使用 df.pivot()? 因为有重复的行索引，如 2016-05-23
date_tags = df.reset_index().groupby(['Due Date', 'Tag']).sum()
date_tags

# In[18]:


# 以 tag 作为列索引
dates = date_tags.reset_index().pivot(index='Due Date', columns='Tag', values='Duration')
dates

# In[19]:


# 补足连续时间，可以看到哪些天没有在学习
full_dates = dates.reindex(pd.date_range(start_date, end_date)).fillna(0)
full_dates

# In[20]:


# 画出柱状图
full_dates.plot(kind='bar', stacked=True, figsize=(16, 8))

# In[21]:


full_dates.resample('m', how='sum').to_period('m').plot(kind='bar', stacked=True, figsize=(8, 8))


# ## 时间事件日志
# 
# 感兴趣的同学可以参阅 https://github.com/kamidox/utils 。
