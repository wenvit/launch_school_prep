##### Problem statement

# You come across the following code. 
# What errors does it raise for the given examples and 
# what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

#find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

##### Solution

# The function `find_first_nonzero_among` is defined in lines 7-10.
# It takes in one parameter called numbers.
# The body of the function has a `for` loop that loops over numbers.
# Within the `for` loop is an `if` statement that says if the number 
# does not equal 0, return the number.
# Line 12 invokes the find_first_nonzero_among function with 6 integers as arguments.
# This invocation of the function will generate a TypeError on the first line of the
# function definition because the function is
# expecting a single argument, and 6 are passed instead. 
# Line 13 invokes the find_first_nonzero_among function with a single integer as argument.
# This invocation raises an error (also TypeError) on the line of the `for` loop  
# because an integer is not iterable.

# Additional discussion from Launch School solution:
# Error messages output in this example are referred to as 'call stack'
# Traceback (most recent call last) -- most recent call will always be at the bottom of
# the error message. 