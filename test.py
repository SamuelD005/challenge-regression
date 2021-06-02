# import streamlit as st
# from normalize_data import *
# from utils.utils import change_to_province
# from normalize_data import preprocessor
#
# st.title("Welcome to the best house pricing predictor in Belgium")
# st.markdown("Get the price of your house")
#
# st.header("Time to ive us some information about your house")
# st.markdown("Let's go!!")
#
#
locality = 1
number_of_room = 2
area = 3
terrace_area = 4
garden_area = 5
surface_of_the_land = 6

type_of_property = 6
fully_equipped_kitchen = 7
furnished = 8
open_fire = 9
number_of_facades = 10
swimming_pool = 11
state_of_building = "test"
province = "haha"
region = "hehe"

numerical_features = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land ]
categorial_features = [type_of_property,fully_equipped_kitchen, furnished, open_fire,number_of_facades,
                       swimming_pool, state_of_building, province, region]

x = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land,
     type_of_property, fully_equipped_kitchen, furnished, open_fire, number_of_facades,
     swimming_pool, state_of_building, province, region
     ]
print(numerical_features, categorial_features)
# load
# @st.cache(suppress_st_warning=True)

# file_name = "xgb_reg.pkl"
# xgb_model_loaded = pickle.load(open(file_name, "rb"))
# st.write(xgb_model_loaded.predict(x))