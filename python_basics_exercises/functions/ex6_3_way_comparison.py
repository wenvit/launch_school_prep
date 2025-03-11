##### Problem statement

# Write a function that compares the length of two strings. 
# It should return -1 if the first string is shorter, 
# 1 if the second string is shorter, 
# and 0 if they're of equal length. 
# For example:

# compare_by_length('patience', 'perseverance') # -1
# compare_by_length('strength', 'dignity')      #  1
# compare_by_length('humor', 'grace')           #  0

##### Solution

def compare_by_length(string1, string2):
    
    length1 = len(string1)
    length2 = len(string2)

    if length1 < length2:
        return(-1)
    elif length1 > length2:
        return(1)
    else:
        return(0)
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0