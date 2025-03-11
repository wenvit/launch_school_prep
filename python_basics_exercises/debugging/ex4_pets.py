##### Problem statement

# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser,
# to the pets dictionary. After doing so, she realizes that her dogs Sparky 
# and Fido have been mistakenly removed. Help Magdalena fix her code so 
# that all three of her dogs' names will be associated with the key 
# 'dog' in the pets dictionary.

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'] = 'bowser' 

# print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

##### Solution

# The value associated with the key dog is a list. Can use the append method
# to add bowser to list without removing other values.
# This approach mutates list rather than reassigning value associated with dog key.

pets['dog'].append('bowser')

print(pets) 