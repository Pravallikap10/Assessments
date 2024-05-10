# -*- coding: utf-8 -*-
"""4370lab2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QbKxraYcFX1Fn1hJcx09hBchHtCS0Rme
"""

import pandas as pd
import numpy as np
from sklearn import metrics #accuracy, f1 score, precision.....
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

df = pd.read_csv("/content/penguins_classification.csv")
df.head()

df.species = pd.to_numeric(df.species,errors='coerce')
df.info()

num_df = df.select_dtypes(include=np.number)
df2=df.iloc[:, 1:]

print(df2)

df2['body_mass_g'].replace(to_replace = 'Yes', value=1, inplace=True)
df2['body_mass_g'].replace(to_replace = 'No' , value=0, inplace= True)

df_dummies=pd.get_dummies(df2)
print(df_dummies.head())

df2.select_dtypes(include=np.number).corr()['body_mass_g']
df_co=df_dummies.corr()['body_mass_g']
df_co.plot(kind = 'bar')

df_bodymass = df_dummies['body_mass_g']
df_bodymass
df_bodymass.dropna(axis =0, inplace=True)
df_dummies.dropna(axis =0, inplace=True)
df_dummies2=df_dummies.copy()

y=df.body_mass_g
enc = LabelEncoder()
y_enc = enc.fit_transform(y)
y_enc = y_enc.reshape(-1,1)

from sklearn.preprocessing import MinMaxScaler
features = df_dummies2.columns.values
scaler = MinMaxScaler(feature_range = (0,1))
scaler.fit(df_dummies2)
X=pd.DataFrame(scaler.transform(df_dummies2))
X.columns = features
X

num_df.dropna(axis= 0, inplace=True)
num_df

X_train, X_test, y_train, y_test = train_test_split(num_df,df_bodymass)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

## fitting logistic regression
model = LogisticRegression()
# model = linear_model.LogisticRegression(random_state=16)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)


cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))