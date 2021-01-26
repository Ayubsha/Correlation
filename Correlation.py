#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#Reading the csv file as a pandas dataframe
df1=pd.read_csv(r"C:\Users\Abu Ayub\Desktop\BRP\Correlation diagram\long.csv")


# In[3]:


df1.head(2)


# In[4]:


#Checking for dimensions of dataframe
print(df1.shape)


# In[5]:


#Creating a correlation matrix
correlation_mat = df1.corr()


# In[6]:


sns.heatmap(correlation_mat, annot = True)


# In[7]:


#Getting complete list of correlation pairs
corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[8]:


#Getting correlation pairs with correlation values greater that 0.5
strong_pairs = corr_pairs[abs(corr_pairs) > 0.5]

print(strong_pairs)

