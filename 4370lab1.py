# -*- coding: utf-8 -*-
"""4370lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C8o3bRa5Hd00d4myFBb_yYQoFRCnYDjS
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
# import statsmodels.api as sm

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score,mean_squared_error

df = pd.read_csv("/content/Fare prediction.csv")
df.head()

df.head()

df.info()

df.describe(include='all')

df.isnull().sum()

df.duplicated().sum()

df = df.drop_duplicates()

df.duplicated().sum()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

#could'nt run the code fully as the system isn't supporting.

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
# Compute the correlation matrix for numerical variables
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()