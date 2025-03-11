##### Problem statement

# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, 
# then use the resulting error message to determine exactly what is wrong.
# (You don't have to fix this code.)

##### Solution

# # The python standard library reference, built-in exceptions documentation
# states: Raised when an operation or function is applied to an object of 
# inappropriate type. 

# When the above code is run, the `tweet + 5` expression is highlighted
# The TypeError message states: can only concatenate str (not "int") to str
# The issue is that `tweet` is a string and python is interpreting the `+`
# operator as a string concatenation operation. So the TypeError is raised
# when it attempts to concatenate the string `tweet` and the integer `5`

