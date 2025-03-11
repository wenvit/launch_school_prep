##### Problem statement

# Determine what the following code snippet prints. 
# First solve it in your head or on paper, then run it in 
# your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# Bonus question:
# Do we need the parentheses in the boolean expression 
# or could we have written the following?:

# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
# print(is_moving)

##### Solution

# This will print True

# looking at python language reference, operator precedence table,
# order of evaluation of the complex expression:
#     1. expressions in parentheses 
#     2. >, < comparison operators
#     3. and 
#     4. or

# based on this, the expression is evaluated in this order:
# (speed > 0 or acceleration > 0) returns True 
# This is because only one operand must be truthy with the `or` operator
#     speed > 0 => False
#     acceleration > 0 => True
# braking_force < acceleration => True
# Lastly, the `and` condition is evaluated, where both operands must be truthy
# So we have: True and True
# This evaluates to True because both sides are the boolean True 

# bonus: how does this evaluate without the parentheses?
# This will print out True
# Here's how 
# braking_force < acceleration and speed > 0 or acceleration > 0:
# The `<` and `>` expressions are evaluated first
#     braking_force < acceleration => True
#     speed > 0 => False 
#     acceleration > 0 => True
# Now we have:
#     True and False or True
# Next, the `and` expression is evaluated, both sides must be truthy
#     True and False => False
# Finally, `or` is evaluated, one side must be truthy
#     False or True => True


# But not so simple, and it's important to look at other test cases 

# speed = 0
# acceleration = 10
# braking_force = 19

# is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
# print(is_moving)

# setting acceleration < braking_force
#  w/parens: False and (False or True) => False and True => False
# wo/parens: False and False or True => False or True => True

## Parentheses do make a difference in the outcome!!

