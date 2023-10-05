#!/usr/bin/env python
# coding: utf-8

# In[5]:


from matplotlib import pylab
print(pylab.__version__)


# In[3]:


import numpy as np
x=np.linspace(0,10,25)
y=x*x+2
print(x)
print(y)
print(np.array([x,y]).reshape(25,2).reshape(2,25))


# In[6]:


pylab.plot(x,y,'r') # 'r' stands for red


# In[7]:


pylab.plot(x,y,'b') # 'b' stands for blue


# In[8]:


# Drawing a subgraph
pylab.subplot(1,2,1) #The contents of the brackets represents (rows,columns,indexes)
pylab.plot(x,y,'r--') # the 3rd parameter determines color and line style
pylab.subplot(1,2,2)
pylab.plot(x,y,'g*-')


# In[9]:


from matplotlib import pyplot as plt 


# In[10]:


fig=plt.figure()
axis=fig.add_axes([0.5,0.1,0.8,0.8]) #control the left, right,width, height of the canvas(from 0 to 1)
axis.plot(x,y,'r')


# In[12]:


fig,axes=plt.subplots(nrows=1,ncols=2)# submap is of 1 row 2 columns
for ax in axes :
    ax.plot(x,y,'r')


# In[13]:


fig,axes=plt.subplots(nrows=1,ncols=3)# submap is of 1 row 2 columns
for ax in axes :
    ax.plot(x,y,'r')


# In[14]:


fig,axes=plt.subplots(nrows=1,ncols=5)# submap is of 1 row 2 columns
for ax in axes :
    ax.plot(x,y,'r')


# In[15]:


fig,axes=plt.subplots(nrows=3,ncols=1)# submap is of 1 row 2 columns
for ax in axes :
    ax.plot(x,y,'r')


# In[19]:


fig=plt.figure(figsize=(16,9),dpi=300)
axes1=fig.add_axes([0.1,0.1,0.8,0.8]) #big axes
axes2=fig.add_axes([0.2,0.5,0.4,0.3]) #small canvas
axes1.plot(x,y,'r')
axes2.plot(x,y,'g')


# # Matplotlib Library

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y)


# # remove heading

# In[3]:


x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y)
plt.show()


# # Change line color

# In[4]:


x = [1,2,3,4]
y = [5,6,7,8]
c='r'
plt.plot(x,y,c)
plt.show()


# # Use Marker

# In[6]:


x = [1,2,3,4]
y = [5,6,7,8]
c='r'
plt.plot(x,y,c,marker='o')
plt.show()


# # Show different plot

# In[8]:


x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y)
plt.plot(y,marker='>')
plt.show()


# # Bar graph

# In[9]:


x = [1,2,3,4]
y = [5,6,7,8]
plt.bar(x,y)
plt.show()


# # Change bar graph color 

# In[15]:


x = [1,2,3,4]
y = [5,6,7,8]
c = ['r','g','b','y']
plt.bar(x,y, color = c)
plt.show()


# # Horizontal view

# In[16]:


import numpy as np


# In[21]:


x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.barh(x,y,color="red")
plt.show()


# In[22]:


x = ["A","B","C","D"]
y = [5,6,7,8]
plt.barh(x,y,color="purple")
plt.show()


# # change width

# In[23]:


x = [1,2,3,4]
y = [5,6,7,8]
c = ['r','g','b','y']
plt.bar(x,y, color = c, width = 0.5)
plt.show()


# # Change height

# In[24]:


x = ["A","B","C","D"]
y = [5,6,7,8]
plt.barh(x,y,color="purple", height = 0.2)
plt.show()


# # Scatter Plot

# In[26]:


x=[1,2,3,4,5,6]
y=[5,6,7,8,9,2]
plt.title("scatter plot")
plt.scatter(x,y)
plt.show()


# # Adding Label

# In[27]:


x=[1,2,3,4,5,6]
y=[5,6,7,8,9,2]
plt.title("scatter plot")
plt.xlabel("Month")
plt.ylabel("Number")
plt.scatter(x,y)
plt.show()


# # Change Color

# In[29]:


x=[1,2,3,4,5,6]
y=[5,6,7,8,9,2]
plt.title("scatter plot")
plt.xlabel("Month")
plt.ylabel("Number")
c=['red','magenta','green','orange','blue','brown']
plt.scatter(x,y,color=c)
plt.show()


# # Change size

# In[30]:


x=[1,2,3,4,5,6]
y=[5,6,7,8,9,2]
plt.title("scatter plot")
plt.xlabel("Month")
plt.ylabel("Number")
c=['red','magenta','green','orange','blue','brown']
plt.scatter(x,y,color=c, s=150)
plt.show()


# # Add Image

# In[44]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = r'1689921672236.jpg'
image = Image.open(fname).convert('L')
plt.imshow(image, cmap = 'gray')
plt.show()


# # Image Title

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = r'1689921672236.jpg'
image = Image.open(fname).convert('RGB')
plt.imshow(image, cmap = 'gray')
plt.title("Pranali Valve")
plt.show()


# # Xlabel & Ylabel

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = r'1689921672236.jpg'
image = Image.open(fname).convert('RGB')
plt.imshow(image, cmap = 'gray')
plt.title("Pranali Valve")
plt.xlabel("Width")
plt.ylabel("Height")
plt.show()


# # Grid

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = r'1689921672236.jpg'
image = Image.open(fname).convert('RGB')
plt.imshow(image, cmap = 'gray')
plt.title("Pranali Valve")
plt.xlabel("Width")
plt.ylabel("Height")
plt.grid()
plt.show()


# # Pie Chart

# In[7]:


import matplotlib.pyplot as plt


# In[12]:


a=[10,20,30,40]
b=["Java","C++","DBMS","Python"]
plt.pie(a, labels=b)
plt.show()


# # Change color

# In[13]:


a=[10,20,30,40]
b=["Java","C++","DBMS","Python"]
c = ["Yellow","magenta","Brown","aqua"]
plt.pie(a, labels=b, colors = c)
plt.show()


# # legend

# In[14]:


a=[10,20,30,40]
b=["Java","C++","DBMS","Python"]
c = ["Yellow","magenta","Brown","aqua"]
plt.pie(a, labels=b, colors = c)
plt.legend()
plt.show()


# In[ ]:




