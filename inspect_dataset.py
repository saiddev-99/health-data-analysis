import pandas as pd

df = pd.read_csv('archive/pima_diabetes_data.csv')
print('columns:')
print(list(df.columns))
print('shape:', df.shape)
print('head:')
print(df.head(3).to_string())
