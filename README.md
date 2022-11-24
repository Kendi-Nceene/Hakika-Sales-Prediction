# Sales-Prediction
## Big-Mart SALES PREDICTION
This project does Data Analytics and applies machine learning algorithms to predict the outlet production sales.

## NAME
#### KENDI NCEENE



## SUPERVISORS
#### SABURI KIMOTHO JOHN

## POWER LEARN PROJECT
#### SOFTWARE DEVELOPMENT
#### COHORT  1




## Problem Statement

The aim is to build a predictive model and find out the sales of each product at a particular store. Create a model by which Big Mart can analyse and predict the outlet production sales

It is the perfect project for learning Data Analytics. In this projec the reader will come to know 1: Data Exploration 2: Data Cleaning 3: Feature Engineering 4: Creating Models








## General Objective
To use a supervised  machine learning algorithm to make sales predictions.

## Specific Objectives
To determine which store makes the highest sales.
To determine which gender makes purchases more.
To determine which category of products make the highest amount of sales.
To determine which mode of payment is used more.
Research Questions
Which gender makes more purchases?
What category of products make the highest amount of sales?
Is there a mode of payment that is used more?
Which store makes the highest amount of sales.
Business Success Criteria

Successfully building a model that makes sales predictions with a low RMSE without overfitting.

## Project Plan
We will use the Cross Industry Standard Process For Data mining(CRISP - DM) for conducting this research. 
Assessing the Situation
Resource Inventory
Datasets:
link
Software:
 i. Github
ii. Jupyter Notebook
iii.Streamlit

## Assumptions
The data provided is correct and up to date

## Constraints

There are not many available datasets to use for the project.
The time given for this project to be completed was not enough

## 2. Data Understanding
Data Understanding Overview
In this section, we explore the dataset and identify the features of the data. In order to perform further analysis, the quality of data gathered is required.
Data Description

The dataset we are using for analysis and exploration contains data sourced from rpubs. The data we are using was retrieved from the following site: 
. Which is in CSV format.
This dataset contains 1000 rows and 16 columns.

## Verifying Data Quality
 The following criteria was used to clarify the quality of our data
Accuracy: The data described was accurate.
Relevancy: The data met the requirements for the intended use.
Completeness: The data did not contain missing values
Timeliness: The data was up-to-date.
Consistency: The data had the data format as expected and was cross reference-able with the same results.

## 3. Data Preparation
These are the steps taken during data preparation :
   ## 3.1 Loading the dataset
Unzipped a folder then loaded the dataset from a CSV and created a python dataframe.

 ## 3.2 Cleaning Data

The data cleaning involved several steps :

 (i) We checked for missing values and found out that our data did not have null values.
 (ii) Checked for duplicates. The dataset had no duplicated values.
 (iii) There were outliers in our dataset but we decided to retain them since they were true values.
(iv) Corrected data types of some columns which include date and time. They were objects instead of datetime.
(v) Stripped off white spaces and lowered the cases of all columns.

## 4.0 Data Analysis

We performed the following activities in the analysis : Univariate Bivariate and Multivariate Analysis.

## (i) Univariate Analysis.

Under the univariate analysis we used histograms and pie charts.
From the analysis we deduced that :

The tax column,cogs distribution and gross income distribution columns were slightly skewed to the right.
The unit price column had an almost  normal distribution.
Food and beverages had the highest sales amounting to 56144.8440 whereas beauty products had the least sales of 49193.
Branch A had slightly higher sales than other branches with a total percentage of 34%.
Gender was almost equal in proportion although the female gender had a total of 50.1% .

## (ii) Bivariate Analysis

The variables did not have a strong correlation as the most of the correlations  ranged on the lower quartiles of having a direct relationship.


The analysis was also conducted as per the objectives :

Objective One :




## 5. Modeling

In the modeling process, we performed both supervised and deep learning.
The following models were used in the supervised learning :







