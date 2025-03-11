# 1. To what values do the following expressions evaluate?

False or (True and False)
# False
# This is an `or` expression so one side or other must be truthy.
# Since the left side of expression is boolean False, python 
# continues to evaluate right side. Subexpression `True and False`
# evaluates to boolean False because both sides must be truthy 
# with `and` operator.

True or (1 + 2)
# True
# This is an `or` expression so one side or other must be truthy.
# Because left side is boolean True, python short circuits
# after left side of expression and returns boolean True. 

(1 + 2) or True
# 3
# This is an `or` expression so one side or the other must be truthy.
# The left side `1 + 2` evaluates to a truthy value of 3
# so python short circuits here with integer of 3.

True and (1 + 2)
# 3
# This is an `and` expression so both sides must be truthy.
# The left side is the boolean True so python continues to 
# right side, which evaluates to 3.

False and (1 + 2)
# False
# This is an `and` expression so both sides must be truthy.
# First subexpression is boolean False, so python short circuits
# and returns boolean False

(1 + 2) and True
# True
# This is an `and` expression so both sides must be truthy.
# First subexpression evaluates as a truthy value of 3
# so python continues to evaluate the second subexpression 
# which is the boolean True.

(32 * 4) >= 129
# False
# Expression that says: 128 is greater than or equal to 129
# This evalues to boolean False because 128 is not greater 
# than or equal to 129

False != (not True)
# False
# This expression says: False is not equal to False (not True)
# This evaluates to boolean False.

True == 4
# False
# This expression says: the boolean True is equal to 4 
# This evaluates to the boolean value False

False == (847 == '847')
# True
# The subexpression 847 == '847' is False because it's comparing
# the integer 847 to a string '847'
# False is equal to False
