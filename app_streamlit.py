import streamlit as st
from utils.preprocessing_model import ModellingData
from utils.utils import change_to_province
import pandas as pd
import pickle


df = pd.read_csv("Dataset.csv", sep=",")
del df['Price']
columns = df.columns


st.title("Welcome to an house pricing predictor in Belgium")
st.markdown("Get the price of your house")

st.header("Time to give us some information about your house")
st.markdown("Let's go!!")


locality = st.number_input("Enter your locality")
number_of_room = st.number_input("Enter the number of rooms")
area = st.number_input("Enter the area of your house")
terrace_area = st.number_input("Enter the area of your terrace")
garden_area = st.number_input("Enter the area of your garden")
surface_of_the_land = area + terrace_area + garden_area

type_of_property = st.selectbox('Type of property', ["house", "apartment"])
fully_equipped_kitchen = st.selectbox('Is your Kitchen fully equipped?', ["Yes", "No"])
furnished = st.selectbox('Is your house is sell furnished?', ["Yes", "No"])
open_fire = st.selectbox('Do you have an open fire?', ["Yes", "No"])
number_of_facades = st.selectbox('What is the number of facades?', [2, 3, 4])
swimming_pool = st.selectbox('Do you have a swimming pool?', ["Yes", "No"])
state_of_building = st.selectbox('What is the state of your house?', ["medium", "good", "to renovate", "new"])
fully_equipped_kitchen = 1 if fully_equipped_kitchen == "Yes" else 0
furnished = 1 if furnished == "Yes" else 0
open_fire = 1 if open_fire == "Yes" else 0
swimming_pool = 1 if swimming_pool == "Yes" else 0

numerical_features = ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area', 'Surface of the land' ]
categorical_features = ['Type of property','Fully equipped kitchen', 'Furnished', 'Open fire','Number of facades',
                       'Swimming pool', 'State of the building', 'Province', 'Region']

if st.button("Submit"):
    province = change_to_province(locality)[0]
    region = change_to_province(locality)[1]
    x = [locality, type_of_property,number_of_room, area, fully_equipped_kitchen,furnished,open_fire,
         terrace_area, garden_area, surface_of_the_land,
          number_of_facades,
         swimming_pool, state_of_building, province, region
         ]
    x = pd.DataFrame([x],columns=columns)
    file_name = "xgb_reg.pkl"
    xgb_model_loaded = pickle.load(open(file_name, "rb"))
    result = xgb_model_loaded.predict(x)
    st.success(f"The estimated price of the property is {round(result[0])} euros")
