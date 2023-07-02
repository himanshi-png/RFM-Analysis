# Project title: RFM-Analysis

#### The link for the Project:
[Project Code](https://github.com/himanshi-png/RFM-Analysis/blob/main/RFM_Analysis.py)

## Description
This project, the data is Superstore, in which I have used libraries like panda, matplotlib and numpy. 
In this project I have tried to answer of how we use data to help up-selling of products for a Superstore. I will write code to import the data and answer interesting questions about it by computing descriptive statistics.

## About the Dataset
The given dataset was taken from the dataset bundle present in Kaggle Datasets, Refer to this link This data is freely available on Kaggle <https://www.kaggle.com/datasets/vivek468/superstore-dataset-final>

With this dataset I am trying to answer few questions asked usually in data team to help find the most active/loyal customers for the company and whom should we promote more products. 

The name of the Dataset used for this projects is data.csv. There are 37039 rows in the file each row containing data about each customer's customer_id, InvoiceDate, Country etc.

I have used Python 3 for this analysis. The Libraries/Packages I used in this projects are as follows:
* numpy (as np is one of the very famous packages for working with arrays in python) 
* pandas (Is greatly used in analysis of data and making dataframe)
* matplotlib (Module is a visualization library) 
* datetime (Module supplies classes for manipulating dates and times)

## RFM Technique
To solve the questions I have used a Customer Segmentation technique to find most premium/loyal customers to the Superstore called as RFM- Recency, Frequency, Monetary.
* Recency - Number of days since last purchase made by customer.
* Frequency - Number of orders has the customer purchased in total.
* Monetary - The amount customer has spent in total for purchase of items.

RFM groups customers into different customer segments for easy recall and campaign targeting. It’s super useful in understanding responsiveness of your customers and for segmentation driven database marketing. It helps to decide the follwoing questions:
* Who are the loyal/slipping customers?
* Who has potential to be converted to loyal customers?
* Which customers can be retained?

## Inferences and Conclusion
The analysis gives an overview from most loyal to slipping customer segments.

With that, we’ve come to the end of this analysis. The following are conclusions drawn from the analysis. Hope you enjoyed!!

* Loyal segment has the most customers and mostly are from UK
* Hybernating segmented customers are second highest and are from UK
* Potentail segment has least number of customers and most are from UK

## References and Future Work
###Future Work
There are lot of scopes of improvement and/or addition in this project in future, with the data provided and adding extra datasets we can do:
* The in-depth targeted marketing may also use type of item purchased or customer campaign responses as factors.
* Customer demographics such as age, gender and ethinicity are not covered in RFM analysis
* RFM only uses historical data about customers and may not predict future customer activity.

### Refereces

* Netflix Titles Dataset: <https://www.kaggle.com/datasets/vivek468/superstore-dataset-final>
* Kaggle Datasets (Choose Dataset of your choice): <https://www.kaggle.com/datasets>
* RFM Technique: <https://www.investopedia.com/terms/r/rfm-recency-frequency-monetary-value.asp>
* Pandas user guide: <https://pandas.pydata.org/docs/user_guide/index.html>
* Matplotlib user guide: <https://matplotlib.org/3.3.1/users/index.html>
* Data analysis guide <https://jovian.ml/aakashns/python-pandas-data-analysis>
* Stackoverflow Community (Get answers of any problems): <https://stackoverflow.com/questions>
* Python solutions in Geeksforgeeks (Solutions made easy): <https://www.geeksforgeeks.org/python-programming-language/>
  
