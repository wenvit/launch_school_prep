# 1. What happens when you run the following program?
#  Why do we get that result?

# def set_foo():
    # foo = 'bar'

# print(set_foo())  added this to check return value
# set_foo()
# print(foo)

################

# Running this code results in an error

# The set_foo function definition begins on line 4. 
# The function has no parameters.  
# The function simply initializes a local variable foo 
# by assigning it to the string value of 'bar'
# and returns a default value of None.
# The function set_foo is invoked on line 8 without passing any arguments.
# After invoking set_foo, the variable foo has a local value
# limited to the scope of the function but is not defined in the global scope 
# outside the function. 
# Invoking the print function with the variable foo on line 9
# outside set_foo results in an error because it doesn't 
# find a value for foo.

###########################
# One way to fix

# def set_foo():
#     foo = 'bar'
#     return foo

# foo = set_foo()
# print(foo)

#######################
# Another way 

# def set_foo():
#     foo = 'bar'
#     print(foo)

# set_foo()
