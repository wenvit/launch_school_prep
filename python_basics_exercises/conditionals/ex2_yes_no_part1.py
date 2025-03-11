##### Problem statement

# The code provided below randomly initializes random_number
# to either 0 or 1 each time it is executed.
# Write an if statement that prints Yes! if random_number is 1, 
# and No. if random_number is 0.

##### Solution

import random

random_number = random.randint(0, 1)

print(random_number)

if random_number:
    print('Yes!')
else:
    print('No')

# Further exploration:
# See documentation for random module, use
# use python's module index and search for random


