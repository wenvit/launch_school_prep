##### Problem statement

# We have a grocery list. As we check off items on that list, 
# from the top of the list to the bottom, we want to remove them from the list.

# Write code that removes the items from grocery_list, 
# one by one, until it is empty. 
# If you print the elements you remove, the expected behavior would look as follows.

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# # Your code.

# print(grocery_list)

# Expected output
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []

##### Solution

# `for` loop doesn't work because the pop method
# mutates the list by removing an element one by one, so it
# destructively changes the list each iteration.
# This solution relies on a `while` loop that iterates
# as long as grocery_list is truthy, i.e., as long as as
# the list contains elements

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                 'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list.pop(0))

print(grocery_list)
    




