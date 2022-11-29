# HAKIKA SALES PREDICTION

## Student’s name : Kendi Nceene
## Power Learn Project
#### Python 
###### (Data Science project)
###### 
####### October, 2022



## Supervisors
### Saburi Kimotho John
### Stanley Munga


## BUSINESS UNDERSTANDING
## Business Overview


Sales forecasting is a process in which a company can estimate their future sales based on previous data and industry comparisons. As a process, sales forecasting allows companies to utilize this data in order to produce accurate performance plans which can shape the way they do business.
 
Some of the key areas which a sales forecast can benefit your business are predicting sales revenues for varied lengths of time which allows the business to appropriately assign resources where needed and to develop data driven plans for future growth and expansion.
 
According to an article by intact softwares the first step to accurate sales forecasting is to look not to the future but the past. By examining sales data over the past several months, you’ll glean insights that you can use as the basis of your future sales predictions, noting things like volumes, trends, and seasonality changes that caused peaks and troughs in demand.
 
Sales prediction is especially important for small businesses because losses due to unsold inventory may threaten the company's survival. Forecasting reduces uncertainty but replaces it with the risk of excess inventory, reduced profit or other specific risks. Data and the use of models can reduce the risk of sales forecasting if they are based on past successful forecasting. Adding current data to revise forecasts also reduces risk.
 
In this regard, a sales prediction model is vital for businesses. A sales forecast system is a model that predicts  company’s sales based on a few criterias of how the business runs
 
 
Problem Statement










General Objective
To build a supervised  machine learning algorithm to make sales predictions.

Specific Objectives
To determine which store makes the highest sales.
To determine which products sells the most
To determine which category of products make the highest amount of sales.
To determine which .
Research Questions
Which store makes the highest sales?
What category of products make the highest amount of sales?
Is there a mode of payment that is used more?
Which store makes the highest amount of sales.
Business Success Criteria

Successfully building a model that makes sales predictions with a low RMSE.

Project Plan
We will use the Cross Industry Standard Process For Data mining(CRISP - DM) for conducting this research. 
Assessing the Situation
Resource Inventory
Datasets:
link
Software:
 i. Github
ii. Jupyter Notebook
iii. Django


Assumptions
The data provided is correct and up to date

Constraints

There are not many available datasets to use for the project.
The time given for this project to be completed was not enough

2. Data Understanding
Data Understanding Overview
In this section, we explore the dataset and identify the features of the data. In order to perform further analysis, the quality of data gathered is required.

Data Description

The dataset we are using for analysis and exploration contains data sourced from hdx. 

The data we are using was retrieved from the following site: which is in a CSV format.
This train dataset contains 8523 rows and 12 columns while the test dataset contains 5681 rows and 11 columns.

ProductID : unique product ID

Weight : weight of products

FatContent : specifies whether the product is low on fat or not

Visibility : percentage of total display area of all products in a store allocated to the particular product

ProductType : the category to which the product belongs

MRP : Maximum Retail Price (listed price) of the products

OutletID : unique store ID

EstablishmentYear : year of establishment of the outlets

OutletSize : the size of the store in terms of ground area cove

LocationType : the type of city in which the store is located

OutletType : specifies whether the outlet is just a grocery store or some sort of supermarket

OutletSales : (target variable) sales of the product in the particular store

