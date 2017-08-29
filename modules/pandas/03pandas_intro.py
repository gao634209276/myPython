# coding: utf-8

# In[2]:


get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[4]:


dates = pd.date_range('20160301', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

# In[6]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1

# In[8]:


df1.loc[dates[1:3], 'E'] = 2
df1

# In[10]:


df1.fillna(value=5)

# In[15]:


pd.isnull(df1).any().any()

# In[18]:


df1.mean()

# In[20]:


df1.mean(axis=1)

# In[23]:


df1.cumsum()

# In[24]:


s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s

# In[26]:


df

# In[27]:


df.sub(s, axis='index')

# In[29]:


df.apply(np.cumsum)

# In[30]:


df.apply(lambda x: x.max() - x.min())


# In[33]:


def _sum(x):
	print(type(x))
	return x.sum()


df.apply(_sum)

# In[40]:


s = pd.Series(np.random.randint(10, 20, size=20))
s

# In[41]:


s.value_counts()

# In[42]:


s.mode()

# In[44]:


df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
df

# In[45]:


df.iloc[:3]

# In[48]:


df.iloc[3:7]

# In[50]:


df.iloc[7:]

# In[52]:


df1 = pd.concat([df.iloc[:3], df.iloc[3:7], df.iloc[7:]])
df1

# In[55]:


(df == df1).all().all()

# In[57]:


left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [4, 5]})

# In[58]:


left

# In[59]:


right

# In[60]:


# select * from left inner join right on left.key = right.key;
pd.merge(left, right, on='key')

# In[68]:


s = pd.Series(np.random.randint(1, 4, size=5), index=list('ABCDE'))
s

# In[70]:


df.append(s, ignore_index=True)

# In[71]:


df

# In[72]:


df = pd.DataFrame({
	'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
	'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
	'C': np.random.randn(8),
	'D': np.random.randn(8)
})
df

# In[73]:


df.groupby('A').sum()

# In[74]:


df.groupby(['A', 'B']).sum()

# In[75]:


df.groupby(['B', 'A']).sum()


# In[ ]:
