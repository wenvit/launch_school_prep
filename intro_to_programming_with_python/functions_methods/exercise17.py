# 17. Which of the identifiers in the following program are function names? 
# Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

## Function names

# say - defined line 4, invoked on line 10

## Method names: methods are invoked on an object

# upper - invoked line 10
# lower - invoked line 10

## Built-in functions 

# print - invoked line 5
# input - invoked on lines 7 & 8
# max - invoked on line 10
