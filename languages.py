import pandas as pd

import openpyxl 

df = pd.read_csv('languages.csv')

#print(df.head(5))
'''
columnas = df.columns
print(f'\n\n {columnas}')

columnas_int = df.select_dtypes(include=['int64']).columns
print(f'\n\n {columnas_int}')

#guardar dataset en formato xlsx
df.to_excel('languages.xlsx', engine='openpyxl')
'''
print(df['number_of_users'].max())