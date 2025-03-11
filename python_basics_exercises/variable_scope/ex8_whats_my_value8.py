##### Problem statement

print(greeting)

greeting = 'Hello world!'

##### Solution

# This code will raise an error.
# Line 3 invokes print function passing global greeting variable as an 
# argument. On line 5, the greeting variable is initialized to the string
# `Hello world!` Even though the greeting variable is initialized in
# the global scope that the print function should be able to access, 
# the print function is invoked before greeting is initialized 
# so it results in an error.