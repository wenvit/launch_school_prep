# 1. The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# This code causes an infinite loop because the counter variable is never
# incremented, therefore the expression remains truthy and while loop
# never stops
# The while block iterates as long as the counter is less than 5.
# The counter variable is initialized as 0 and because it is never incremented,
# it remains less than 5