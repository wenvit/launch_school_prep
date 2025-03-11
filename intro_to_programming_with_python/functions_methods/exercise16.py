# 16. In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names

# multiply - defined on line 4, used on line 12
# get_num - defined on line 7, used on lines 10 & 11
# float - built-in function used on line 8
# input - built-in function used on line 8
# print - built-in function used on line 13

# Parameters

# left & right - defined on line 4, used as local variables on line 5
# prompt - defined on line 7, used as local variable on line 8