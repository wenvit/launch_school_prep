##### Problem statement

# Rewrite your code from the previous exercise 
# to use a ternary expression.

##### Solution

# syntax of ternary expressions:
# expression1 if condition else expression2

import random

random_number = random.randint(0, 1)

print(random_number)

# print('Yes!') if random_number else print('No')
# This syntax above is ok but generally speaking, 
# ternary expressions
# are used for choosing between two values, not taking
# different actions

# This is better, have ternary expression return a string
# pass the return value from ternary expression as argument
# to print function

print('Yes!' if random_number else 'No')