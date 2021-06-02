import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv("../Data8.csv")

pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_columns", None)

print(df.describe())