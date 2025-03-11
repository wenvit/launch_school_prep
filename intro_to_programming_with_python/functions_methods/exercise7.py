# 7. Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo('Hello')

#########################

# Running this code will result in an error message.
# Cannot pass fewer arguments than parameters in the function definition.

# The function foo is defined beginning on line 3 with two positional 
# parameters: bar and qux.
# foo is invoked on line 7 with only a single positional argument 
# but the function definition is expecting two arguments.

######################
# potential fix

def foo(bar, qux = 'Goodbye'):   # can provide a default for the second parameter
    print(bar)
    print(qux)

foo('Hello')