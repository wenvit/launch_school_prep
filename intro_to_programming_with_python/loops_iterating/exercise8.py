# 8. Write a comprehension that creates a dict object whose keys
# are strings and whose values are the length of the corresponding key.
# Only keys with odd lengths should be in the dict. 

# Dictionary comprehension syntax
# { key: value for element in iterable if condition }


my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result_dict = { name: len(name) 
           for name in my_set 
           if len(name) % 2 != 0 }
print(result_dict)