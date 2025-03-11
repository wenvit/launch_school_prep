##### Problem statement

# How can you check if a variable holds a value that is a list? 
# Given two variables, verify whether the values they hold are lists.

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

##### Solution

# The `type` function returns the type of an object

print(type(some_value1).__name__ == 'list')
print(type(some_value2).__name__ == 'list')

# Launch School solution with isinstance function -- more straightforward

print(isinstance(some_value1, list))
print(isinstance(some_value2, list))