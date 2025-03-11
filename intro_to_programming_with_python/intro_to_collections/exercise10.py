# 10. Bob expects the following code to print the names in 
# alphabetical order. Without running the code, can you say 
# whether it will? Explain your answer.

names = { 
    'Chris', 
    'Clare', 
    'Karis', 
    'Karl',
    'Max', 
    'Nick', 
    'Victor',
}

# This will not always print the names in alphabetical order
# becuase it's a set. A set is not an ordered sequence so can't 
# be counted on to consistently print the same order every time.

print(names)