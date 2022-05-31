#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("E:/PYTHON/dataset/zomato.csv",encoding="ISO-8859-1")


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.shape


# Observation:- There are 21 diffrent features and 9551 records of customers

# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


# check for missing value
df.isnull().sum()


# In[9]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[10]:


import seaborn as sns
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")


# In[11]:


#importing another dataset of country code
df_country=pd.read_excel("E:/PYTHON/dataset/Country-Code.xlsx")


# In[12]:


df_country.head()


# In[13]:


#Combining 2 dataset
pd.merge(df,df_country)


# In[14]:


final=pd.merge(df,df_country,on="Country Code",how="left")


# In[15]:


final.head()


# In[16]:


final.columns


# In[17]:


# Visualizing a pie chart for customer records per country
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
country_name=final.Country.value_counts().index
country_val=final.Country.value_counts()
plt.pie(country_val,labels=country_name,autopct="%1.2f%%",radius=3)


# Observation:- 1.around 90% of customer records from india
#               
#               2.around 4.5% of customers record from united state

# In[18]:


#Rating analysis
df_rating=final.groupby(['Aggregate rating', 'Rating color','Rating text']).size().reset_index().rename(columns={0:"Rating Count"})


# In[19]:


df_rating.head()


# In[20]:


df_rating.loc[32]


# In[21]:


df_rating.describe()


# observation :-  1. There are 33 diffrent types of rating.
#                 2.  2148 customers did not give ratings.
#                 3. 61 customers gives maximum rating of 4.9 

# In[22]:


# visualization of Aggregate ratings by customers
import matplotlib
matplotlib.rcParams["figure.figsize"]=(12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",hue="Rating color",data=df_rating,palette=['white','red','orange','yellow','green','green']  )


# Observation:- maximum customersgives rating between 2.9 to 3.9

# In[23]:


sns.countplot(x="Rating color",data=df_rating,palette=['white','red','orange','yellow','green','green'])


# In[36]:


#find the country name that have given 0 ratings
final[final['Rating color']=="White"].groupby("Country").size().reset_index()


# # Find top 10 cuisines

# In[39]:


final["Cuisines"].unique()


# In[47]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
cusines_name=final.Cuisines.value_counts().index
cusines_count=final.Cuisines.value_counts()
plt.pie(cusines_count[:10],labels=cusines_name[:10],autopct="%1.2f%%",radius=2)


# In[46]:


cusines_count=final.Cuisines.value_counts()
print(cusines_count[:10])


# In[ ]:




