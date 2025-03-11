##### Problem statement

# You are trying to access a value in a dictionary, but the code i
# s giving you an error. Can you change line 9 so that it prints
#  "Unknown" instead of raising an error?

# info = {'name': 'Srdjan', 'age': 38}

# print(info['city'])

##### Solution

# The code as originally written raises a KeyError when the print
# function is invoked on line 9 because the info dictionary key
# passed as an argument doesn't exist. Here's a fix:

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))

# Another way

#print(info['city'] if 'city' in info else 'Unknown')
