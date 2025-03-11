##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

##### Solution

# This will print 1.
# On line 7, the local variable `a` is initialized to a value of 1 
# within the body of my_function.
# The if statement within the function body evaluates to truthy
# because the boolean True is truthy
# So the if block executes by invoking the print function with
# the variable `a` as an argument
# The local variable `a` is accessible anywhere within the 
# scope of the function, including the if statement
# my_function is invoked on line 12
