##### Problem statement

# Write a function that counts the number of occurrences of a 
# substring in a string.

# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0

##### Solution

# One approach using str.count method

def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0


