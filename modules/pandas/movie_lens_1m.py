
# coding: utf-8

# In[1]:


# 导入pandas
import pandas as pd


# In[4]:


# 读取users.dat数据,并且表示出列索引
unames = ['user_id','gender','age','occupation','zip']
# 由于jupyter notebook 启动的目录为ml-1m的目录,这里读取相对位置如下:
users = pd.read_table('ml-1m/users.dat',sep='::',header=None,names=unames)


# In[5]:


# 统计总量
print len(users)
# 查看前几条数据
users.head(5)


# In[6]:


# 用相同的方法导入电影和评分数据
rating_names = ['user_id','movie_id','rating','timestamps']
ratings = pd.read_table('ml-1m/ratings.dat',sep='::',header=None,names=rating_names)

movie_names = ['movie_id','title','genres']
movies = pd.read_table('ml-1m/movies.dat',sep='::',header=None,names=movie_names)


# In[8]:


# 查看评分数据
print len(ratings)
ratings.head(5)


# In[9]:


# 查看电影数据
print len(movies)
movies.head(5)


# In[10]:


# 接下来讲三个表合并起来
data = pd.merge(pd.merge(users,ratings),movies)
# 查看下合并数据
print len(data)
data.head(10)
# 可以看到合并后的数据是通过join关联操作形成的,users和ratings以user_id关联,然后在与movies的movie_id关联


# In[12]:


# 查看下user_id为1的数据
data[data.user_id==1]


# In[14]:


# 通过数据透视,分别查看一下不同性别的评分
# 透视的数据为ratings,行索引应该为电影title,类索引应该为性别gender,这里使用平均值透视
ratings_by_gender = data.pivot_table(values='rating',index='title',columns='gender',aggfunc='mean')
ratings_by_gender.head(10)


# In[15]:


# 为了查看不同性别评分的差距大小,这里对ratings_by_gender添加一个列,diff
ratings_by_gender['diff'] = ratings_by_gender.F - ratings_by_gender.M


# In[16]:


ratings_by_gender.head(10)


# In[17]:


# 找出差距最大的10部电影,升序
ratings_by_gender.sort_values(by='diff',ascending=True).head(10)


# In[18]:


# 找出差距最大的10部电影,降序
ratings_by_gender.sort_values(by='diff',ascending=False).head(10)


# In[19]:


# 查看那个电影评分最多
ratings_by_title = data.groupby('title').size()
ratings_by_title.head(10)


# In[20]:


# 降序排列
ratings_by_title.sort_values(ascending=False).head(10)


# In[21]:


# 计算每部电影的平均得分
mean_ratings = data.pivot_table(values='rating',index='title',aggfunc='mean')
mean_ratings.head(10)


# In[22]:


# 降序排序,前10高的评分
mean_ratings.sort_values(ascending=False).head(20)


# In[24]:


# 从上面看,评分很高的电影有些都没有听说过,这是因为看的人少,但他们给了比较高的评分
# 我们看下10大热门电影的评分
top_10_hot = ratings_by_title.sort_values(ascending=False).head(10)
mean_ratings[top_10_hot.index]


# In[25]:


# 那么前20大高评分电影中,他们的热度是多少呢
top_20_score = mean_ratings.sort_values(ascending=False).head(20)
ratings_by_title[top_20_score.index]
# 从这个数据上可以验证到,评分很高的电影看的人一般很少..


# In[26]:


# 真正的好电影,应该是评分高,看的人也多
# 找到热度足够高的电影,假定评分此时大于1000表示热度高
hot_movies = ratings_by_title[ratings_by_title > 1000]
print len(hot_movies)
hot_movies.head(10)


# In[28]:


# 然后用热度足够高的电影找出评分好的电影
hot_movies_rating = mean_ratings[hot_movies.index]
top_10_good_movies = hot_movies_rating.sort_values(ascending=False).head(10)
top_10_good_movies


# In[ ]:




