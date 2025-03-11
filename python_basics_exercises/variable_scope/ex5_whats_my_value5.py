##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

##### Solution

# This raises an error.
# On line 6, the variable `a` is initialized to 1. This is in
# the global scope.
# Within the body of my_function, print is invoked on line 9, 
# passing `a` as the argument. Because on the next line, the variable `a` 
# is assigned to 2, python treats `a` as a local variable within the 
# scope of my_function. The local `a` supercedes the global `a` within 
# the scope of my_function. Because print is invoked before the 
# local variable `a` is assigned, it raises an error (UnboundLocalError)

# More discussion from Launch School solution:
# No matter where it happens in function, if we try to assign a variable
# within a function, python will treat it as a local variable if global
# keyword hasn't been used.
