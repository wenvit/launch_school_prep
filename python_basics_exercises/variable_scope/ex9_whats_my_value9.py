##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

# a = 7

# def my_function(b):
#     b += 10

# my_function(a)
# print(a)

##### Solution

# This will print 7. 
# Variable `a` is initialized to 7 in global scope on line 6.
# Definition of my_function includes `b` as a parameter.
# Within function, `b` is reassigned by adding 10 to the number passed in
# to the function. The variable `b` is local to the scope of the function. 
# my_function is invoked on line 11, passing global `a` as argument to my_function.
# So `a` and `b` point to the same object (integer 7)
# when the function is invoked.
# Within function body, `b` is reassigned to 17 (b += 10)
# Because integers are immutable, the change to `b` 
# doesn't change the variable `a`. 
# The print function is invoked on line 12, passing `a` as argument. 
# This is the global `a` that isn't changed by my_function. 