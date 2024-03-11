'''
URL: https://srm--c.vf.force.com/apex/coursearticle?Id=kA00c000001DYiRCAW
COMPETENCY 2: The graduate constructs functions and control structures (if/elif/else, for, while) to interact with data structures (lists, sets, dictionaries, tuples) and direct program flow.
'''

# Task 1
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(7, 9))  # expected outcome: 16
print(add_two_numbers(20, 49))  # expected outcome: 69

# Task 2
myNewSum = add_two_numbers(2, 8)
print(myNewSum)  # expected outcome: 10

# Task 3
def grade_report(score):
    if score >= 90:
        return "You received an A and have passed the course."
    elif score >= 80:
        return "You received a B and have passed the course."
    elif score >= 0:
        return "You have not passed the course. Please retake the exam."
    else:
        return "You have not attempted the exam. Please schedule it."

print(grade_report(90))
print(grade_report(70))

# Task 4
for num in range(6, 13):
    print(num)

# Task 5
myNames = ['Dana', 'Cemal', 'Jessica', 'Mike', 'Dana']

# Task 6
print(len(myNames))  # expected outcome: 5

# Task 7
if 'David' not in myNames:
    myNames.append('David')
print(myNames)  # expected outcome: ['Dana', 'Cemal', 'Jessica', 'Mike', 'Dana', 'David']

# Task 8
names_str = ', '.join(myNames)
print(names_str)  # expected outcome: Dana, Cemal, Jessica, Mike, Dana, David

# Task 9
selected_names = ["Mike", "Dana"]
print(selected_names)

# Task 10
unique_names = list(set(myNames))
print(unique_names)  # expected outcome: ['Dana', 'Cemal', 'Jessica', 'Mike', 'David']

# Task 11
for name in unique_names:
    print(f"Welcome to WGU, {name}")

# Task 12
for employee, salary in employeeDatabase.items():
    new_salary = salary * 1.02
    print(f"{employee}, your current salary is {salary:.2f}. You received a 2% raise. This makes your new salary {new_salary:.2f}")

# Task 13
leap_years = [year for year in range(2000, 2021) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print(f"These are the leap years: {leap_years}")

# Task 14
temperature = 98.0
while temperature < 104.0:
    temperature += 0.5
print(f"The temp has reached {temperature:.1f}")

# Task 15a
wgu_phone_number = (8, 7, 7, 4, 3, 5, 7, 9, 4, 8)

# Task 15b
print(wgu_phone_number[-4:])  # expected outcome: 7948

# Task 15c
phone_number_str = '-'.join(map(str, wgu_phone_number))
print(f"Call WGU now at {phone_number_str}")

# Task 16
def fruitFunction(fruits):
    return ' '.join(fruits[:2])

print(fruitFunction(['banana', 'apple', 'orange', 'grapes', 'pineapple']))  # expected outcome: banana apple
print(fruitFunction(['mango', 'avocado', 'pear']))  # expected outcome: mango avocado

# Task 17
def fruitFunction2(fruits):
    return 'avocado is in the list' if 'avocado' in fruits else 'avocado not found'

print(fruitFunction2(['pear', 'apple', 'lemon', 'grapes', 'pineapple']))  # expected outcome: avocado not found
print(fruitFunction2(['lime', 'avocado', 'pear']))  # expected outcome: avocado is in the list

# Task 18
def favFoods(x):
    return x.count('pizza')

print(favFoods(['apple', 'banana', 'pizza', 'Pizza', 'ice cream', 'cupcakes']))  # expected output: 2
print(favFoods(['almonds', 'spaghetti', 'pizza', 'kombucha', 'Pizza', 'pizza']))  # expected output: 3

# Task 19
def makeList(names):
    return names.split()

print(makeList('Jessica John Paul Grace Ginger Billy Arlene'))  # expected output: ['Jessica', 'John', 'Paul', 'Grace', 'Ginger', 'Billy', 'Arlene']
print(makeList('David Cemal Dana Rodger Jerry Jessica Mike'))  # expected output: ['David', 'Cemal', 'Dana', 'Rodger', 'Jerry', 'Jessica', 'Mike']

# Task 20
def costCount(purchases):
    return sum(purchases)

print(costCount([39.90, 40.21, 8.73, 9.57]))  # expected output: 98.41
print(costCount([139.90, 10.11, 1.53, 3.57]))  # expected output: 155.10999999999999
