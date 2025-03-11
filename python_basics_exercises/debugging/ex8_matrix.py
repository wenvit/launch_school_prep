##### Problem statement

# We wanted to create a matrix 3x3 so we could use it 
# to build a Tic-Tac-Toe game. However, we encountered an issue, 
# as whenever we change a value in one nested list, 
# all nested lists are affected. Can you fix the code?

# sub_list = ["-", "-", "-"]
# matrix = []

# for _ in range(3):
#     matrix.append(sub_list)

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

##### Solution

# On line 8, the sub_list variable is assigned to a list of ["-", "-", "-"].
# Within the `for` loop, the value of sub_list is appended to the outer list (matrix)
# three times. Each nested list points to the same sub_list object
# in memory. For this reason, when the nested list at index 0 is mutated on line 14,
# all nested lists are mutated because they're the same object.

# check ids of each nested list --
# unique representation of an object
# if id function returns same number, it's the same object
# print(id(matrix[0]))
# print(id(matrix[1]))
# print(id(matrix[2]))

# How to fix it:
# copy method creates shallow copy of the list
# since each one is a separate object, mutating one nested list
# won't change the others

sub_list = ["-", "-", "-"]
matrix = []

for i in range(3):
    matrix.append(sub_list.copy())

print(matrix) # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

matrix[0][0] = 'X'
print(matrix)

matrix[2][1] = 'O'
print(matrix)

# check ids again

print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))

# Another way from Launch School solution - very common
# very pythonic way of creating shallow copies using slicing
# list.copy() is same as list[:]

# sub_list = ["-", "-", "-"]
# matrix = []

# for i in range(3):
#     matrix.append(sub_list[:])

# print(matrix) # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# matrix[0][0] = 'X'
# print(matrix)

# matrix[2][1] = 'O'
# print(matrix)


# print(id(matrix[0]))
# print(id(matrix[1]))
# print(id(matrix[2]))