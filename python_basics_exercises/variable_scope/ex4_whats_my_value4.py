##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

##### Solution

# This will print 1.
# On line 6, the variable `a` is initialized to 1. This is 
# in the global scope.
# Within the body of the my_function function on line 9,
# the print function is invoked with the variable `a` as an argument.
# This print invocation is within the local scope of the function, but
# in this case where there's not a local definition of `a`, python will
# search in the global scope for `a` so it prints the value of `a`
# 