#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[30]:


df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\prodigy intern\task1\API_SP.POP.TOTL_DS2_en_csv_v2_5607187.csv')


# In[31]:


df


# In[34]:


df.head()


# In[33]:


df.tail()


# In[35]:


df.shape


# In[36]:


df.columns


# In[37]:


df.dtypes


# In[38]:


df.info()


# In[39]:


df.describe()


# In[40]:


df.duplicated().sum()


# In[41]:


df.isna().sum().any()


# In[42]:


df = df.fillna(method = "ffill")
df.head()


# In[43]:


df.isna().sum().any()


# In[44]:


df['Country Name'].unique()


# In[45]:


df['Country Code'].unique()


# In[46]:


df['Indicator Name'].unique()


# In[47]:


df['Indicator Code'].unique()


# In[48]:


df.drop(['Indicator Name','Indicator Code','Country Code'],axis = 1, inplace = True)


# In[49]:


df.columns


# In[50]:


cols = ['1960', '1961', '1962', '1963', '1964', '1965', '1966',
       '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984',
       '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
       '1994', '1995', '1996', '1997', '1998', '1999', '2000','2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020', '2021', '2022']


# In[51]:


for i in cols:
        fig = plt.figure(figsize=(5,5))
        plt.hist(df[i],color='#B22222',bins=10)
        plt.xlabel(i)
        plt.show()


# In[ ]:




