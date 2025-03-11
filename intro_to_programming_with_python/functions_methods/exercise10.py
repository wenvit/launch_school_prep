# 10. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

#####################
# This code will print the values 42, 3.141592 and 2 on separate lines.

# The definition of the function foo begins on line 3. It has three parameters: 
# first, second, and third. The second and third parameters have default
# values of 3 and 2 respectively.
# In the body of the function (lines 4-6), the local variables first, second, 
# and third are passed as arguments to the print function. 
# When foo is invoked on line 8, the positional arguments of 42 and 3.141592 are passed.
# foo will assign the first two positional arguments to the first and 
# second parameters. Since a 3rd argument wasn't passed, foo uses the 
# default value of 2 for the third parameter.