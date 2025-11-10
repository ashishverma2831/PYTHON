# Day 9 of 30DaysOfPython Challenge
# Conditional Statements in Python

"""
By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
"""

"""
# syntax
if condition:
    this part of code runs for truthy conditions
"""

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

"""
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
"""

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')


"""
# syntax
if condition:
    code
elif condition:
    code
else:
    code
"""

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# syntax
# code if condition else code

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# Nested if statements
"""
# syntax
if condition:
    code
    if condition:
    code
"""

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

"""
# syntax
if condition and condition:
    code
"""

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

"""
# syntax
if condition or condition:
    code
"""

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


# Exercises
# Write an if statement that assigns 'adult' to a variable called status if age is greater than or equal to 18, and 'minor' otherwise.

age = int(input("Enter your age: "))
if age >= 18:
    print('You are an adult.')
else:
    age_count = 18 - age
    print(f'You are a minor. {age_count} years left to be an adult.')