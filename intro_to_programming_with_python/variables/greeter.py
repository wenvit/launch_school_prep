# 5. Write a program named greeter.py that greets 'Victor' three times.
# Your program should use a variable and not hard code the string value
# 'Victor' in each greeting. 

name = 'Victor'
greeting = ['Good morning,', 'Good afternoon,', 'Good evening,']

for greet in greeting:
    print(f'{greet} {name}.')