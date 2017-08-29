
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# Pandas方法read_csv可以直接读取csv格式数据
pd.read_csv('ex1.csv')


# In[4]:


# 另外可以通过read_table指定分隔符读取
pd.read_table('ex1.csv',sep=',')


# In[7]:


# read_table比read_csv更灵活,可以通过正则表达式读取
# ex1.csv文件中包含有列名称,那么对与没有列名称的文件读取
pd.read_csv('ex2.csv',header=None,names=['a','b','c','d','message'])


# In[8]:


# 同时可以指定列作为行索引
pd.read_csv('ex2.csv',header=None,names=['a','b','c','d','msg'],index_col='msg')


# In[9]:


# 甚至可以制定多级行索引
pd.read_csv('ex2.csv',header=None,names=['a','b','c','d','msg'],index_col=['msg','b'])


# In[11]:


# 对于不规则的分隔符处理
#一下文件包含1到多个空格分割,通过read_table的正则表达式处理如下:
pd.read_table("ex3.csv",sep='\s+')


# In[13]:


# 缺失值的处理(默认NA和空为缺失值)
# read_csv可以指定特定字符为缺失值
pd.read_csv('ex5.csv',na_values=['NA','NULL','foo'])


# In[14]:


# 同时可以根据特定列的指定特定字符为缺失值
pd.read_csv('ex5.csv',na_values={'message':['NA','NULL','foo'],'someting':['two']})


# In[40]:


#import string
#df1 = pd.DataFrame(np.random.randn(10000,4), columns=['one','two','three','four'])
#df1['key']=pd.DataFrame(np.random.choice(list(string.ascii_uppercase),10000))
#df1.to_csv('ex6.csv',index=False)

# nrows表示读取10行数据
pd.read_csv('ex6.csv',nrows=10)


# In[42]:


# 逐块的处理数据,设定分10块读取
# 一次读取1000行
tr = pd.read_csv('ex6.csv',chunksize=1000)
tr


# In[43]:


# TextFileReader支持迭代器
result = pd.Series([])
for chunk in tr:
    # for循环迭代tr,统计每一块的key中的value个数,然后与之前原有的resut累加
    result = result.add(chunk['key'].value_counts(),fill_value=0)
result


# In[45]:


result = result.sort_values(ascending=False)
result[:10]


# In[46]:


# pandas保存数据
df = pd.read_csv('ex5.csv')
df


# In[48]:


# 通过index = False不写行索引,header=None不指定列名称
df.to_csv('ex5_out.csv',index=False,header=None)


# In[49]:


# 只写特定的列
df.to_csv('ex5_out.csv',index=False,header=None,columns=['b','c',',message'])


# In[50]:


# 可以指定分隔符
df.to_csv('ex5_out.csv',index=False,header=None,columns=['b','c',',message'],sep='|')


# In[ ]:


# 除了文本方式存储,也可以通过二进制方式存储

