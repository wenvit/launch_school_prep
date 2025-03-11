##### Problem statement

# Referring to the official Python documentation, how would you 
# identify the data type of the following values?

# 23.5
# 'Call me Ishmael.'
# False
# 0
# None

##### Solution

# From python documentation, python standard library, built-in functions:
# type function with one argument returns the type of an object. The return
# value is a type object and generally the same object as returned by 
# object.__class__

print(type(2.3))                 # Float
print(type('Call me Ishmael.'))  # String
print(type(False))               # Boolean
print(type(0))                   # Integer
print(type(None))                # NoneType