# 1. Write a program named greeter.py. 
# The program should ask for your name, then output Hello, NAME! 
# where NAME is the name you entered:

name = input("What's your name? ")

print(f'Hello, {name}!') # f-string interpolation
print('Hello, ' + name + '!') # string concatenation

# another way is to use separate arguments with no separator
print('Hello, ', name, '!', sep = '')