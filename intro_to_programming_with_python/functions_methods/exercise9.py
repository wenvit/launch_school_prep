# 9. Without running the following code, what do you think it will do?

def foo(first, second = 3, third = 2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

#######################

# This code will print the values 42, 3.141592, and 2.718
# on separate lines.

# The definition of the function foo begins on line 3 with three parameters:
# first, second, and third. 
# The second and third parameters are given default values of 3 and 2, respectively.
# In The body of the function (lines 4-6), the print function is invoked 
# with the arguments first, second, and third. 
# When foo is invoked on line 8, the values 42, 3.141592, and 2.718 are 
# passed as arguments to the function. The arguments passed for the second and third
# parameters supercede the default values
