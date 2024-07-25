#!/usr/bin/env python
# coding: utf-8

# list Operation

# In[10]:


mylst = [1,2,[10,11]]


# In[11]:


print(mylst[2][0])


# Distionary data access

# In[12]:


d={'k1':{'innerkey':[1,2,3]}}


# In[13]:


print(d['k1'])


# In[14]:


print(d['k1']['innerkey'][1])


# Tupple's operation

# In[15]:


t = (1,2,3)


# In[16]:


t[0]


# In[17]:


t[0] = 14


# Set property

# In[18]:


s = {1,1,2,3,4,2}


# In[19]:


s


# In[20]:


print(s)


# In[21]:


s.add(5)


# In[22]:


s


# Loops

# In[23]:


my_list = [1,2,3]


# In[24]:


for var in my_list:
    print(var)


# In[25]:


a = [1,2,3]
b = [3,4,5]


# In[53]:


for vara in a:
    for varb in b:
        print (vara)
        print (varb)


# In[55]:


i=0
while i<=15:
    print(i)
    i = i+1


# In[61]:


print(len(s))


# In[63]:


print(len(t))


# In[64]:


string = "hi my name is Dhaval"


# In[65]:


print(len(string))


# Functions

# In[70]:


def my_function(name):
    print("my Name is "+ name)
my_function("Dhaval")


# In[71]:


my_function("ABC")


# In[111]:


def sum(a,b):
    c=a+b
    print(c)
sum(5,5)


# Lambda function

# In[83]:


t= lambda x : x*2


# In[84]:


t(2)


# In[110]:


t1= lambda x,a,b,c: x=a+b+c


# In[86]:


t1(5,4,6,3)


# In[115]:


t2= lambda a,b,c: a+b+c


# In[116]:


t2(8,9,45)


# Map

# In[105]:


maplst=[1,2,3]


# Filter

# In[108]:


myfltlst =[2,3,4,5]
list(filter(lambda num:num%2==0,myfltlst))

