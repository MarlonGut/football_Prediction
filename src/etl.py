import pandas as pd
import numpy as np


#etl prozess für titanic daten 

#extract

#file path
file_path = r'C:\Users\Marlon Gutjahr\Documents\Data Science\soccer_matches\football_Prediction\data\train_and_test2.csv'
#read csv
data = pd.read_csv(file_path)
#in dataframe umwandeln
df = pd.DataFrame(data)

#explore

#head ausgeben
print(df.head())

#shape ausgeben
print(df.shape)

#namen von spalten
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df.nunique())
print(df.dtypes)

# drop the columns that are not needed for analysis
cols_to_drop = [ col for col in df.columns if df[col].nunique() == 1 ]
print(cols_to_drop)