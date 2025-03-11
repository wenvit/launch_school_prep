##### Problem statement

# Without running the following code, determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

##### Solution

# This code will print $3.99
# Line 5 initializes the sale variable by assigning it to boolean True
# Line 6 initializes the admission_price variable by assigning it to the
# value returned by the ternary expression `5.25 if not sale else 3.99`
# The ternary expression returns the value 5.25 if sale is not truthy (falsy),
# otherwise 3.99 (if sale is truthy). In this example, sale is truthy, so this
# expression returns 3.99
# Line 8 print function takes in an f-string argument
# consisting of $ and admission_price (3.99)