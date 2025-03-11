##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.


b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

##### Solution

# This will print [10, 2, 3]
# On line 7, the variable b is initialized by assigning it to
# a mutable list object [1, 2, 3]. This initialization is in the global scope.
# my_function (no parameters) mutates the global `b` by reassigning 
# the value at b[0] to 10 (index reassignment).
# When my_function is invoked on line 12, the mutation of global variable 
# `b` occurs. 
# Mutated value of global `b` is passed as an argument to the print function.