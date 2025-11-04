# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple



# Exercise 
# 1. Check the python version you are using
# Python 3.13.1
# Python3 3.14.0

"""2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
"""
print(3 + 4)   # addition
print(3 - 4)   # subtraction
print(3 * 4)   # multiplication
print(3 % 4)   # modulus
print(3 / 4)   # division
print(3 ** 4)  # exponential
print(3 // 4)  # floor division operator

"""3. Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
"""

print("John")                     # Your name
print("Doe")                      # Your family name
print("USA")                      # Your country
print("I am enjoying 30 days of python")  # I am enjoying 30 days of python

"""4. Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country"""

print(type(10))                     # Int
print(type(9.8))                    # Float
print(type(3.14))                   # Float
print(type(4 - 4j))                 # Complex
print(type(['Asabeneh', 'Python', 'Finland']))  # List
print(type("John"))                 # String
print(type("Doe"))                  # String
print(type("USA"))                  # String


# 5. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

# Integer
num1 = 10
print(type(num1))  # Output: <class 'int'>

# Float
num2 = 3.14
print(type(num2))  # Output: <class 'float'>

# Complex
num3 = 2 + 3j
print(type(num3))  # Output: <class 'complex'>

# String
name = "Alice"
print(type(name))  # Output: <class 'str'>

# Boolean
is_student = True
print(type(is_student))  # Output: <class 'bool'>

# List
fruits = ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>

# Tuple
coordinates = (10.0, 20.0)
print(type(coordinates))  # Output: <class 'tuple'>

# Set
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))  # Output: <class 'set'>

# Dictionary
person = {'name': 'Bob', 'age': 25}
print(type(person))  # Output: <class 'dict'>

# 6. Find an Euclidian distance between (2, 3) and (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.dist(point1, point2)
print(distance) 

distance = math.sqrt((10 - 2) ** 2 + (8 - 3) ** 2)
print(distance)  # Output: 9.433981132056603