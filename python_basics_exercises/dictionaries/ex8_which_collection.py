##### Problem statement

# Rewrite car as a list of lists in which each nested list 
# contains two elements that represent the corresponding 
# key/value pairs.

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

##### Solution


car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}


car_list = [ [key, value] for key, value in car.items() ]

print(car_list)