#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plotly


# # Matplotlib

# In[1]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [7,2,4,5,3,1,2,7,8,9]


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


plt.plot(x,y, color='r')
plt.title("Line graph")
plt.show()


# # Seaborn

# In[6]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [7,2,4,5,3,1,2,7,8,9]


# In[7]:


import seaborn as sns


# In[8]:


fig = sns.lineplot(x = x, y = y, color='red')
plt.show()


# # Plotly

# In[9]:


import plotly.express as px


# In[10]:


fig=px.line(x=x, y=y, title="Line graph")
fig.show()


# In[11]:


import plotly.graph_objects as go


# In[12]:


fig = go.Figure(go.Scatter(x=x,y=y))


# In[13]:


fig.show()


# # Adding titles

# In[14]:


fig = go.Figure(go.Scatter(x=x, y=y))
fig.update_layout(title = "Line Graph", xaxis_title = "This is X axis", yaxis_title = "This is Y axis")
fig.show()


# In[15]:


x1, y1 = [1,2,3,4,5], [5,4,6,7,3]
x2, y2 = [1,2,3,4,5], [4,3,6,2,1]
x3, y3 = [1,2,3,4,5], [8,6,8,2,6]


# In[16]:


fig = go.Figure()


# In[17]:


fig.add_trace(go.Scatter(x=x1, y=y1))
fig.add_trace(go.Scatter(x=x2, y=y2))
fig.add_trace(go.Scatter(x=x3, y=y3))


# In[18]:


fig = go.Figure()


# In[19]:


fig.add_trace(go.Scatter(x=x1, y=y1, name="line1", mode="lines"))
fig.add_trace(go.Scatter(x=x2, y=y2, name="line2", mode="markers"))
fig.add_trace(go.Scatter(x=x3, y=y3, name="line3", mode="lines+markers"))


# # Bubble Chart

# In[20]:


import plotly.graph_objects as go


# In[21]:


x = [1,2,3,4]
y = [5,6,7,8]


# In[22]:


fig=go.Figure(go.Scatter(x=x, y=y, mode='markers'))
fig.show()


# # Increase Marker size

# In[23]:


fig=go.Figure(go.Scatter(x=x, y=y, mode='markers', marker_size= [40,20,30,50]))
fig.show()


# # Show Title

# In[24]:


fig=go.Figure(go.Scatter(x=x, y=y, mode='markers', marker_size= [40,20,30,50], text=["Product A","Product B","Product C","Product D"]))
fig.show()


# In[ ]:




