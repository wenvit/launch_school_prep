##### Problem statement

# Without looking at your notes or the official 
# documentation, try to recall all values that 
# count as falsy in Python.

##### Solution

# Looked at documentation for some of these:
# python standard library, truth value testing

# Constants:
# False
# None

# Any representation of zero:
# 0    integer
# 0.0  float
# 0j   complex

# Empty collections & sequences:
# []   list
# {}   dictionary
# ()   tuple
# range(0)  have to use range constructor because there's no literal range
# set() have to use set constructor because {} is empty dictionary
# ''   string


##### Tip from Launch School solution: use bool() to check
# truthy or falsy based on return of True or False

print(bool(range(0)))
print(bool({}))
print(bool(0j))
print(bool([0]))  # True because it's not an empty list