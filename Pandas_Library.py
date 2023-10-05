#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#check pandas version
print(pd.__version__)


# # Series create

# In[3]:


# creating a series from a list
arr=[0,1,2,3,4]
s1=pd.Series(arr)
s1


# In[4]:


order=[1,2,3,4,5]
s2=pd.Series(arr,index=order)
s2


# In[5]:


order=['A','B','C','D','E'] #Using characters
s3=pd.Series(arr,index=order)
s3


# In[6]:


import numpy as np
n=np.random.randn(5)#create a random ndarray
n


# In[8]:


#create series from numpy library
import numpy as np
n=np.random.randn(5)#create a random ndarray
order=['A','B','C','D','E']
s3=pd.Series(n,index=order)
s3


# In[9]:


#create series from dictionary
d={'A':1,'B':2,'C':3,'D':4,'E':5}
print(pd.Series(d))


# # Modify series

# In[10]:


print(s1)


# In[13]:


s1.index=['A','B','C','D','E']
s1


# In[14]:


#Slicing
a=s1[:3]
a


# In[15]:


s1[3:]


# In[16]:


s1


# In[17]:


s2


# In[19]:


s4=s1.append(s2)
s4


# In[20]:


s4.drop(1)


# In[21]:


s3


# In[22]:


s4


# # Series Operations

# In[23]:


arr1=[0,1,2,3,4,5,7]
arr2=[6,7,8,9,5]


# In[24]:


s5=pd.Series(arr2)
s5


# In[25]:


s6=pd.Series(arr1)
s6


# In[26]:


s5.add(s6)


# In[27]:


s5.sub(s6)


# In[28]:


s5.mul(s6)


# In[29]:


s5.div(s6)


# In[32]:


print('Median',s6.median())
print('Max',s6.max())
print('Min',s6.min())


# # Dataframe create

# In[46]:


#Creating datafram
data1=[1,2,3,4,'Pranali']
df=pd.DataFrame(data1)
df


# In[47]:


data1=[1,2,3,4,'Pranali']
order=['A','B','C','D','E']
order1=['A']
df=pd.DataFrame(data1,index=order,columns=order1)
df


# In[5]:


import pandas as pd
import numpy as np
dates=pd.date_range('today',periods=6) #Define time sequence as index
num_array=np.random.randn(6,4) #import numpy random array
order=['A','B','C','D'] #Use the table as the column name
df=pd.DataFrame(num_array,index=dates,columns=order)
df


# In[10]:


data={'Name':['Shahu','Om','Shambhu','Pranali','Radha','Swara'],'Age':[7,6,3,20,17,22],'Education':['5th standard','4th standard','Nursery','Graduation','HSC','Under Graduate']}
order=['A','B','C','D','E','F']
df1=pd.DataFrame(data,index=order)
df1


# In[11]:


# Define datatypes of array
df1.dtypes


# In[12]:


# Show first five values
df1.head()


# In[13]:


# Show first two values
df1.head(2)


# In[14]:


# Show first six values
df1.head(6)


# In[16]:


# show last five values
df1.tail()


# In[17]:


# show last three values
df1.tail(3)


# In[19]:


# show index names
df1.index


# In[20]:


# show column names
df1.columns


# In[21]:


# show all the values in an array 
df1.values


# In[22]:


# show statistical data of dataframe
df1.describe()


# In[23]:


# Replace the columnn values with index values
df1.T


# In[24]:


# Sorting in ascending order
df1.sort_values(by='Age')


# In[27]:


df1.sort_values(by='Name')


# In[28]:


#Slicing dataframe
df1[1:3]


# In[29]:


#Slicing dataframe
df1[:3]


# In[30]:


#Slicing dataframe
df1[2:]


# In[31]:


#Sorting in slicing dataframe
df1.sort_values(by='Age')[1:4]


# In[38]:


df1[['Name','Age']]


# In[39]:


#Copy dataframe in another dataframe
df2=df1.copy()
df2


# In[40]:


df2.isnull()


# In[42]:


#Change the existed value
df1.loc['D','Age']=21
df1


# In[43]:


