# 11. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

#################
# This code snippet will print values of 42, 3, and 2 on separate lines

# The definition of the function foo begins on line 3. It has three parameters: 
# first, second, and third. The second and third parameters have default
# values of 3 and 2 respectively.
# In the body of the function (lines 4-6), the local variables first, second, 
# and third are passed as arguments to the print function. 
# When foo is invoked on line 8, a single positional arguments of 42 is passed.
# foo will assign the single argument to the first parameter.
# Since only a single argument is passed, foo uses the 
# default values of 3 and 2 for the 2nd and 3rd parameters, respectively.