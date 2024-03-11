'''
URL: https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/13/section/11

Practice problems

You may use a web-based version of Python such as PyFiddle, Repl.It, or PythonFiddle to complete the exercises. Just make sure you are using version 3 or greater. If you use a web-based Python environment, you can easily share code with course instructors if you need help. You may also use a local installation of Python.

You should copy the entire code snippet into your Python editor. Your code should be placed in the area that says "student code goes here" highlighted in yellow. This is inside the function. When you run this entire code snippet, there are test cases below your code. Your output should match the expected output.
'''

from math import factorial, e, ceil
import random
import datetime as dt
import calendar

# Task 1
def calculate(x):
    return factorial(x)

print(calculate(3))  # expected outcome: 6
print(calculate(9))  # expected outcome: 362880

# Task 2
def selection(x):
    return random.choice(x)

print(selection(['apple', 'banana', 'orange', 'grape']))
print(selection([7, 5, 3, 9, 12, 4, 8, 10]))

# Task 3
def currentDate(x):
    seconds_in_a_day = 60 * 60 * 24
    total_seconds = x * seconds_in_a_day
    print(f"The total number of seconds is {total_seconds}.")

currentDate(4)  # expected outcome: The total number of seconds is 345600.0.
currentDate(7)  # expected outcome: The total number of seconds is 604800.0.

# Task 4
def currentDate():
    return f"The current date is {dt.date.today()}."

print(currentDate())  # Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

# Task 5
def mathCalculation(x):
    return ceil(x * e)

# expected outcome: 9
print(mathCalculation(3))

# expected outcome: 25
print(mathCalculation(9))

# Task 6
def countLeapYears(yearList):
    leap_years = [year for year in yearList if calendar.isleap(year)]
    return len(leap_years)

# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))

# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))

# Task 7
def printMonthName(monthNum):
    month_name = calendar.month_name[monthNum]
    print(month_name)

# expected output: March
printMonthName(3)

# expected output: November
printMonthName(11)

# Task 8
def printWeekdayName(year, month, day):
    weekday_name = calendar.day_name[calendar.weekday(year, month, day)]
    print(weekday_name)

# expected output: Friday
printWeekdayName(2001, 8, 31)

# expected output: Monday
printWeekdayName(2018, 10, 1)

# Task 9
def getRandom():
    return random.randrange(5, 8)

# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())

# Task 10
def add90Days(someDate):
    new_date = someDate + dt.timedelta(days=90)
    return new_date

# expected output: 2018-12-30
print(add90Days(dt.date(2018, 10, 1)))

# expected output: 2015-05-12
print(add90Days(dt.date(2015, 2, 11)))
