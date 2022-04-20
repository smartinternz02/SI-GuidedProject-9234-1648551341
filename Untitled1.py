#!/usr/bin/env python
# coding: utf-8

# # Assignment-2

# In[1]:


import numpy as np


# In[2]:


arr=np.zeros(10)
print(arr)


# In[3]:


arr=np.ones(10)
print(arr)


# In[4]:


arr=np.ones(10)*5
print(arr)


# In[5]:


arr=np.arange(10,51)
print(arr)


# In[6]:


arr=np.arange(10,51,2)
print(arr)


# In[7]:


arr=np.arange(0,9).reshape(3,3)
print(arr)


# In[8]:


arr=np.eye(3,3)
print(arr)


# In[9]:


arr=np.random.rand(1)
print(arr)


# In[10]:


arr=np.random.rand(1,25)
print(arr)


# In[11]:


arr=np.arange(0.01,1.01,0.01).reshape(10,10)
print(arr)


# In[12]:


arr=np.linspace(0,1,20)
print(arr)


# In[13]:


temp=np.arange(1,26).reshape(5,5)


# In[14]:


print(temp[2:,1:])


# In[15]:


print(temp[3][-1])


# In[16]:


print(temp[:3,1].reshape(3,1))


# In[17]:


print(temp[-1])


# In[18]:


print(temp[-2:])


# In[19]:


print(temp.sum())


# In[20]:


print(temp.std())


# In[21]:


print(temp.sum(axis=0))


# In[ ]:




