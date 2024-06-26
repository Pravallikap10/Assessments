# -*- coding: utf-8 -*-
"""4370IApython2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fpm24f_ZzqL82LGwREDgZnQoPn8pi8kB
"""

#1
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(f"Min: {np.min(array)}")
print(f"Max: {np.max(array)}")
print(f"Sum: {np.sum(array)}")
print(f"Mean: {np.mean(array)}")
print(f"Standard Deviation: {np.std(array)}")

#2
import numpy as np
def normalize_health_data(data):
    mean = data.mean(axis=0)
    std = data.std(axis=0)
    normalized_data = (data - mean) / std
    return normalized_data
health_data = np.array([[160, 70, 30], [165, 65, 35], [170, 75, 40]])
normalized_health_data = normalize_health_data(health_data)
print(normalized_health_data)

#3
import numpy as np
scores = np.array([
    [80, 90, 78, 85, -1],
    [70, 95, 88, -1, 92],
    [88, 92, -1, 90, 91],
    [65, 75, 80, 85, 90]])
def calculate_average_last_three_subjects(scores):
    averages = np.array([np.mean(row[row != -1][-3:]) for row in scores])
    return averages
average_scores = calculate_average_last_three_subjects(scores)
print(average_scores)

#4
import numpy as np
start_temp = 15
end_temp = 25
num_readings = 24
temperature_readings = np.linspace(start_temp, end_temp, num_readings)
print(temperature_readings)

#5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
moving_averages = np.convolve(daily_closing_prices, np.ones(window_size)/window_size, mode='valid')
print(moving_averages)

#6
import numpy as np
mean_vector = [0, 0]
covariance_matrix = [[1, 0.5], [0.5, 2]]
synthetic_data = np.random.multivariate_normal(mean_vector, covariance_matrix, 100)
print(synthetic_data[:5])

#7
import numpy as np
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
determinant = np.linalg.det(properties_matrix)
print(f"matrix: {determinant}")

#8
import numpy as np
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
filtered_array = array[array > 5]
print(filtered_array)

#9
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, 35, 40, 45, 50, 55],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}
filtered_data = [(name, city) for name, age, city,
                 department in zip(data['Name'], data['Age'],
                                   data['City'], data['Department'])
                 if age < 45 and department != 'HR']
print("(Name, City):")
for name, city in filtered_data:
    print(f"{name}, {city}")

#10
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
fruit_data = [(product, price, promotion) for product, category,
              price, promotion in zip(data['Product'],
                                      data['Category'], data['Price'],
                                      data['Promotion']) if category == 'Fruit']
average_price = sum(price for product, price,
                    promotion in fruit_data) / len(fruit_data)
candidates_promotion = [product for product, price,
                            promotion in fruit_data
                            if price > average_price and not promotion]
print(candidates_promotion)

#11
import pandas as pd
data = {
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales': [70000, 50000, 30000, 40000, 60000]}
df = pd.DataFrame(data)
avg_sales_per_salesperson = df.groupby('Department')['Sales'].mean().reset_index()
avg_sales_per_salesperson['Rank'] = avg_sales_per_salesperson['Sales'].rank(ascending=False)
avg_sales_per_salesperson = avg_sales_per_salesperson.sort_values(by='Rank')
print(avg_sales_per_salesperson)

#12
import pandas as pd
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']}
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']}
employee_df = pd.DataFrame(employee_data)
project_df = pd.DataFrame(project_data)
merged_df = pd.merge(employee_df, project_df, on='Employee', how='left')
merged_df['Project'].fillna('No Project', inplace=True)
print(merged_df)

#13
import pandas as pd
df = pd.read_csv(

#14
NA

#15
NA