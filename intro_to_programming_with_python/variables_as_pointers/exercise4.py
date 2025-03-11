# 4. Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

print(dict1['a'] is dict2['a'])
print(dict1['b'] == dict2['b'])

# This code will print [1, 42, 3].
# On line 8, new variable dict2 is initialized by assigning to a copy of dict1, 
# which results from passing dict1 as an argument to the `dict` constructor function.
# The `dict` constructor function creates a shallow copy of an object, so while it creates
# a new dict object, any nested objects are actually pointers or aliases to the same object.
# In this example, the list at key 'a' are the same objects in dict1 and dict2.
# Also, the tuple at key 'b' are the same objects in dict1 and dict2.
# On line 9, when the list value associated with the key 'a' is mutated by reassigning
# the integer at index 1 to 42, the same nested list associated with key 'a' within dict2 
# is mutated as well. 

