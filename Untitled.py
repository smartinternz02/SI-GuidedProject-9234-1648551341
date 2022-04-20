#!/usr/bin/env python
# coding: utf-8

# # Assignment-1

# In[1]:


print(7**4)


# In[2]:


s="Hi there Sam!"
l=s.split()
l[-1]="dad!"
print(l)


# In[3]:


planet="Earth"
diameter=12742
print("The diameter of {} is {} kilometers".format(planet,diameter))


# In[4]:


lst=[1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
print(lst[3][1][2][0])


# In[5]:


d={'k1':[1,2,3,{'tricky':['oh', 'man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# In[6]:


print("Tuples are immutable and values can't be alttered within it and Lists are mutable")


# In[7]:


def domain(a):
    return a.split("@")[-1]
print(domain("user@domain.com"))


# In[8]:


def fun(a):
    return True if "dog" in a else False
print(fun("dog"))


# In[9]:


def fun(a):
    return a.count("dog")
print(fun("dot"))


# In[10]:


def ticket(speed,bod):
    if bod:
        speed-=5
    if speed>80:
        return "Big Ticket"
    elif speed>60:
        return "Small Ticket"
    else:
        return "No Ticket"
print(ticket(70,True))
print(ticket(90,False))


# In[ ]:




