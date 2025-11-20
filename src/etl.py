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
print(df.dtypes)
print(df.describe())

#check for msiisng values
print(df.isnull().sum())


#null Werte aus embarked spalte entfernen
df = df[df['Embarked'] != 0]
print(df['Embarked'])

#schauen ob die zero zeilen nur null enthalten
print((df['zero'] == 0).all())

for column in df.columns:
    if (df[column] == 0).all():
        print(f"Column {column } contains only zero values.")
    else:
        print(f"Column {column} contains non-zero values.")

#spalten mit nur null werten entfernen
zero_only_columns = (df == 0).all()



    