# 15. Using the code below, classify the identifiers as global, local, 
# or built-in. For our purposes, you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

## Global identifiers
# multiply, get_num, first_number, second_number, product

## Local identifiers
# left, right, prompt

## Built-in identifiers -- can be accessed anywhere in code
# float, input, print

#########

# multiply - global function (line 4)
# left and right - local parameters/variables for multiply function (line 4 & 5)
# get_num - global function (line 7)
# prompt - local parameter/variable (line 7 & 8)
# float - built-in function (line 8)
# input - build-in function (line 8)
# first_number - global variable initialization (line 10)
# get_num - global function (line 10 & 11)
# second_number - global variable initialization (line 11)
# product - global variable initialization (line 12)
# multiply - global function (line 12)
# first_number & second_number - global variables used as arguments to multiply function (line 12)
# print - built-in function (line 13)
# first_number, second_number, product - global variables used in f-string interpolation
#                                       argument to print function (line 13)