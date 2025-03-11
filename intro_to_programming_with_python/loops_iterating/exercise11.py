# 11. Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0 # initialize index for outer loop

while outer_index < len(my_list):

    nested_list = my_list[outer_index]
    inner_index = 0 # initialize index for inner loop, have to reset for each nested list
    
    while inner_index < len(nested_list):
        if nested_list[inner_index] % 2 == 0:
            print(nested_list[inner_index])
        inner_index += 1

    outer_index += 1
