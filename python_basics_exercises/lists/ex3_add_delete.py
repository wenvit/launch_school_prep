##### Problem statement

# We are given the following list of energy sources.

#energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# Write some code to remove 'fossil' from the list, 
# then add 'geothermal' to the end of the list.

##### Solution

# initialize energy variable by assigning it to list

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# `remove` method removes first instance of element from mutable sequence
# `remove` mutates the list

energy.remove('fossil') 
print(energy)          

# `append` appends a single object to the end of a mutable sequence
# `append` mutates thte list

energy.append('geothermal') 
print(energy)

# Other discussion from Launch School solution: with `remove` and `append`
# make sure desired outcome is to mutate the list