##### Problem statement

# Use Python's string methods on the string 'Captain Ruby' 
# to create a string with the value 'Captain Python'.

##### Solution

# One way: seems easiest to follow

ruby_string = 'Captain Ruby'

py_string = ruby_string.replace('Ruby', 'Python')

print(py_string) 

# Another way
py_string = ruby_string.split()[0] + ' Python'

print(py_string)
