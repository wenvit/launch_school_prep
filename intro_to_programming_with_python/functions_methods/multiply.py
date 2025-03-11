# 3. Write a program that uses a multiply function to multiply 
# two numbers and returns the result. Ask the user to enter 
# the two numbers, then output the numbers and result as a 
# simple equation.
##########################
# First solution

# def multiply_nums(a, b):
#     return a * b

# a = float(input('Enter a number: '))
# b = float(input('Enter another number: '))
# product = multiply_nums(a, b)

# print(f'{a} x {b} = {product}')

#########################
# Launch School solution that creates a separate function for 
# handling data input and convert to float
# Breaking a problem down into smaller pieces
# makes code cleaner, reduces  repetition, and is more 
# modular, which makes more adaptable/easier to add functionality later

def multiply(first_num, second_num):
    return first_num * second_num

def enter_numbers(prompt):
    number = input(prompt)
    return float(number)

first_num = enter_numbers('Enter a number: ')
second_num = enter_numbers('Enter another number: ')

product = multiply(first_num, second_num)

print(f'{first_num} x {second_num} = {product}')