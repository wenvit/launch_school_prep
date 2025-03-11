##### Problem statement

# Predict the output of the code shown below. When you run the code, 
# do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

##### Solution

# This will print True
# On lines 6 & 7, list1 and list2 are initialized to 
# two list literals containing the same elements.
# The equality operator `==` on line 9 looks at whether
# list1 and list2 have the same value, i.e., contain the same elements.
# This expression returns boolean True, which is passed
# as an argument to the print function.

# More discussion from Launch School solution:
# Because list1 and list2 are not the same object in memory, 
# the `is` operator returns False here.

print(list1 is list2)

# `==` evaluates value equality
# `is` evaluates object equality