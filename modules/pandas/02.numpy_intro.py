# coding: utf-8

# # numpy 简介

# ## ndarray 数组

# In[1]:


import numpy as np

# ### 一维数组

# In[2]:


data = np.array([1, 2, 4, 5])
data

# In[3]:


data.shape

# In[4]:


data.dtype

# In[5]:


data[0] = 9
data

# ### 二维数组

# In[6]:


data = np.array([[1, 2], [3, 4]])
data

# In[7]:


data[0, 1]

# In[8]:


data.shape

# ### arange

# In[9]:


np.arange(10)

# In[10]:


data = np.arange(1, 10)
data

# ### reshape

# In[11]:


data2 = data.reshape(3, 3)
data2

# In[12]:


data

# In[13]:


data2

# In[14]:


data2[0, 1] = 100

# In[15]:


data2

# In[16]:


data

# ### 其他创建方法

# In[17]:


np.zeros((2, 2))

# In[18]:


a = np.ones((2, 2, 3))
a

# In[19]:


a[0, 1, 2]

# In[20]:


b = np.arange(12).reshape(2, 2, 3)
b

# In[21]:


b[0, 1, 2]

# In[22]:


np.eye(3)

# In[23]:


np.random.randint(1, 10, (3, 3))

# ### 索引

# In[24]:


# 一维数组
data = np.arange(100, step=10)
data

# In[25]:


data[1:5]

# In[26]:


data[4:]

# In[27]:


data[:4]

# In[28]:


# 二维数组
data = np.arange(16).reshape(4, 4)
data

# In[29]:


data[1:3]

# In[30]:


data[1:]

# In[31]:


data[:3]

# In[32]:


data[1:3, 1:3]

# In[33]:


data[:, 1:3]

# In[34]:


data[2:4, :]

# In[35]:


data[2:5]

# ### 数组作为索引

# In[36]:


data = np.arange(16).reshape(4, 4)
data

# In[37]:


data[[0, 2, 3], [1, 2, 3]]

# In[38]:


print data[0, 1], data[2, 2], data[3, 3]

# In[39]:


xidx = np.array([0, 2, 3])
yidx = np.array([1, 2, 3])
data[xidx, yidx]

# In[40]:


# 修改每行里的特定列的数据
yidx = [0, 3, 2, 0]
data[np.arange(4), yidx] += 100
data

# ### bool 索引

# In[41]:


data = np.arange(16).reshape(4, 4)
data

# In[42]:


idx = data >= 10

# In[43]:


idx

# In[44]:


data[idx]

# In[45]:


# 输出是元素线性化后的结果
data[data >= 10]

# In[46]:


# 偶数元素
data[data % 2 == 0]

# ### 数学运算

# In[47]:


x = np.arange(1, 5).reshape(2, 2)
x

# In[48]:


y = np.arange(5, 9).reshape(2, 2)
y

# In[49]:


x + y

# In[50]:


np.add(x, y)

# In[51]:


y - x

# In[52]:


np.subtract(y, x)

# In[53]:


x * y

# In[54]:


x / y

# In[55]:


x = np.array(x, dtype=float)
x

# In[56]:


y = np.array(y, dtype=float)
y

# In[57]:


x / y

# In[58]:


np.sqrt(x)

# In[59]:


x

# In[60]:


x + 10

# ### 矩阵运算

# In[61]:


a = np.array([[2, 4], [3, 7]])
a

# In[62]:


b = np.arange(4).reshape(2, 2)
b

# In[63]:


a.dot(b)

# In[64]:


np.dot(a, b)

# In[65]:


c = np.arange(6).reshape(2, 3)
c

# In[66]:


a.dot(c)

# In[67]:


c.dot(a)

# In[68]:


c.T

# ### 统计功能

# In[69]:


data = np.arange(16).reshape(4, 4)
data

# In[70]:


data.sum()

# In[71]:


data.sum(axis=0)

# In[72]:


data.sum(axis=1)

# ### 几个常用函数

# In[73]:


np.linspace(0, 10, num=51)
