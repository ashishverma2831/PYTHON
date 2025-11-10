# Day 10 of 30 DaysOfPython Challenge
# Looping Statements in Python

"""

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

while loop
for loop
"""

"""
# syntax
while condition:
    code goes here
"""

count = 0
while count < 5:
    print(count)
    count += 1
#prints from 0 to 4

"""
# syntax
while condition:
    code goes here
else:
    code goes here
"""

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

"""
# syntax
while condition:
    code goes here
    if another_condition:
        break
"""

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

"""
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
"""

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count += 1


"""
# syntax
for iterator in lst:
    code goes here
"""

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


"""
The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end).
"""

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

"""
# syntax
for iterator in range(start, end, step):
"""

"""
# syntax
for x in y:
    for t in x:
        print(t)
"""

"""
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
"""


"""
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
"""

for number in range(6):
    pass


# Exercises

for i in range(1,8):
    print(' ')
    for j in range(1,8):
        if j <= i:
            print('#', end=' ')