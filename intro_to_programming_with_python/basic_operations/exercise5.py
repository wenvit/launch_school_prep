#5. Will an error occur if you try to access a list element with 
#an index greater than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
#print(foo[3])      # will this result in an error?

# Answer: YES, this code will result in an error 

# Here's one approach with indices that do not result in errors

for idx in range(len(foo)):
    print(foo[idx])
