# 7. Write a find_integers function that returns a list 
# of all the integers from my_tuple:

def find_integers(input_tuple):
    return [ element 
            for element in input_tuple 
            if type(element) is int ]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

# Hint:
# print(type(True) is int)      # False (boolean)
# print(type([1, 2, 3]) is int) # False (list)
# print(type(3.141592) is int)  # False (float)
# print(type(77) is int)        # True




