# 5. On reflection, we've decided that we don't want to rely on using a global variable 
# in the code we wrote in the previous example. 
# To fix this, we're going to nest the code from the previous example into an outer function.
# There's a bug in this code. Identify the bug, and fix it.

def all_actions():
    counter = 0  # counter initialized in outer scope of function (not global)

    def increment_counter(): # nested function that increments counter
  #      global counter       # this is the bug because counter isn't a global variable
        nonlocal counter      # tells python to look in outer scope of function (not global scope)
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()  # invokes all_actions() function