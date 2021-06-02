import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
import pickle
from xgboost import XGBRegressor

df = pd.read_csv("Data8.csv", sep=",")

X = df.drop("Price", axis=1)
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)


numerical_features = ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area', 'Surface of the land' ]
categorical_features = ['Type of property','Fully equipped kitchen', 'Furnished', 'Open fire','Number of facades',
                       'Swimming pool', 'State of the building', 'Province', 'Region']


numerical_pipeline = make_pipeline(SimpleImputer(), StandardScaler())
categorical_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"),
                                   OneHotEncoder())
preprocessor = make_column_transformer((numerical_pipeline, numerical_features),
                       (categorical_pipeline, categorical_features))


#def preprocessor(numeric, categorical):
    #return preprocessor

model = make_pipeline(preprocessor, XGBRegressor())
model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(model.score(X_test, y_test))

file_name = "xgb_reg.pkl"

# save
pickle.dump(model, open(file_name, "wb"))


# # load
# xgb_model_loaded = pickle.load(open(file_name, "rb"))
# print(xgb_model_loaded)
# # test
# ind = 1
# test = X_val[ind]
# xgb_model_loaded.predict(test)[0] == xgb_model.predict(test)[0]