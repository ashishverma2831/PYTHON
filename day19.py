# Day 19 of 30DaysOfPython Challenge
# File Handling in Python

# .txt, .json, .xml, .csv, .tsv, .excel

# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

"""
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)



The default mode of open is reading, so we do not have to specify 'r' or 'rt'.
"""

# f = open('./files/reading_file_example.txt')
# print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

"""
read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.
"""

# f = open('./files/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# read(n): read n characters from the file
# f = open('./files/reading_file_example.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# readline(): read only the first line
# f = open('./files/reading_file_example.txt')
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# readlines(): read all the lines and return it as a list of strings
# f = open('./files/reading_file_example.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# splitlines(): read all the lines and return it as a list of strings without newline character 
# f = open('./files/reading_file_example.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

"""
To write to an existing file, we must add a mode as parameter to the open() function:

"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.
"""

# The method below creates a new file, if the file does not exist
# with open('./files/writing_file_example.txt','w') as f:
    # f.write('This text will be written in a newly created file')

# import os
# os.remove('./files/example.txt')

# import os
# if os.path.exists('./files/example.txt'):
    # os.remove('./files/example.txt')
# else:
    # print('The file does not exist')



# Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# csv
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# Excel files
# import xlrd
# # excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

# <?xml version="1.0"?>
# <person gender="female">
#   <name>Asabeneh</name>
#   <country>Finland</country>
#   <city>Helsinki</city>
#   <skills>
#     <skill>JavaScrip</skill>
#     <skill>React</skill>
#     <skill>Python</skill>
#   </skills>
# </person>

