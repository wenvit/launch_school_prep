##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

##### Solution

# This will print 1.
# `a` is initialized to 1 on line 6. This is a global variable.
# Within the definition of my_function on lines 8 & 9, `a` is 
# initialized to 2. This is a local variable, limited to the scope of 
# my_function. 
# On line 11, my_function is invoked but the function doesn't print 
# or return the local variable `a`
# The print function is invoked within the global scope on line 12, passing
# `a` as an argument. This is the global `a` because the 
# local value of `a` is only available wihin my_function