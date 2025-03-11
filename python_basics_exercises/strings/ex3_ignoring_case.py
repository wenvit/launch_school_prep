##### Problem statement

# Using the following code, compare the value of name with the string 
# 'RoGeR' while ignoring the case of both strings.
# Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between the value of 
# name and the string 'DAVE'.

name = 'Roger'

##### Solution

name_no_case = name.casefold()
print(name_no_case)

print(name_no_case == 'RoGeR'.casefold())
print(name_no_case == 'DAVE'.casefold())