# 2. Can you write some code to change the value 'bye' in 
# the following tuple to 'goodbye'?

# tuples are immutable so this solution is to convert to a list
# using list() constructor, change the 'bye' element in the list
# then convert back to tuple

stuff = ('hello', 'world', 'bye', 'now')
# print(stuff)
 
# stuff_list = list(stuff)
# print(stuff_list)

# stuff_list[2] = 'goodbye'
# print(stuff_list)

# stuff = tuple(stuff_list)
# print(stuff)


#########################
# Another solution from Launch School
# can use addition operator with tuples to concatenate tuples


# must use the (element,) format to designate tuple with single element
#stuff = stuff[0:2] + ('goodbye',) + stuff[3:]
# a little simpler
stuff = stuff[0:2] + ('goodbye', stuff[3])

print(stuff)