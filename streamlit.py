import streamlit as st
from normalize_data import *
from utils.utils import change_to_province
from normalize_data import preprocessor

st.title("Welcome to the best house pricing predictor in Belgium")
st.markdown("Get the price of your house")

st.header("Time to ive us some information about your house")
st.markdown("Let's go!!")


locality = st.number_input("Enter your locality")
number_of_room = st.number_input("Enter the number of rooms")
area = st.number_input("Enter the area of your house")
terrace_area = st.number_input("Enter the area of your terrace")
garden_area = st.number_input("Enter the area of your garden")
surface_of_the_land = area + terrace_area + garden_area

type_of_property = st.selectbox('Select', ["House", "Apartment"])
fully_equipped_kitchen = st.selectbox('Is your Kitchen fully equipped?', ["Yes", "No"])
furnished = st.selectbox('Is your house is sell furnished?', ["Yes", "No"])
open_fire = st.selectbox('Do you have an open fire?', ["Yes", "No"])
number_of_facades = st.selectbox('What is the number of facades?', [2, 3, 4])
swimming_pool = st.selectbox('Do you have a swimming pool?', ["Yes", "No"])
state_of_building = st.selectbox('What is the state of your house?', ["medium", "good", "to renovate", "new"])
province = change_to_province(locality)[0]
region = change_to_province(locality)[1]

numerical_features = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land ]
categorial_features = [type_of_property,fully_equipped_kitchen, furnished, open_fire,number_of_facades,
                       swimming_pool, state_of_building, province, region]

x = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land,
     type_of_property, fully_equipped_kitchen, furnished, open_fire, number_of_facades,
     swimming_pool, state_of_building, province, region
     ]

# load
if st.button("Submit"):
    preprocessor(numerical_features, categorial_features)
    file_name = "xgb_reg.pkl"
    xgb_model_loaded = pickle.load(open(file_name, "rb"))
    result = (xgb_model_loaded.predict(x))
    st.write('Tour house is evaluated to : %€' % result)
