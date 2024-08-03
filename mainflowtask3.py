#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[2]:


data=pd.read_csv("C:\householdtask3.csv")


# In[4]:


display(data.head(10))


# In[12]:


#scatter plot with year against own
plt.scatter(data['year'],data['own'])

#Adding title to the plot 
plt.title("Scatter plot")

#setting the x and y label
plt.xlabel("year")
plt.ylabel("own")

#showing the result
plt.show()


# In[8]:


#line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

#Adding title to the plot 
plt.title("Line Chart")

#setting the x and y label
plt.xlabel("year")
plt.ylabel("own")

#showing the result
plt.show()


# In[9]:


#Bar chart or bar plot
plt.bar(data['year'],data['own'])

#Adding title to the plot 
plt.title("Bar Chart")

#setting the x and y label
plt.xlabel("year")
plt.ylabel("own")

#showing the result
plt.show()


# In[10]:


#Histogram
plt.hist(data['income'])

plt.title("histogram")
plt.show()





