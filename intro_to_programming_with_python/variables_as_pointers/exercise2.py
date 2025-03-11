# 2. Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)   

# This code will print {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# Order of elements may differ because sets are not ordered.
# The set1 variable is initialized in line 3 to a set with 3 elements, an integer, string and tuple
# At line 4, set2 is initialized by assigning it to the value referenced by set1 
# set2 and set1 are pointing to the same object in memory (aliases of same object)
# When range(5, 10) is added to set1 in line5 (add mutates set1), 
# printing set2 results in same set as set1 because they are the same object

