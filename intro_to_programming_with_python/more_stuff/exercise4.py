# Write a function called increment_counter that increments a counter variable 
# every time it is called. You can test your code with the following:

counter = 0  # must initialize counter first

# If we want to reference or access a global variable within a function, python 
# will allow us to do so and knows to search for outer/global scope.
# However, if we want to change or modify a global variable within a function, need
# to explicitly tell python to look for global variable value with global keyword.
# This is designed to ensure we are intentional about changing global variables.

def increment_counter():
    global counter # this tells python to reference global counter
    counter += 1   # reassigns global counter to counter + 1

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
