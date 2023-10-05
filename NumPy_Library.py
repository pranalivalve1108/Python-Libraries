#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([1,2,3])
a


# In[3]:


a[0]


# In[4]:


a[1]


# In[5]:


import time
import sys


# In[6]:


b=range(1000)
print(sys.getsizeof(5)* len(b))


# In[7]:


c=np.arange(1000)
print(c.size*c.itemsize)


# In[8]:


size=100000


# In[9]:


L1=range(size)
L2=range(size)
A1=np.arange(size)
A2=np.arange(size)


# In[13]:


start=time.time()
result=[(x+y) for x,y in zip(L1,L2)]
result=[(x+y) for x,y in zip(L1,L2)]
print(result)
print("Python list took:", (time.time()-start)*1000)


# In[14]:


start=time.time()
result=A1+A2
print("NumPy array took:", (time.time()-start)*1000)


# In[15]:


a=np.array([[1,2],[3,4],[5,6]])
a


# In[16]:


a.ndim


# In[17]:


a.itemsize


# In[18]:


a.shape


# In[ ]:





# In[2]:


import numpy as np


# In[4]:


arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# # Zero dimension

# In[6]:


arr=np.array(20)
print(arr)
print(type(arr))
print(arr.ndim)


# # one dimension

# In[7]:


arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.ndim)


# # 2 dimension

# In[8]:


arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)


# # 3 dimension

# In[10]:


arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(arr)
print(arr.ndim)


# # 5 dimension

# In[4]:


import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.ndim)


# In[5]:


arr=np.array([[[[[1,2,3,4]]]]])
print(arr)
print(arr.ndim)


# # Slicing in 1D array

# In[1]:


import numpy as np


# In[3]:


arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])


# In[4]:


arr=np.array([1,2,3,4,5,6,7])
print(arr[::2])


# # Slicing in 2D array

# In[6]:


a=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(a[1,1:4])


# In[8]:


a=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(a[0,0:3])


# # checking the data type of array

# In[9]:


a=np.array([1,2,3,4,5])
print(a.dtype)


# In[11]:


a=np.array(["Pranali","Chakuli","Swara"])
print(a.dtype)


# In[12]:


a=np.array([1,2,3,4,5],dtype='S')
print(a)
print(a.dtype)


# # create an array with data types 4 bytes integer

# In[13]:


arr=np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)


# # numpy array shape

# In[17]:


arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)


# In[18]:


arr=np.array([[[1,2,3,4],[5,6,7,8],[1,2,3,4]]])
print(arr.shape)


# # Joining numpy arrays

# In[19]:


# 1D array
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.concatenate((arr1,arr2))
print(arr3)


# In[22]:


# 2D array
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr3=np.concatenate((arr1,arr2), axis=1)
print(arr3)


# In[23]:


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr3=np.concatenate((arr1,arr2), axis=0)
print(arr3)


# # Spliting the array

# In[24]:


# Spliting the array in 3 parts
arr=np.array([1,2,3,4,5,6])
arr1=np.array_split(arr,3)
print(arr1)


# In[25]:


# Spliting the array in 2 parts
arr=np.array([1,2,3,4,5,6])
arr1=np.array_split(arr,2)
print(arr1)


# # ravel & flatten

# In[30]:


m=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
print("Dimension is:",m.ndim)
n=m.ravel()
print(n)
print("New Dimension is:",n.ndim)


# In[31]:


m=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
print("Dimension is:",m.ndim)
n=m.flatten()
print(n)
print("New Dimension is:",n.ndim)


# In[32]:


m=np.array([[[[1,2],[3,4],[5,6]]]])
print(m)
print("Dimension is:",m.ndim)
n=m.flatten()
print(n)
print("New Dimension is:",n.ndim)


# # Unique function

# In[34]:


u=np.array([1,2,1,3,4,5,3,6,7,8,5,4,9,0,2,1,3,7])
print(u)
x=np.unique(u)
print(x)


# In[35]:


# Print index Value
u=np.array([1,2,1,3,4,5,3,6,7,8,5,4,9,0,2,1,3,7])
print(u)
x=np.unique(u,return_index=True)
print(x)


# In[37]:


# Count Repeated
u=np.array([1,2,1,3,4,5,3,6,7,8,5,4,9,0,2,1,3,7])
print(u)
x=np.unique(u,return_index=True,return_counts=True)
print(x)


# # Delete

# In[42]:


d=np.array([1,2,3,4])
a=np.delete(d, [1])
print(a)


# In[43]:


x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
m=np.delete(x, 1, axis=0)
print()
print(m)


# In[3]:


import numpy as np
arr=np.array(10)
print(arr.ndim)


# In[2]:


arr=np.array([1,2,3,4,5,6,7])
print(arr.ndim)


# In[4]:


arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim)


# In[5]:


arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr.ndim)


# In[7]:


arr=np.array([10],ndmin=4)
print(arr)
print(arr.ndim)


# In[8]:


arr=np.array([10],ndmin=5)
print(arr)
print(arr.ndim)


# In[ ]:




