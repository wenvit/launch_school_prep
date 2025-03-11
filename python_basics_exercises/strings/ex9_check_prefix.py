##### Problem statement

# Write a function that checks whether a string starts with a specific prefix.

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

##### Solution

# One approach relying on str.startswith method

# def starts_with(string, pattern):

#     return string.startswith(pattern)

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# Another approach 

# This approach determines the length of the pattern to check. 
# The length of the pattern is used as the stop index for slicing the string.
# The string is sliced from the first character (index 0) up to the 
# stop index (not inclusive)
# The prefix slice is compared to the pattern, returns True if prefix slice 
# has the same value as pattern, False otherwise

def starts_with(string, pattern):

    stop = len(pattern)  
    prefix = string[:stop] 

    return prefix == pattern

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True
# print(starts_with('     123434', ''))
