# Day 24 of 30DaysOfPython Challenge
# Statistics with Python

"""
Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part. After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decisions based on data, data tells as they say.
"""

"""
What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. If data is not put in a context, it doesn't make any sense to a human or computer. To make sense from data we need to work on the data using different tools.

The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created. There are structured and unstructured data.

Data can be found in small or big format. Most of the data types we will get have been covered in the file handling section.
"""

"""
The Python statistics module provides functions for calculating mathematical statistics of numerical data. The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.
"""

"""
In the first section we defined Python as a great general-purpose programming language on its own, but with the help of other popular libraries as(numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.

NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.

So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access jupyter notebook let's install anaconda. If you are using anaconda most of the common packages are included and you don't have install packages if you installed anaconda.

# pip install numpy
"""

"""
    # How to import numpy
    import numpy as np
    # How to check the version of the numpy package
    print('numpy:', np.__version__)
    # Checking the available methods
    print(dir(np))
"""

# creating Numpy Array
    # # Creating python List
    # python_list = [1,2,3,4,5]

    # # Checking data types
    # print('Type:', type (python_list)) # <class 'list'>
    # #
    # print(python_list) # [1, 2, 3, 4, 5]

    # two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

    # print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # # Creating Numpy(Numerical Python) array from python list

    # numpy_array_from_list = np.array(python_list)
    # print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    # print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# Creating float type Numpy array
    # Python list
    # python_list = [1,2,3,4,5]

    # numy_array_from_list2 = np.array(python_list, dtype=float)
    # print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

# Creating boolean type Numpy array
    # numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    # print(numpy_bool_array) # array([False,  True,  True, False, False])

# Creating multidimensional Numpy array
    # two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
    # numpy_two_dimensional_list = np.array(two_dimensional_list)
    # print(type (numpy_two_dimensional_list))
    # print(numpy_two_dimensional_list)

# We can always convert an array back to a python list using tolist().
# np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())


"""
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
"""

"""
The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. If the array is just one dimensional it returns the size of the array.
"""

"""
    nums = np.array([1, 2, 3, 4, 5])
    print(nums)
    print('shape of nums: ', nums.shape)
    print(numpy_two_dimensional_list)
    print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
    three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10, 11]])
    print(three_by_four_array.shape)
"""

"""
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
"""

"""
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3
"""

"""
NumPy array is not like exactly like python list. To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. Mathematical Operation:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)
"""

#Int,  Float numbers
# numpy_int_arr = np.array([1,2,3,4])
# numpy_float_arr = np.array([1.1, 2.0,3.2])
# numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

# print(numpy_int_arr.dtype)
# print(numpy_float_arr.dtype)
# print(numpy_bool_arr.dtype)

"""
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
"""

# two_dimension_array[::]
# two_dimension_array[::-1,::-1]


"""
    # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
"""

"""
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
"""

"""
flattened = reshaped.flatten()
flattened
"""

"""
    ## Horitzontal Stack
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

    ## Vertical Stack
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
"""

#     # Generate a random float  number
    # random_float = np.random.random()
    # random_float

    # Generating a random integers between 2 and 11, and creating a one row array
    # random_int = np.random.randint(2,10, size=4)
    # random_int

"""
    # np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array
"""





"""
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
"""

# four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))

# Similar to range arange numpy.arange(start, stop, step)
# whole_numbers = np.arange(0, 20, 1)
# whole_numbers

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
# np.linspace(1.0, 5.0, num=10)x

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

# np.logspace(2, 4.0, num=4)


"""
NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile,standard deviation and variance, etc from the given elements in the array. The functions are explained as follows − Statistical function Numpy is equipped with the robust statistical function as listed below

Numpy Functions
Min np.min()
Max np.max()
Mean np.mean()
Median np.median()
Varience
Percentile
Standard deviation np.std()
"""

# a = [1,2,3]

# Repeat whole of 'a' two times
# print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
# print('Repeat: ', np.repeat(a, 2))


# Random numbers between [0,1) of shape 2,3
# r = np.random.random(size=[2,3])
# print(r)

# print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))


"""
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
"""

# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()

"""
# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)
"""

## Linear algebra
### Dot product: product of two arrays
# f = np.array([1,2,3])
# g = np.array([4,5,3])
### 1*4+2*5 + 3*6
# np.dot(f, g)  # 23


### Matmul: matruc product of two arrays
# h = [[1,2],[3,4]]
# i = [[5,6],[7,8]]
### 1*5+2*7 = 19
# np.matmul(h, i)

"""
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
"""

