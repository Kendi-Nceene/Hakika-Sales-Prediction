import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import xgboost as xg
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import make_multilabel_classification


header = st.container()
dataset = st.container()
features = st.container()
model_Training = st.container()

@st.cache
def get_data():
  df = pd.read_csv('data/carrefour.csv')

  return df

with header:
  st.title("Supermarket Sales Prediction")
  st.text("In this project I will look into product that makes most sales")
  df = pd.read_csv('data/carrefour.csv')
  st.write(df.head())

  st.subheader("Product line distribution on Carrefour dataset")
  product_sale = pd.DataFrame(df['product_line'].value_counts())
  st.bar_chart(product_sale)
with dataset:
    st.header("Carrefour sales dataset")


with features:
    st.header("The features I created")

    st.markdown('')

with model_Training:
    st.header("Time to train the model")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes")
    
    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('What should be the max_depth of the model, min_value =10,max_value = 100',value = 20, step = 10)
    n_estimators = sel_col.selectbox('How many trees should there be?', options = [100,200,300,'No limit'],index = 0)
    sel_col.text('Here are the input features')
    sel_col.write(df.loc[:, df.columns!='total'])
    input_features = sel_col.text_input('Which feature should be used as input feature?','product_line')
    
if n_estimators == "No limit":
    xg.XGBRegressor(max_depth = max_depth)
else:
    xg.XGBRegressor(max_depth = max_depth, n_estimators = n_estimators)

X = df[[input_features]]
y = df[['total']]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) 
#print(X_train)
#xgb_r = xg.XGBRegressor()

#xgb_r.fit(X_train, y_train)
#y_pred = xgb_r.predict(X_test)
#df1 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

#disp_col.subheader("mean absolute error is:")
#disp_col.write("Mean Absolute Error, y, prediction")

#disp_col.subheader("mean squared error is:")
#disp_col.write("mean Squared Error, y, prediction")

#disp_col.subheader("root mean squared error is: ")
#disp_col.write("root mean squared error, y, prediction")