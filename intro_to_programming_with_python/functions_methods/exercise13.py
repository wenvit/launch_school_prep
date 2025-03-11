# 13. Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

#####################
# This code snippet will result in an error

# The definition of the function foo begins on line 3. It has three parameters: 
# first, second, and third. The second parameter has a default value of 3, and 
# the third parameter doesn't have a default.
# python will generate an error when a parameter without a default value
# follows a parameter with a default.
# Once a default value is set, all subsequent positional parameters must have defaults.
# Note that this is a syntax error where the function is defined, not invoking
# the function foo