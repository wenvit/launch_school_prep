##### Problem statement

# Without running the following code, determine what it will print:

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):  # 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
#         print(f'{dividend} / {divisor} = 3') # 3 / 1 = 3, 6 / 2 = 3, ...
#         divisor += 1

# multiples_of_three

##### Solution

# This code as written won't print anything. 
# Line 12 doesn't invoke the function, it needs parens: 
# multiples_of_three()

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):  # 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three() # This fix properly invokes the function