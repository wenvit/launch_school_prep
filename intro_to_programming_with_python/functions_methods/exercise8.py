# 8. Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

#######################

# This code snippet will result in an error
# Cannot pass more arguments than parameters

# The function foo is defined beginning on line 3 with 
# two positional parameters: bar and qux.
# The function is invoked on line 7 with 3 arguments (42, 3.141592, 2.718)
# when it only expects 2.

