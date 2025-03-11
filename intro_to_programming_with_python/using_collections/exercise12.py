# 12. Write some code that determines and prints whether the number 3 appears 
# inside each of these lists:


####################
# First take

# def look_for_3(input_list):
#     if 3 in input_list:
#         print(True)
#     else:
#         print(False)

# Refactor 
# def look_for_3(input_list):
#     print(True if 3 in input_list else False)

# Launch School solution -- even more concise
def look_for_3(input_list):
    print(3 in input_list)

numbers1 = [1, 3, 5, 7, 9, 11]    # True
numbers2 = []                     # False
numbers3 = [2, 4, 6, 8]           # False
numbers4 = ['1', '3', '5']        # False
numbers5 = ['1', 3.0, '5']        # True

look_for_3(numbers1)
look_for_3(numbers2)
look_for_3(numbers3)
look_for_3(numbers4)
look_for_3(numbers5)