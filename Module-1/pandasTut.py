import pandas as pd
import numpy as np
# Creating a pandas dataframe

# importing the boston house price data
from sklearn.datasets import fetch_openml

housing = fetch_openml(name="house_prices", as_frame=True)
# print(type(housing))
# print(housing)

# pandas dataframe
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)

print(housing_df)

# Starting rows of the dataframe
print(housing_df.head())

# Ending rows of the dataframe
print(housing_df.tail())

print(housing_df.shape)

# Columns in the dataframe
print(housing_df.columns)

# Importing the data from a CSV file to pandas DF
diabetes_df = pd.read_csv('large-dataset/diabetes.csv')

print(diabetes_df)

print(type(diabetes_df))

print(diabetes_df.columns)

print(diabetes_df.head())

print(diabetes_df.shape)

# Exporting a DF to a excel file
diabetes_df.to_excel('diabetes_ex.xlsx')

print('Excel Data')

# importing data from excel file to pandas DF
diabetes_ex = pd.read_excel('diabetes_ex.xlsx')

print(diabetes_ex)

print(diabetes_ex.columns)

print("Total Columns: ", len(diabetes_ex.columns))

print("\nDataframe with random values")
# Creating a DF with random values

random_df = pd.DataFrame(np.random.rand(20, 10))
print(random_df)
print(random_df.head())
print(random_df[[0]])
print(random_df[[0, 1]])

# Information about the DF
print(diabetes_ex.info())

print('\nNumber of missing/null values in diabetes_ex DF')
# finding the number of missing values
print(diabetes_ex.isnull().sum())

# Counting the values based on labels
print()
print(diabetes_ex.value_counts('Outcome'))

# Group the values based on the mean
print(diabetes_ex.groupby('Outcome').mean())

# Statistical measures
print("\nStatistical measures")

# 1) Count or number of values
print("Total values:")
print(diabetes_ex.count())

# 2) mean value - column wise
print("\nMean values:")
print(diabetes_ex.mean())

# 3) Standard Deviation - column wise
print('\nStandard Deviation-Column wise:')
print(diabetes_ex.std())

# 4) Minimum value
print('\nMinimum value')
print(diabetes_ex.min())

# 4) Maximum value
print('\nMaximum value')
print(diabetes_ex.max())

# 5) All the statistical measures in one go
print('\nAll the statistical measures')
print(diabetes_ex.describe())

# Manipulating the DF

# Adding a column to a DF
manip_df = diabetes_ex

manip_df['OutCome2'] = diabetes_ex['Outcome']
print(manip_df['OutCome2'])
print(manip_df.columns)

# Removing a row & column
print('\nDeleting a Row & Column')
print(manip_df.drop(index=0, axis=0))

print(manip_df.drop(columns='OutCome2', axis=1))

print(manip_df)

# locating a specific row & column
print('\nLocating a specific row using index')

print(diabetes_ex.iloc[2])

print(diabetes_ex.iloc[:, 0])

