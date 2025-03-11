##### Problem statement

# Using the official Python documentation, can you determine 
# how to check whether a string contains a specific substring?

##### Solution

# use the `in` operator. See python language reference, expressions, 
# membership test operations
# `in` returns boolean True if string contains substring
# False otherwise

text = 'Is it going to ice or snow tonight?'

print('ice' in text)
print('rain' in text)