##### Problem statement

# Take a moment to read the Python documentation on the continue statement.

# Write a for loop that iterates over the elements of the list 
# cities and prints the length of each string. 
# If the element is None, use the continue statement to skip 
# forward to the next iteration without printing anything.

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

##### Solution

# In the Python language reference, simple statements section, there's
# a very brief desription of the `continue` statement:
# It continues with the next cycle of the nearest enclosing loop.

for city in cities:
    if city == None:   ## Launch School solution uses `is` here
        continue
    print(f'{city} is {len(city)} characters long')
    
