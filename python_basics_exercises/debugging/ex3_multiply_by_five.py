##### Problem statement

# When the user inputs 10, we expect the program to print 
# The result is 50!, but that's not the output we see. Why not?

# def multiply_by_five(n):
#     return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = input()

# print(f"The result is {multiply_by_five(number)}!")

##### Solution

# This code as written prints 'The result is 1010101010!' when 
# 10 is input.
# This unexpected result results from the `input` function on line 10
# returning the value input by the user as a string. 
# The multiply_by_five function definition on lines 6 & 7 
# has a parameter `n`. It returns n * 5.
# On line 10, the variable `number` is assigned to the string value 
# returned by the `input` function. 
# On line 12, the print function is invoked with an f-string as the argument. 
# Within the f-string, the multiply_by_five function is invoked
# with the argument `number`. 
# As written, because `number` is a string, the multiply_by_five
# return value is the string repeated 5 times. 

# Here's a fix

# Use int constructor function to coerce the value input by the user
# from a string to an integer

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())   

print(f"The result is {multiply_by_five(number)}!")

# Additional discussion from Launch School solution:
# After adding the int constructor function, the code
# will now raise a ValueError if the user inputs something that
# can't be converted to an integer. 