##### Problem statement

# What will the following code do and why? 
# Don't run it until you have tried to answer.

# if True:
#     my_value = 20

# print(my_value)

# What do you think will happen if we run the following code instead:

if False:
    my_new_value = 42

print(my_new_value)

##### Solution

# Line 6-7 is an if statement that sets
# my_value to 20 if the condition is truthy.
# Because boolean True is truthy, my_value is set to 20.
# Line 9 invokes print function, passing my_value as an argument
# The print function has access to my_value 
# because it's in the global scope.

# More discussion from Launch School solution:
# Variables initialized inside an `if`, `match`,
# `while`, `for`, `with`, or `try` statement.
# This entire code snippet only has a single scope.

# In the alternative scenario, the `if False` statement
# is falsy, so the variable isn't initialized. It isn't a
# scoping problem, but it raises an error flag because
# the variable is never initialized.

# Specifically, after I ran this, it's a NameError with 
# with a message my_new_value is not defined