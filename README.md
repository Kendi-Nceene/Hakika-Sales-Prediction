# Hakika Sales Prediction

This project does Data Analytics and applies machine learning algorithms to predict the outlet production sales.
## POWER LEARN PROJECT
#### SOFTWARE DEVELOPMENT
#### COHORT  1

## NAME
###### KENDI NCEENE

## SUPERVISORS
###### SABURI KIMOTHO JOHN
######STANLEY MUNGA




## Problem Statement
Sales Prediction is a problem that can be solved by using a machine learning technique.
The machine learning technique that is used in this problem is called supervised learning.
Supervised learning is one of the three types of machine learning techniques, and it involves training a model to perform a task based oninput data. The input data in this case are the past sales numbers, which are then used to predict future sales numbers.
The goal of supervised machine learning is to find an equation relating the inputs and outputs so that when new inputs are given, we can predict what the outputs will be with more accuracy than if we were just guessing. This equation is called the “model” and there are many different ways to determine what it should look like for each specific problem


## General Objective
Building a machine learning algorithm to predict sales with the lowest Root Mean Squared Error(RMSE).

## Specific Objectives
To investigate the distribution of fat content in the dataset.
To investigate which outlet shop had the highest sales.
To investigate the correlation between the target variable and other variables


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







