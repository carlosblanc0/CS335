'''
URL: https://srm--c.vf.force.com/apex/coursearticle?Id=kA00c000001DYiWCAW

COMPETENCY 3: The graduate writes code in the Python environment, incorporating libraries to support data analytics tasks including data collection, manipulation, and storage.

Note: These exercises were originally written for v3 of C859, not v4. That OA focused more on modules like datetime, calendar, os, and random. These are not required for the v4 OA.

For v4, the most important modules are math and csv. It is also important to be comfortable using the built-in open() function to open files. The filestream methods read(), readlines(), and write() are also important for this competency.

Just because a Lab or exam question has an import statement for the csv module does not mean you must use it. If you are more comfortable using readlines() than the csv method csv.reader() to break down a csv or tsv file's data, by all means use that method. As long as you meet all requirements of the question and stand up to unit testing, it doesn't matter how you get there.

When importing Python code modules, make sure to understand the differing syntax of full imports vs partial imports vs aliased imports.
'''

# ---- Math Module ---
import math

# Task 1
print(math.factorial(7))  # expected outcome: 5040

# Task 2
print(math.sqrt(27))  # expected outcome: 5.196152422706632

# Task 3
print(math.floor(15.87))  # expected outcome: 15

# Task 4
print(math.ceil(15.87))  # expected outcome: 16

# Task 5
print(math.exp(4))  # expected outcome: 54.598150033144236

# Task 6
def nearest(x):
    print(round(x))

nearest(15.87)  # expected result: 16
nearest(7.21)  # expected result: 7

# Task 7
def square(x):
    print(round(math.sqrt(x)))

square(38)  # expected result: 6
square(58)  # expected result: 8

# ---- Random Module ---
import random

# Task 1
print(random.randint(2, 19))  # print a random integer between 2 and 20, exclusive

# Task 2
print(random.randint(1, 100))  # print a random number from the range 1 to 100, inclusive

# Task 3
print(random.random())  # print a random floating point number

# Task 4
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
print(random.choice(word_list))  # return a random element from the list

# ---- OS Module ---
import os

# Task 1
os.link("C://myfile.txt", "C://myPython/myfile.txt")

# Task 2
os.remove("C://myfile.txt")

# Task 3
print(os.getcwd())

# Task 4
os.chdir("C://home/")

# ---- Datetime Module ---
import datetime

# Task 1
print(datetime.datetime.now().year)

# Task 2
print(datetime.datetime.now().month)

# Task 3
print(datetime.datetime.now().day)

# Task 4
four_days_seconds = 4 * 24 * 60 * 60
print(four_days_seconds)

# Task 5
one_year_later = datetime.datetime.now() + datetime.timedelta(days=365)
print(one_year_later)

# ---- Lookup ---
# Task 1
# You can use the help() function to get information on the datetime module or any other module.
# To look up a specific method within the datetime module, you can use help(datetime) and navigate to the relevant section.

# Task 2
# To see only a list of methods associated with a type of object, you can use the dir() function.
print(dir(str))
