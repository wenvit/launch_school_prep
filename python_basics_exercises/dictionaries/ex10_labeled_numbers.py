##### Problem statement

# Use a for loop to iterate over the numbers dictionary 
# and print each element's key/value pair.

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# Expected output
# A high number is 100.
# A medium number is 50.
# A low number is 10.

##### Solution

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():    # example of tuple unpacking
    print(f'A {key} number is {value}.')
