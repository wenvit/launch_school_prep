# 3. Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)   # dict() makes shallow copy -- immutable objects are same object
dict2['Monty Python'] = 'Holy Grail' 
print(dict1['Monty Python'])

# This code will print 'The Life of Brian' which is the original value associated 
# with dict1['Monty Python']
# dict1 is a dictionary consisting of immutable strings as keys, which all have immutable values
# On line 9, the `dict` constructor function is used to create a new object called dict2
# The `dict` constructor function make a shallow copy, meaning any nested collections will be the same object
# However, in this case, dict1 doesn't contain any nested collections, 
# so the keys & values in dict2 are copies, meaning changes to dict2 will not be reflected in dict1
# On line 10, the value associated with the 'Monty Python' key is reassigned to 'Holy Grail'
# Because the immutable values are copies, not the same object, the reassignment of 
# the dict2['Monty Python'] value to 'Holy Grail' does not modify dict1

