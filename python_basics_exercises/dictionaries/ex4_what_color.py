##### Problem statement

# Using the following code, select and print the value 'blue' 
# from the car object:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}


##### Solution

print(car['color']) # if you know key exists
print(car.get('color'))  # if you don't know key exists