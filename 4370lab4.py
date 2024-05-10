# -*- coding: utf-8 -*-
"""4370lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kg7BHzbIvuQYHM_mM4QMT_a_Ql0rWHuF
"""

import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("/content/anomaly_train.csv")
df.head()

clf = IsolationForest(contamination=0.05)

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'Transaction_Type': ['Retail Purchase', 'Online Payment', 'Retail Purchase', 'Online Payment'],

})


label_encoder = LabelEncoder()

df['Transaction_Type_Encoded'] = label_encoder.fit_transform(df['Transaction_Type'])

print(df[['Transaction_Type', 'Transaction_Type_Encoded']])

clf.fit(df)

y_pred = clf.predict(df)

import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("/content/anomaly_train.csv")

df = data[['Time', 'Amount', 'User']]

clf = IsolationForest(contamination=0.05)

clf.fit(df)
y_pred = clf.predict(df)
anomalies = df[y_pred == -1]