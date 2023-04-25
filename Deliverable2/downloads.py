#!/usr/bin/env python
# coding: utf-8

# ## Data Understanding

# In[1]:


#importing libraries
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import boto3

from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


# In[2]:


#pd.options.display.max_columns = None
pd.set_option('display.max_columns', None)


# In[3]:


s3_csv_path = f's3://group5-porter-delivery-estimation/data/dataset.csv'

df = pd.read_csv(s3_csv_path)


# In[4]:


#Information of the data
print(df.info())


# In[5]:


#First 3 rows of table

df.loc[:df.index[2]]


# In[6]:


#year,month and day for 'created_at'

df[['year', 'month', 'day']] = df['created_at'].str.split('-', expand=True)
df['day'] = df['day'].str.split(' ', expand=True)[0]
df[['year', 'month', 'day']] = df[['year', 'month', 'day']].astype(int)



# In[7]:


#created_at & actual_delivery_time into date_time format conversion
df['created_at'] = pd.to_datetime(df['created_at'])
df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])


# In[8]:


#feature'time_taken(mins)' created to store the time taken for delivery in minutes
df['time_taken(mins)'] = (df['actual_delivery_time'] - df['created_at']).astype('timedelta64[m]')


# In[9]:


#created_at and actual_deivery_time dropping
df = df.drop(columns=['created_at', 'actual_delivery_time'])


# In[10]:


#make a copy for exploration
df_=df.copy()


# ### Exploratory Data Analysis

# In[11]:


#missing values percentage in each category
percent_missing = df_.isnull().sum() * 100 / len(df_)
missing_value_df = pd.DataFrame({'%age of missing value': percent_missing})
missing_value_df.index.name = 'feature'
missing_value_df = missing_value_df.reset_index()


# In[12]:


#categorical and numerical features splitting
categorical_feature = []
numerical_feature = []

for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype == 'category':
        categorical_feature.append(col)
    else:
        numerical_feature.append(col)


# In[13]:


# total number of order from each market
store_count = df_.groupby('market_id')['store_id'].count()
plt.bar(store_count.index, store_count.values, color='yellow')
plt.xlabel('Market ID')
plt.ylabel('Store Count')
plt.title('Store Count by Market ID')
plt.show()


# In[14]:


#Analysing what was the frequency of orders in each month and in year 2014 and 2015
df_['month']=df_['month'].map({1:'jan',2:'feb',3:'oct'})
fig=plt.figure(figsize=(20,5))
ax=[None for _ in range(2)]
ax[0]=plt.subplot2grid((1,2),(0,0))
ax[1]=plt.subplot2grid((1,2),(0,1))
sns.set_style('darkgrid')
sns.countplot(x='month',data=df_,palette='Set2',ax=ax[0])
sns.countplot(x='year',data=df_,palette='Set2',ax=ax[1])


# In[15]:


#ways in which different orders are placed(i.e., order protocol with most number of orders)
sns.catplot(x='order_protocol', kind='count', data=df_, palette='Greens')


# In[16]:


#top 20 i.e., most ordered category
fig, ax = plt.subplots(figsize=(20, 8))
df_['store_primary_category'].value_counts().sort_values(ascending=False)[:20].plot(kind='bar', ax=ax, color='purple')
ax.set_xlabel('Store Primary Category', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Top 20 Store Primary Categories', fontsize=18)
plt.show()



# In[17]:


#Analysis of the numerical features 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 8))
sns.boxplot(x='total_items', data=df_, palette='Set2', ax=axes[0, 0])
sns.boxplot(x='subtotal', data=df_, palette='Set2', ax=axes[0, 1])
sns.boxplot(x='min_item_price', data=df_, palette='Set2', ax=axes[1, 0])
sns.boxplot(x='max_item_price', data=df_, palette='Set2', ax=axes[1, 1])



# In[18]:


#fig=plt.figure(figsize=(20,8))
ax=[None for _ in range(4)]
ax[0]=plt.subplot2grid((2,2),(0,0))
ax[1]=plt.subplot2grid((2,2),(0,1))
ax[2]=plt.subplot2grid((2,2),(1,0))
ax[3]=plt.subplot2grid((2,2),(1,1))
sns.boxplot(x='time_taken(mins)',data=df_,palette='PuBu',ax=ax[0])
sns.boxplot(x='total_outstanding_orders',data=df_,palette='YlGnBu',ax=ax[1])
sns.boxplot(x='num_distinct_items',data=df_,palette='Oranges',ax=ax[2])
sns.boxplot(x='total_onshift_partners',data=df_,palette='Reds',ax=ax[3])



# In[19]:


#bivariate analysis: to see how the other features are correlated with delivery time 'time_taken(mins)'
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 8))
sns.scatterplot(x='total_items', y='time_taken(mins)', data=df_, ax=axes[0, 0])
sns.scatterplot(x='num_distinct_items', y='time_taken(mins)', data=df_, ax=axes[0, 1])
sns.scatterplot(x='subtotal', y='time_taken(mins)', data=df_, ax=axes[0, 2])
sns.scatterplot(x='total_onshift_partners', y='time_taken(mins)', data=df_, ax=axes[1, 0])
sns.scatterplot(x='total_outstanding_orders', y='time_taken(mins)', data=df_, ax=axes[1, 1])
sns.scatterplot(x='max_item_price', y='time_taken(mins)', data=df_, ax=axes[1, 2])
plt.tight_layout()


# In[20]:


fig=plt.figure(figsize=(20,8))
ax=[None for _ in range(3)]
ax[0]=plt.subplot2grid((2,3),(0,0))
ax[1]=plt.subplot2grid((2,3),(0,1))
ax[2]=plt.subplot2grid((2,3),(0,2))
sns.scatterplot(x='month',y='time_taken(mins)',data=df_,color='green',ax=ax[0])
sns.scatterplot(x='day',y='time_taken(mins)',data=df_,color='orange',ax=ax[1])
sns.scatterplot(x='year',y='time_taken(mins)',data=df_,color='purple',ax=ax[2])
plt.tight_layout()


# In[21]:


#correlation heatmap
plt.figure(figsize=(24,10))
sns.heatmap(df_.corr(), cmap='YlGnBu', annot=True, annot_kws={'size':10})



# In[22]:


abs_corr = abs(df_.corr()['time_taken(mins)'])
sorted_corr = abs_corr.sort_values(ascending=False)
print(sorted_corr)

