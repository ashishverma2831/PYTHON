# Day 25 of 30DaysOfPython Challenge
# Pandas Library for Data Analysis

"""
Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:

reshaping
merging
sorting
slicing
aggregation
imputation. If you are using anaconda, you do not have install pandas.
"""


# pip install conda
# pip install pandas

# Pandas data structure is based on Series and DataFrames.

# A series is a column and a DataFrame is a multidimensional table made up of collection of series. In order to create a pandas series we should use numpy to create a one dimensional arrays or a python list.

"""
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
"""

# import pandas as pd

# nums = [1, 2, 3, 4,5]
# s = pd.Series(nums)
# print(s)


'''
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)
'''

# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

# s = pd.Series(10, index = [1, 2, 3])
# print(s)


# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)


# Creating DataFrame 
"""
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
"""

# data = [
#     {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
#     {'Name': 'David', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
# df = pd.DataFrame(data)
# print(df)


"""
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
"""

# print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# print(df.shape) # as you can see 10000 rows and three columns

# print(df.columns)

# he describe() method provides a descriptive statistical values of a dataset.

# print(heights.describe()) # give statisical information about height data

"""
Modifying a DataFrame: * We can create a new DataFrame * We can create a new column and add it to the DataFrame, * we can remove an existing column from a DataFrame, * we can modify an existing column in a DataFrame, * we can change the data type of column values in the DataFrame
"""

# adding a new column
# weights = [74, 78, 69]
# df['Weight'] = weights
# df

# df['Height'] = df['Height'] * 0.01
# df

# Using functions makes our code clean, but you can calculate the bmi without one
# def calculate_bmi ():
#     weights = df['Weight']
#     heights = df['Height']
#     bmi = []
#     for w,h in zip(weights, heights):
#         b = w/(h*h)
#         bmi.append(b)
#     return bmi
    
# bmi = calculate_bmi()


# df['BMI'] = round(df['BMI'], 1)
# print(df)

# datatype
# print(df.Weight.dtype)


