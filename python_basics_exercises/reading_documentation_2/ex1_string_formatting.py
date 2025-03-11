##### Problem statement

# Python offers multiple ways to format strings.
# The str.format method is a popular method, but since Python 3.6, 
# a new way called f-strings (formatted string literals) was introduced. 
# F-strings offer a concise way to embed expressions inside string literals.

# Given the following variables:

name = "Victor"
profession = "programmer"

# 1. How can you print the string Hello, Victor. You are a programmer. 
# using the str.format method? You should fill in the name and profession 
# in a string literal that contains 
# the rest of the text.
# 2. How can you achieve the same result using an f-string?

##### Solution

# 1. Using str.format method

print('Hello, {}. You are a {}.'.format(name, profession)) # this relies on position
print('Hello, {0}. You are a {1}.'.format(name, profession)) # explicitly references format method arguments by index

# Launch School solution relies on creating variable with message to pass as argument to print function 

message_format = 'Hello, {}. You are a {}.'
print(message_format.format(name, profession))

# 2. Using f-strings
# Note: f-strings discussed in python language reference, lexical analysis section

print(f'Hello, {name}. You are a {profession}.')

# Launch School solution 

message_format = f'Hello, {name}. You are a {profession}.'
print(message_format)


