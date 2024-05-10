#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\prodigy intern\task1\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_251119.csv')


# In[4]:


# Check for missing values
print(df.isnull().sum())

# Encoding categorical variables using get_dummies for simplicity
df_encoded = pd.get_dummies(df, drop_first=True)


# In[5]:


df_encoded.columns


# In[7]:


df


# In[8]:


gender_counts = df['Region'].value_counts()
bar_width = 0.9
x=range(len(gender_counts.index))


plt.bar(gender_counts.index,gender_counts.values)
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Distribution of Region')


plt.xticks(x,gender_counts.index,rotation=45)
plt.tight_layout()
plt.show()


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


df.isnull().sum()


# In[13]:


df.info()


# In[ ]:




