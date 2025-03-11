# 5. Which of the following values can't be used as a 
# key in a dict object, and why?

# 'cat'                        # valid key
# (3, 1, 4, 1, 5, 9, 2)        # valid key
# ['a', 'b']                   # not valid, lists are mutable
# {'a': 1, 'b': 2}             # not valid, dicts are mutable
# range(5)                     # valid key
# {1, 4, 9, 16, 25}            # not valid, sets are mutable
# 3                            # valid key
# 0.0                          # valid key
# frozenset({1, 4, 9, 16, 25}) # valid key


### Note on hashable: if a tuple contains a list as an element, it 
# is no longer hashable because the list is mutable