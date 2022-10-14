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

#@st.cache
#def get_data():
 ##return df

with header:
  st.title("Supermarket Sales Prediction")
  st.text("In this project I will look into product that makes most sales")
  df = pd.read_csv('data/carrefour.csv')
  st.write(df.head())

  st.subheader("Product line distribution on Carrefour dataset")
  product_sale = pd.DataFrame(df['product_line'].value_counts())
  st.bar_chart(product_sale)

  st.subheader("Customer Type")
  customer = pd.DataFrame(df['customer_type'].value_counts())
  st.bar_chart(customer)

  st.subheader("Carrefour Branches")
  branches = pd.DataFrame(df['branch'].value_counts())
  st.bar_chart(branches)

  st.subheader("payment method")
  payment = pd.DataFrame(df['payment'].value_counts())
  st.bar_chart(payment)
with dataset:
    st.header("Carrefour sales dataset")


with features:
    st.header("The features I created")

    st.markdown('branch')
    st.markdown('customer_type')
    st.markdown('gender')
    st.markdown('product_line')
    st.markdown('unit_price')
    st.markdown('quantity')
    st.markdown('tax')
    st.markdown('date')
    st.markdown('time')
    st.markdown('payment')
    st.markdown('cog')
    st.markdown('cogs')
    st.markdown('gross_income')
    st.markdown('rating')
    st.markdown('total')

with model_Training:
    st.header("Time to train the model")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes")
    
    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('What should be the max_depth of the model, min_value =10,max_value = 100',value = 20, step = 10)
    n_estimators = sel_col.selectbox('How many trees should there be?', options = [100,200,300,'No limit'],index = 0)
    sel_col.text('Here are the input features')
    sel_col.write(df.loc[:, df.columns!='total'])
    input_features = sel_col.text_input('Which feature should be used as input feature?','product_line')
  