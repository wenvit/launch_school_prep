##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

##### Solution

# This will print 2.
# Variable `a` is initialized in the global scope to 1 on line 6.
# Within the body of my_function, on line 9, the `global a`
# statement tells python that the global variable `a` will be used
# within the scope of the function.
# Line 10 within the body of the function reassigns `a` to 2, 
# and because of the `global a` statement, it's the global `a`
# that is changed to 2. When my_function is invoked on line 12, the global `a` is
# reassigned to 2. Then when print is invoked passing in `a` as 
# an argument, it references the global `a`