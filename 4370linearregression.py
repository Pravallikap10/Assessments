# -*- coding: utf-8 -*-
"""4370linearregression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q0tHc4aTFxvLQqxCxzKiOucx7fdzI2Hp
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score,mean_squared_error

df = pd.read_csv("/content/expenses.csv")
df.head()

df.head()

df.info()

df.describe(include='all')

df.isnull().sum()

df.duplicated().sum()

df = df.drop_duplicates()

df.duplicated().sum()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
# Compute the correlation matrix for numerical variables
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

data_null_models = df[df['bmi'].isna()]

data_null_models.head(20)

df1 = df.groupby(['region','bmi'])['age'].mean()

bmi_mode = df['bmi'].mode()[0]  # The mode() function returns a Series, take the first element
age_mode = df['age'].mode()[0]

print(bmi_mode)
print(age_mode)
# # Fill missing values with the mode
df['bmi'] = df['bmi'].fillna(bmi_mode)
df['age'] = df['age'].fillna(age_mode)

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create a box plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(10, 6))  # Set the figure size for better readability
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

Q1 = df['children'].quantile(0.25)
Q3 = df['children'].quantile(0.75)
iqr = Q3-Q1
lower_bound = Q1-1.5*iqr
upper_bound = Q3+1.5*iqr
df_proper= df[(df['children']>lower_bound) & (df['children']<upper_bound)]
df_proper

scaler = MinMaxScaler()
scaler.fit(X)
scaler.transform(X)
x-min/max-min =
X_expense=pd.DataFrame(scaler.fit_transform(X_expense[list(X.children)]),
                                    columns=X.children)
X_test=pd.DataFrame(scaler.transform(X_test[list(X.children)]),
                                    children=X.children)
#

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

y_pred[:5]

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

rmse = mean_squared_error(y_test, y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

r2_s = r2_score(y_test, y_pred)
print("R2 Score:", r2_s)