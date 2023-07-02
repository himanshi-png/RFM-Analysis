import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

#Taking a look at the data
df=pd.read_csv('data.csv')
df.head(5)

# Here, I tried to take a closer look at the data where I found that there is exists null values in CustomerID which 
df.info()

#Creating a new table where I will use only the required columns for my snanlysis
table1=df[['InvoiceNo','CustomerID','InvoiceDate','UnitPrice','Quantity','Country']]

# Creating a new column called Sales which gives the total sales from each customer made
table1['Sales']=table1['UnitPrice']*table1['Quantity']

# Converting InvoiceDate into datetime
table1['InvoiceDate']=pd.to_datetime(table1['InvoiceDate'])

# Removing all the NA values and assigning it to a new table called table2
table2=table1.dropna()
table2.info()


#1. Recency (R): Days since last purchase: How many days ago was their last purchase
# Using current date and time to get today's date
now=datetime.now()

# Creating a new table with 2 columns only which will help to calculate Recency
df_recency=table2[['CustomerID','InvoiceDate']].copy()

# Used groupby function to group by the CustomerID and getting the maximum date which will help to calculate the days difference between today's date  and the last date since order for each customer

df_recency.groupby('CustomerID').agg({'InvoiceDate':['max']})
df2=df_recency.drop_duplicates(subset='CustomerID')
df2

# Created a new column Recency which consists the difference of days
df2['Recency']=(now-df2.InvoiceDate).dt.days
Recency=df2.drop('InvoiceDate',axis=1)
Recency


#2. Monetary(M): Total money spent by customer

# Creating a new table with 2 columns only which will help to calculate Monetary
df_monetary=table2[['CustomerID','Sales']].copy()

# Used groupby function to group by the CustomerID and getting the sum of amount spent by per customer
Monetary=df_monetary.groupby('CustomerID',sort=False).sum().reset_index()
Monetary


#3. Frequency: Total number of transactions: How many times has the customer purchased from our store?
# Creating a new table with 2 columns only which will help to calculate Frequency
df2=table2[['CustomerID','InvoiceNo']].copy()

#  Used groupby function to group by the CustomerID and getting the total number of orders ordered per customer
Frequency=df2.groupby(['CustomerID'],sort=False)['InvoiceNo'].count().reset_index()
Frequency


# Created a new table called df_rfm which will consist all 3 tables created and joining them bbased on left join on CustomerID column
df_rm=Monetary.merge(Recency,on='CustomerID',how='left')
df_rfm=Frequency.merge(df_rm,on='CustomerID',how='left')
df_rfm.rename(columns={'InvoiceNo':'Frequency','Sales':'Monetary','InvoiceDate':'Recency'},inplace=True)
df_rfm

#Calculating RFM scores using quantile-based discretization
# Calculating r_score,f_score,m_score
df_rfm['r_score']=pd.qcut(df_rfm['Recency'], q=5, labels=[1, 2, 3, 4, 5])
df_rfm['f_score']=pd.qcut(df_rfm['Frequency'], q=5, labels=[1, 2, 3, 4, 5])
df_rfm['m_score']=pd.qcut(df_rfm['Monetary'], q=5, labels=[1, 2, 3, 4, 5])

#Calculating the aggregating RFM_Score
df_rfm['RFM_score']=df_rfm['r_score'].astype(str) +df_rfm["f_score"].astype(str) + df_rfm["m_score"].astype(str)
df_rfm


# Assigning the segments based on the rfm_score
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

df_rfm['Segment'] = df_rfm['r_score'].astype(str) + df_rfm['f_score'].astype(str)
df_rfm['Segment'] = df_rfm['Segment'].replace(seg_map, regex=True)
df_rfm.head()


#Added Country to a new table for the analysis
df_segment=df_rfm.assign(Country=table1.Country,CustomerID=table1.CustomerID)
df_segment


# Used groupby function to find where most Customers are from and of which category
table4=df_segment.groupby(['Segment','Country'])['CustomerID'].count()
table4

#Used plotly library to get a stacked bar chart which conveys where most customers are from and of which 
Segmentdf_segment.groupby(['Segment','Country'])['CustomerID'].count().unstack().plot(kind='bar',stacked='True')