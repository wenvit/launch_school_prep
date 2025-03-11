##### Problem statement

# Find the Python Documentation on operator precedence, and 
# use it to determine the result of evaluating 4 * 5 + 3**2 / 10.

##### Solution

# Evaluation order is discussed in the expressions section of the 
# python language reference

# Order of evaluation of expression:
# 3**2 = 9 
# * and / have same order of preference, but evaluated left to right
# 4 * 5 = 20
# 9 / 10 = 0.9 
# 20 + 0.9 
# Result is expected to be 20.9

# Check
print(4 * 5 + 3**2 / 10)

# Tip from Launch School solution: use parentheses to make code clear
print((4 * 5) + ((3**2) / 10))

