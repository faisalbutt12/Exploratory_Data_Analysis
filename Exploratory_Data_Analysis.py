#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv("C:\\Users\\ITS\\OneDrive\\Desktop\\supermarket_sales - Sheet1.csv",parse_dates=['Date'])


# In[6]:


df


# In[7]:


import warnings


# In[8]:


warnings.filterwarnings('ignore')

Invoice id: Computer generated sales slip invoice identification number
Branch: Branch of supercenter (3 branches are available identified by A, B and C).
City: Location of supercenters
Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
Gender: Gender type of customer
Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
Unit price: Price of each product in $
Quantity: Number of products purchased by customer
Tax: 5% tax fee for customer buying
Total: Total price including tax
Date: Date of purchase (Record available from January 2019 to March 2019)
Time: Purchase time (10am to 9pm)
Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
COGS: Cost of goods sold
Gross margin percentage: Gross margin percentage
Gross income: Gross income
Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)


# # Display Top 5 Rows of Data

# In[9]:


df.head(5)


# # Display Last 5 Rows of Data

# In[10]:


df.tail(5)


# # Display Random 5 Rows of Data

# In[11]:


df.sample(5)


# # Find Shape of DataSet

# In[12]:


df.shape


# In[13]:


print("Total Rows are ", df.shape[0])


# In[14]:


print("Total Columns are ", df.shape[1])


# # Check Null Values

# In[15]:


df.isnull()


# In[16]:


df.isnull().sum()


# # Get Data Set Info

# In[17]:


df.info()


# # Get OverAll Statistics about Data

# In[18]:


df.describe()


# In[19]:


cat_vars=[]
num=[]
for column in df.columns:
    if df[column].nunique()>10:
        num.append(column)
    else:
        cat_vars.append(column)


# In[20]:


cat_vars


# In[21]:


num


# # Univariant Analysis

# # Find Aggregrate Sales Among Branches (Cetagorical Columns)

# In[22]:


sns.countplot(x='Branch', data=df)


# In[23]:


df['Branch'].value_counts()


# In[24]:


df['Branch'].value_counts().plot(kind='pie', autopct="%1.2f%%")


# # Most Popular Method used by Customers (Cetagorical)

# In[25]:


df.columns


# In[26]:


value=df['Payment'].value_counts();


# In[27]:


value


# In[28]:


sns.countplot(x='Payment', data=df)


# # Find Distribution of Customer Rating

# In[29]:


sns.displot(df['Rating'],kde=True)


# In[30]:


df['Rating'].skew()


# In[31]:


df['Rating'].mean()


# In[32]:


df['Rating'].median()


# # Find The Distribution of Cost of Goods Solds(Numerical)

# In[33]:


sns.distplot(df['cogs'])


# In[34]:


sns.boxplot(x='cogs',data=df)


# # BiVariant Analysis//Multivariant Analysis

# # Does the cost of goods Sold effects the Rating That the customer provide?(Numerical)

# In[35]:


cat_vars


# In[36]:


num


# In[37]:


sns.scatterplot([df['cogs'], df['Rating']])


# # Does the cost of goods Sold effects the Rating That the customer provide?(Numerical)

# In[38]:


sns.scatterplot([df['gross income'],df['Rating']])


# # Find The Most Profitable Branch As Per Gross Income

# In[39]:


sns.barplot(x='Branch',y='gross income', data=df)


# In[40]:


sns.barplot(x='Branch',y='gross income', data=df, hue=df['City'])


# # Is There any Relation Between Gender and Gross Incom Numerical Column and Cetegorical 

# In[41]:


sns.barplot(x='Gender',y='gross income', data=df)


# In[45]:


sns.boxplot(x='Gender', y='gross income', data=df)


# In[48]:


sns.boxplot(x='Gender', y='gross income', data=df, hue=df['Customer type'])


# # Fine The Product Line That Genrate the Most Income

# In[50]:


sns.barplot(x='Product line',y='gross income', data=df)
plt.xticks(rotation=60)


# # Find The Highest Unit Price in Product Line

# In[53]:


sns.barplot(x='Product line', y='Unit price', data=df)
plt.xticks(rotation=60)


# # Fine The Diffrent Payment Method Used by the CUstomer City Wise

# In[55]:


data=pd.crosstab(df['City'],df['Payment'])


# In[56]:


data


# In[57]:


sns.heatmap(data)


# # Which Product Line Purchase the Highest Quantity

# In[66]:


df.groupby('Product line').sum()['Quantity'].nlargest().plot(kind='bar')


# # Display Daily Sales By Day of the Week

# In[67]:


df['Date'].dt.dayofweek


# In[68]:


dw_mapping={
    0:'Mon',
    1:'Tue',
    2:'Wed',
    3:'Thu',
    4:'Fri',
    5:'Sat',
    6:'Sun'
}


# In[69]:


df['Date'].dt.dayofweek.map(dw_mapping)


# In[70]:


df['day_of_week']=df['Date'].dt.dayofweek.map(dw_mapping)


# In[71]:


df.head(5)


# In[72]:


df['day_of_week'].value_counts()


# In[73]:


df['day_of_week'].value_counts().plot(kind='bar')


# # What will The Highest Month of Sale

# In[74]:


month_mapping={
    1:'Jan',
    2:'Feb',
    3:'Mar',
    4:'Apr',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Aug',
    9:'Sep',
    10:'Oct',
    11:'Nov',
    12:'Dec'
}


# In[77]:


df['month']=df['Date'].dt.month.map(month_mapping)


# In[78]:


df.head(5)


# In[79]:


df['month'].value_counts()


# In[81]:


df['month'].value_counts().plot(kind='bar')


# In[ ]:




