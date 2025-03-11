##### Problem statement

# Write a function that accepts a single argument, a number, 
# and returns the result of multiplying its argument by an exponent 
# of 2 (also known as squaring the number or 
# raising the number to the power of 2).

##### Solution

def square(number):
    return number**2

numbers = [0, 1, 2, 5, 10]

for num in numbers:
    print(square(num))