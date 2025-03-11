# 12. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

#####################
# This code snippet will result in an error

# The definition of the function foo begins on line 3. It has three parameters: 
# first, second, and third. The second and third parameters have default
# values of 3 and 2 respectively.
# When foo is invoked on line 8, no arguments are passed.
# Because foo is expecting at least one argument, it results in an error.