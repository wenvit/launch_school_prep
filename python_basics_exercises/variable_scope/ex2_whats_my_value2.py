##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

##### Solution

# This code will raise an error.
# Line 6 initializes the variable x assigning it to the value 10
# in the code's global scope.
# Lines 8-10 define the my_function function. Line 9 in
# the function body reassigns the variable x to x + 5.
# Because the variable x is not initialized within the local scope
# of the function, it can't be reassigned. In python, you can't 
# reassign a global variable within the local scope of the function,
# unless you explicitly specify that's your intent using the 
# global keyword. You can access the value of a global variable
# within the local scope but you can't reassign it.

# The following is one way to fix this:

x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()