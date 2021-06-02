import pandas as pd
from utils.utils import *
import numpy as np

url = "https://raw.githubusercontent.com/JulienAlardot/challenge-collecting-data/main/Data/database.csv"
df = pd.read_csv("Data8.csv")
df = df[df['Type of property'].notna()]
df['Terrace Area'] = df['Terrace Area'].fillna(0)
df['Garden Area'] = df['Garden Area'].fillna(0)
df['Furnished'] = df['Furnished'].fillna(0)
df['Number of facades'] = df['Number of facades'].fillna(2)
df['Number of rooms'] = df['Number of rooms'].fillna(2.6)
df['State of the building'] = df['State of the building'].fillna("medium")
df['Surface of the land'] = df['Area'] + df['Terrace Area'] + df['Garden Area']
del df['Terrace']
del df['Garden']
del df['Prov_num']
del df['Region_num']

# drop_row_without_value("Area", df)
# drop_row_without_value("Price", df)
# df["PriceperMeter"] = df["Price"]//df["Area"]
# df["Province"] = df.apply(lambda x: change_to_province(x["Locality"])[0], axis=1)
# df["Region"] = df.apply(lambda x: change_to_province(x["Locality"])[1], axis=1)
# df["Prov_num"] = df.apply(lambda x: change_to_province(x["Locality"])[2], axis=1)
# df["Region_num"] = df.apply(lambda x: change_to_province(x["Locality"])[3], axis=1)

#del df['Unnamed: 0']
#del df['Url']
#del df['Source']

#print(df.head())
#null = df.isnull().sum()
#print(df["Subtype of property"].value_counts())
#df = df.drop(df.index[np.where(df["Subtype of property"] == "building")[0]])
#df = df.drop(df.index[np.where(df["Price"] <= 30000)[0]])
#df = df.drop(df.loc[df['Area'].idxmax()])
#df = df.drop(df['Area'].idxmax())
#url =["https://www.logic-immo.be/fr/vente/maisons-a-vendre/havre-7021/maison-70-chambres-e992c303-35a9-e5d5-fd27-4ae8d0876117.html",
    # "https://www.immoweb.be/fr/annonce/maison/a-vendre/havre/7021/8703998",
    # "https://www.immoweb.be/fr/annonce/immeuble-a-appartements/a-vendre/havre/7021/8951414",
    # "https://www.immoweb.be/fr/annonce/maison/a-vendre/marche-en-famenne/6900/9209135",
    # "https://www.immoweb.be/fr/annonce/immeuble-mixte/a-vendre/schaerbeek/1030/9140569"]

#df2 = df[~df.Url.str.contains('autres-biens')]

#df = df.set_index()
#data_final = df.reset_index()
del df['Unnamed: 0']
#del df['Unnamed: 0.1']
#del df['Type of sale']

del df['Subtype of property']
#del df['Url']

# df = df.set_index("Unnamed: 0.1")
# df = df.reset_index()
# dfhouse = df.drop(df.index[np.where(df["Type of property"] == "house")[0]])
# dfapart = df.drop(df.index[np.where(df["Type of property"] == "apartment")[0]])
# dfhouse.to_csv("DataHouse.csv")
df.to_csv("Data8.csv")

