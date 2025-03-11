##### Problem statement

# What happens if we take the list ['fish', 'and', 'chips'] and try to access 
# the element at index position 10? 
# First try to determine what will happen by consulting the documentation, 
# then verify your understanding in the Python REPL.

##### Solution

# Per the python documentation:
# exception IndexError
# Raised when a sequence subscript is out of range.

my_list = ['fish', 'and', 'chips']
print(my_list[10])