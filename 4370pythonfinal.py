# -*- coding: utf-8 -*-
"""4370pythonfinal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Da6AiDTkBTwXPuN47aRVy0v2cqRLZ1A
"""

#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("/Final Dataset - IPL.csv")
num_rows, num_cols = dataset.shape
print(f'Number of rows: {num_rows}')
print(f'Number of columns: {num_cols}')
data_types = dataset.dtypes
numerical_cols = data_types[data_types != 'object'].index.tolist()
categorical_cols = data_types[data_types == 'object'].index.tolist()
print('Numerical columns:', numerical_cols)
print('Categorical columns:', categorical_cols)

#2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
missing_values = df.isnull().sum()
print('Missing values per column:')
print(missing_values)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df['first_ings_score'].fillna(df['first_ings_score'].mean(), inplace=True)
df['first_ings_wkts'].fillna(df['first_ings_wkts'].mode()[0], inplace=True)

#3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df.head(10)
df= df['highscore']
mean_values = df.mean()
median_values = df.median()
mode_values = df.mode().iloc[0]
range_values = df.max() - df.min()
variance_values = df.var()
std_deviation_values = df.std()
print('Mean values:')
print(mean_values)
print('Median values:')
print(median_values)
print('Mode values:')
print(mode_values)
print('Range values:')
print(range_values)
print('Variance values:')
print(variance_values)
print('Standard Deviation values:')
print(std_deviation_values)
print(df.describe())

#4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df.head(10)

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='first_ings_score', y='first_ings_wkts',
        s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
df.groupby('venue').size().plot(kind='barh',
                                color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df['second_ings_score'].plot(kind='line',
                             figsize=(8, 4), title='second_ings_score')
plt.gca().spines[['top', 'right']].set_visible(False)

#5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df.head(10)
my_str = df['date']
float_num = np.float64(my_str)
print(df.corr())

#6
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
z_scores = stats.zscore(df['margin'])
outliers = df[(z_scores > 3) | (z_scores < -3)]
print(outliers)
cleaned_df = df[(z_scores >= -3) & (z_scores <= 3)]
print(cleaned_df)

#7
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
avg_first_innings_score = df.groupby('venue')['first_ings_score'].mean()

win_rates_by_stage = df.groupby('stage')['match_winner'].value_counts(normalize=True).unstack()
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
avg_first_innings_score.plot(kind='bar')
plt.xlabel('Venue')
plt.ylabel('Average First Innings Score')
plt.title('Average First Innings Score by Venue')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
win_rates_by_stage.plot(kind='bar', stacked=True)
plt.xlabel('Stage of Tournament')
plt.ylabel('Win Rate')
plt.title('Win Rates by Stage of Tournament')
plt.xticks(rotation=45)
plt.legend(title='Team')
plt.show()

#8
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
player_of_match_count = df['player_of_the_match'].value_counts()
plt.figure(figsize=(10, 6))
player_of_match_count.head(10).plot(kind='bar')
plt.xlabel('Player')
plt.ylabel('Number of Player of the Match Awards')
plt.title('Top Players by Player of the Match Awards')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df.head(20)
batting_average = df.groupby('top_scorer')['highscore'].mean()
bowling_average = df.groupby('best_bowling')['first_ings_wkts'].mean()
plt.figure(figsize=(12, 6))
sns.barplot(x=batting_average.index, y=batting_average.values, label='Batting Average')
sns.barplot(x=bowling_average.index, y=bowling_average.values, label='Bowling Average')
plt.xlabel('Player')
plt.ylabel('Average')
plt.title('Batting and Bowling Averages for Top Players')
plt.xticks(rotation=45)
plt.legend()
plt.show()

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv("/Final Dataset - IPL.csv")
df.head(10)