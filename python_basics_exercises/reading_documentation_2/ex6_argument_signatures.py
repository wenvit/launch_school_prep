##### Problem statement

# How many arguments does the str.join method expect? 
# What happens if you call it with fewer or more arguments?

##### Solution

# str.join takes one argument

# Trying to pass in fewer or more resuls in a TypeError:
# str.join() takes exactly one argument

print(' '.join(['a', 'b', 'c']))
print('****'.join('abc'))
#print('---'.join()) # TypeError
#print(' '.join('a', 'b')) # TypeError
