# 14. Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply - name of function on line 3
# left & right - parameters for multiply function on line 3
# left & right - local variables (or still parameters??) on line 4
# get_num - name of function on line 6
# prompt - parameter for get_num function on line 6
# float & input - built-in function names on line 7
# prompt - argument passed to input function on line 7
# first_number - global variable initialized to the return value 
#                of get_num function on line 9
# second_number - variable initialized to the return value
#                 of get_num function on line 10
# get_num - function invoked on lines 9 & 10
# product - variable initialized to the return value of multiply
#           function on line 11
# multiply - function name invoked on line 11
# first_number & second_number - arguments passed to multiply
#                                function on line 11
# print - function invoked on line 12
# first_number, second_number, product - arguments passed as 
#                          f-string interpolation to print function on line 12