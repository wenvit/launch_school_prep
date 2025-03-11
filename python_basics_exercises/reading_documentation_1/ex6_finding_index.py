##### Problem statement

# Python lists come with a variety of built-in methods that allow for 
# common list manipulations. One such operation is determining the 
# index of an item in the list.

# Given a list:

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# How would you determine the index of the fruit "cherry" in this list?
# Refer to the official Python documentation on lists to assist with your answer.

##### Solution

# seq.index(x) returns index of first occurence of x in sequence. 
# ValueError if x not found

print(fruits.index('cherry'))  # expect 2
# print(fruits.index('kiwi'))    # ValueError

# Tip from Launch School solution discussion:  Good practice to first check whether value 
# exists in the list using the `in` keyword before attempting to find its 
# index to prevent potential runtime errors and makes code more resilient to 
# unexpected input