#Find mean value
df1.mean()


# In[44]:


#Find summation
df1['Age'].sum()


# In[45]:


#Find mean value for particular column
df1['Age'].mean()


# In[48]:


#Find minimum value
df1['Age'].min()


# In[49]:


#Find maximum value
df1['Age'].max()


# In[50]:


df1.sum()


# # Operations for Dataframe missing values

# In[51]:


df3=df1.copy()
df3


# In[56]:


df3=df1.copy()
df3.fillna(3)
df3


# # Pandas new code

# In[1]:


import pandas as pd


# # Read CSV file

# In[8]:


df=pd.read_csv("E:\SQL Practice\Sample.csv")


# In[9]:


df


# # Show Top 5 values

# In[10]:


df.head()


# # Show Bottom 5 values

# In[11]:


df.tail()


# # Check Datatype

# In[12]:


df.dtypes


# # Calculate using Describe

# In[13]:


df.describe()


# In[15]:


df[["fname","lname"]]


# In[16]:


df.dtypes == 'object'


# In[17]:


df.dtypes == 'float64'


# In[20]:


df.dtypes == 'int64'


# In[21]:


df[df.dtypes[df.dtypes == 'int64'].index]


# In[22]:


df.head(3)


# In[23]:


df.tail(3)


# In[25]:


# Show Column names
df.columns


# # slicing

# In[26]:


df[['fname']][1:4]


# In[27]:


df[['fname','lname']][1:4]


# In[28]:


df[['fname','lname']][1:8:3] #Print 1 to 8 step by 2


# # Add new column

# In[29]:


df['new_col'] = 0


# In[30]:


df


# In[31]:


df['Pranali'] = 5


# In[32]:


df


# # Add column which u want

# In[34]:


df.insert(loc=3, column='abc', value=0)


# In[35]:


df


# In[36]:


df.insert(loc=4, column='Brand', value='Pranali Valve')


# In[37]:


df


# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("E:\SQL Practice\Sample.csv")


# In[4]:


df


# # Slicing

# In[9]:


a = df['fname'][0:5]


# In[10]:


a


# In[11]:


type(a)


# In[1]:


import pandas as pd


# In[11]:


a=df=pd.read_csv("E:\SQL Practice\Sample.csv")


# In[12]:


a


# In[16]:


l = ['a','b','c','d','e','f','g','h','i','j']
pd.Series(a, index = l)


# In[14]:


a = df['fname'][0:5]


# In[15]:


a


# In[18]:


l1 = ['a','b','c','d','e']
pd.Series(a, index = l1)


# # Remove NaN using list()

# In[20]:


l1 = ['a','b','c','d','e']
pd.Series(list(a), index = l1)


# In[29]:


m1 = pd.Series([10,20,30,40,50],index = [1,2,3,4,5])


# In[30]:


m1


# In[31]:


m2 = pd.Series([100,200,300,400,500],index = [1,2,3,4,5])


# In[32]:


m2


# In[33]:


m3 = pd.concat([m1,m2])


# In[34]:


m3


# In[35]:


m3[1]


# In[36]:


m1*m2


# In[37]:


m1+m2


# In[38]:


df


# # Delete Column

# delete temporary

# In[40]:


# Delete Temporary
df.drop("age", axis = 1)


# Delete Permanent
# 

# In[41]:


df.drop("age", axis = 1, inplace = True)


# In[42]:


df


# In[43]:


df=pd.read_csv("E:\SQL Practice\Sample.csv")


# In[44]:


df


# In[45]:


df.drop(9)


# In[46]:


df.drop(9, inplace = True)


# In[47]:


df


# # Particular column convert to index

# In[48]:


df.set_index('dept')


# In[49]:


df.set_index('dept', inplace = True)


# In[50]:


df


# In[51]:


df.reset_index()


# # Making dataframe from the dictionary

# In[53]:


d = {"key1" :[1,2,3],
     "key2" :[4,5,6],
     "key3" :[7,8,9]
    }


# In[54]:


d


# In[55]:


pd.DataFrame(d)


# In[ ]:





# In[ ]:




