# Day 12 of 30DaysOfPython Challenge
# Modules in Python 

"""
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.
"""

"""
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
"""

# from day11 import sum_all_nums
# print(sum_all_nums(1,2,3,4,50)) # 60

# import day11
# print(day11.sum_all_nums(1,2,3,4,50)) # 60


"""
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
"""


"""
Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re
"""

# import the module
import os
# Creating a directory
# os.mkdir('directory_name')
# Changing the current directory
# os.chdir('path')
# Getting current working directory
# os.getcwd()
# Removing directory
# os.rmdir()


"""
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
"""

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# python script.py Asabeneh 30DaysOfPython
# Welcome Asabeneh. Enjoy  30DayOfPython challenge! 

# to exit sys
# sys.exit()
# To know the largest integer variable it takes
# sys.maxsize
# To know environment path
# sys.path
# To know the version of python you are using
sys.version
print(sys.version)

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
print(variance(ages))   # ~5.3
print(pstdev(ages))     # ~2.2
print(pvariance(ages))  # ~4.9
print(fmean(ages))      # ~22.9
print(harmonic_mean(ages)) # ~21.7
print(median_low(ages))   # 22
print(median_high(ages))  # 23
print(multimode(ages))    # [20, 22, 26]
print(quantiles(ages))    # [21.5, 23.0, 25.0]
print(sorted(ages))       # [4, 20, 20, 20, 22, 22, 23, 24, 25, 26, 26]
print(sum(ages))          # 252


import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base


from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

from math import pi as  PI
print(PI) # 3.141592653589793

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.printable)     # all printable characters
# print(string.whitespace)    #  \t\n\r\x0b\x0c

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

# Exercises
# Writ a function which generates a six digit/character random_user_id
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

print(rgb_color_gen())