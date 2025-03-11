##### Problem statement

# You've been asked to implement a function called digit_product 
# that takes a string of digits as an argument and returns the 
#  nproduct of all the digits in the string.

# When testing the function, you find that it returns 0, 
# which is not what you expect. Can you identify the 
# issue and correct the code?

# def digit_product(str_num):
#     digits = [int(n) for n in str_num]
#     product = 0

#     for digit in digits:
#         product *= digit

#     return product

# result = digit_product('12345')
# print(result)  # expected: 120, actual: 0

##### Solution

# This function as originally written always returns 0. This is because
# the product variable is initialized to 0 (line 13). So in the `for`
# loop (lines 14 & 16), when the product variable is reassigned 
# in each iteration to the product of the previous value of product and digit, 
# each digit is multiplied by 0 every time so the result is always 0.

# Here's a fix: initialize product variable to 1 instead of 0

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0