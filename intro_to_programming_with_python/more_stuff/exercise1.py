# 1. What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# This code will print CHRIS
# The function do_something is defined on lines 3 & 4. 
# It takes in a parameter called `dictionary`. 
# For the return value, it first calls dictionary.keys() to create a dictionary view 
# of keys of the dictionary passed in.
# It passes the dictionary view objected as an argument to the sorted function.
# The sorted function returns an alphabetically sorted list.
# The sorted list is indexed in to select the value at index 1. 
# Lastly, the upper() method is invoked on this value at index 1.
# On line 15, do_something is invoked by passing in my_dict. The dictionary keys
# are sorted alphabetically, and the key 'Chris' would be index 1 in the resulting list.
# The return value of 'Chris'.upper() results in CHRIS when passed to the print function.