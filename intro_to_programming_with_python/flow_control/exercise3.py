# 3. Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

#bar_code_scanner('113')  

# This prints Product2
# The string value '113' is passed as an argument to the 
# parameter `serial` in the function `bar_code_scanner`
# The body of the function contains a match statement that
# searches for product numbers.
# In the first execution, a string value of `113` is passed
# to the function. The second case statement matches the value `113`
# and Product2 is printed.


bar_code_scanner(142)

# This prints Product not found!

# The second execution passes the integer `142` to the function
# None of the case statements match the value 142
# including the string value '142' so the match expression
# evaluates to the default value (case _) of Product not found!