'''
URL: https://srm--c.vf.force.com/apex/coursearticle?Id=kA00c000001DYiMCAW
COMPETENCY 1: The graduate integrates Python elements including data types, constants, variables, operators, and expressions to create programming solutions.
'''
# Task 1
# declare 3 variables with one assignment statement and assign each one an integer value
var1, var2, var3 = 5, 10, 15


# Task 2
# convert each of your previous variables to float objects
var1 = float(var1)
var2= float(var2)
var3 = float(var3)

# Task 3
# convert each of your previous variables to string objects
var1 = str(var1)
var2 = str(var2)
var3 = str(var3)

# Task 4
# Print the result of dividing 783.56 by 123.2 and ensure that the answer results in an integer
# expected outcome: 6
result = int(783.56 / 123.2)
print(result)

# Task 5
# Determine if 2019 is a leap year and print the result.
# expected outcome: 3 (?)
year = 2019
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(isLeapYear)

# Task 6
# Print the calculated length of myFirstString.
# expected outcome: 35
myFirstString = 'I love working with Python so much!'
length_of_string = len(myFirstString)
print(length_of_string)


# Task 7
# Create a string value and print it with the first letter of each word capitalized using a Python method.
string_with_capitalized_first_letters = 'hello world'.title()
print(string_with_capitalized_first_letters)

# Task 8
# Create a string value and determine if the string consists of only lowercase characters. Print the results.
# expected outcome: True or False
string_to_check = 'abc123'
is_lowercase = string_to_check.islower()
print(is_lowercase)

# Task 9
# Use the given variable to construct a python statement that counts how many times the word pizza is used. Print the final count.
# expected outcome: 3
commercial = 'In the Little Ceasars pizza commercial the character says, "pizza, pizza"!'
word_to_count = 'pizza'
count_of_word = commercial.lower().count(word_to_count)
print(count_of_word)

# Task 10
# Use the given username and phone to create a message that lets the user know that you will be calling
# at a specified number for your appointment. Use the format method to insert data into the printed message.
# expected outcome:
# Hi, Allen. I will call you at 888-555-0011 for our appointment.
username = 'Allen'
phone = 8885550011
message = "Hi, {}. I will call you at {} for our appointment.".format(username, phone)
print(message)
