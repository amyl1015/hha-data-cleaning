import pandas as pd
import datetime as dt
import uuid 
import numpy as np

df = pd.read_csv ('../data/School_Learning_Modalities.csv')

countRows, countColumns = df.shape
print("Row: " + str(countRows))
print("Columns  " + str(countColumns))

df.columns 
column_names = list(df)
print(column_names)

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
print(list(df))

df.columns = df.columns.str.lower()
print(df.columns)

df.drop(['week'], axis=1, inplace=True, errors='ignore') # remember this is CASE SENSITIVE
column_name = list(df.columns)
print(column_name)

print(df.isnull().sum())
df.dropna(inplace=True)
print()
print(df.isnull().sum())

df['district_nces_id'] = df['district_nces_id'].astype(str)
df['district_name'] = df['district_name'].astype(str)
df['learning_modality'] = df['learning_modality'].astype(str)
df['operational_schools'] = df['operational_schools'].astype(int)
df['student_count'] = df['student_count'].astype(int)
df['city'] = df['city'].astype(str)
df['state'] = df['state'].astype(str)
df['zip_code'] = df['zip_code'].astype(str)

df.duplicated()


def modality_inperson(row):
    if row['learning_modality'] == "In Person": 
        return True
    else:
        return False



df['id'] = df.apply(lambda row: modality_inperson(row), axis=1)
print (df)

