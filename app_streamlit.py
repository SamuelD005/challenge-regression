import app_streamlit as st
from utils.preprocessing_model import *
from utils.utils import change_to_province
from utils.preprocessing_model import preprocessor_fun

df = pd.read_csv("Data8.csv", sep=",")
df = df.drop(["Price", "PriceperMeter", "Unnamed: 0"], axis=1)
columns = df.columns
#df_streamlit = pd.DataFrame(columns = columns)


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


# numerical_features = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land ]
# categorial_features = [type_of_property,fully_equipped_kitchen, furnished, open_fire,number_of_facades,
#                        swimming_pool, state_of_building, province, region]

numerical_features = ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area', 'Surface of the land' ]
categorical_features = ['Type of property','Fully equipped kitchen', 'Furnished', 'Open fire','Number of facades',
                       'Swimming pool', 'State of the building', 'Province', 'Region']

# np.reshape(numerical_features, -1, 1)
# np.reshape(categorical_features, -1, 1)

# x = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land,
#      type_of_property, fully_equipped_kitchen, furnished, open_fire, number_of_facades,
#      swimming_pool, state_of_building, province, region
#      ]
#
# df = df.append(x)
#
# numerical_features = np.array(numerical_features)
# categorical_features = np.array(categorical_features)
# numerical_features = numerical_features.reshape(-1,1)
# categorical_features = categorical_features.reshape(-1,1)
# load
if st.button("Submit"):
    province = change_to_province(locality)[0]
    region = change_to_province(locality)[1]
    x = [locality, number_of_room, area, terrace_area, garden_area, surface_of_the_land,
         type_of_property, fully_equipped_kitchen, furnished, open_fire, number_of_facades,
         swimming_pool, state_of_building, province, region
         ]
    st.write(df_streamlit)
    st.write(x)
    x = pd.DataFrame(x,columns=columns)
    #df = pd.concat([df_streamlit,x],axis=0)
    st.write(x)
    #x = pd.DataFrame(x)
    #df = df.append(x)
    x = preprocessor_fun(numerical_features, categorical_features)
    file_name = "xgb_reg.pkl"
    xgb_model_loaded = pickle.load(open(file_name, "rb"))
    result = xgb_model_loaded.predict(x)
    st.write('Your house is evaluated to : %€' % result)
