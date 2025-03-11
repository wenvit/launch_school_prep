##### Problem statement

# Create a nested dictionary that contains the following data.

# Car

# type	color	year
# sedan	blue	2003

# Truck

# type	color	year
# pickup red	1998

##### Solution


vehicles = {

    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },

    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },
    
}

print(vehicles)
print(vehicles['car'])
print(vehicles['truck']['type'])