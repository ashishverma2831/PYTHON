# Day 6 - 30DaysOfPython Challenge
# Tuples in Python

"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple
"""

# Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# syntax
tpl = ('item1', 'item2','item3')

# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)  # 3

# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

# Changing tuple to list 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print('List:', lst)

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

# Joining tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# Deleting a tuple
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
