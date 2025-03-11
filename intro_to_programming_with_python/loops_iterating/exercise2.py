# 2. Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop to display the future ages.

########################
# Exercise 3 from Input/Output chapter copied over: 
# Write a program named age.py that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years from now. 
# Here's the output for someone who is 27 years old.

# age = input("Please enter your current age: ")
# age = int(age)  # convert age input as a string to an integer to do math

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 20 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

########################
# Here's a refactor using a for loop:

age = input("Please enter your current age: ")
age = int(age)  # convert age input as a string to an integer to do math

print(f'You are {age} years old.')

# range is flexible and dynamic -- can more easily change future years of interest
future_years = range(10, 50, 10) 

for year in future_years:
    print(f'In {year} years, you will be '
          f'{age + year} years old.')
