# 2. Use the REPL and the arithmetic operators to extract the 
# individual digits of 4936:

#One place is 6.
#Tens place is 3.
#Hundreds place is 9.
#Thousands place is 4.

# assign variable to original number
number = 4936
print(f'original number is {number}')

# use % to strip off ones digit
ones = number % 10
print(f'ones digit is {ones}')

# to strip off tens digit, first apply integer division by 10
number2 = number // 10
print(f'new starting point is {number} // 10: {number2}')

tens = number2 % 10
print(f'tens digit is {tens}')

# next strip off hundreds digit 
number3 = number2 // 10
print(f'new starting point is {number2} // 10: {number3}')

hundreds = number3 % 10
print(f'hundreds digit is {hundreds}')

# finally strip off thousands digit in one step
thousands = number3 // 10

print(f'thousands digit is {thousands}')

# put it all together as final check

print(f'reconstructed original number is {thousands}{hundreds}{tens}{ones}')

