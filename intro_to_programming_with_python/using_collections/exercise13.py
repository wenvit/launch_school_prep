# 13. Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')

print('Butterscotch' in cats)    # True, Butterscotch is one of the elements of the tuple cats
print('Butter' in cats)          # False, Butter is not one of the elements of the tuple cats
print('Butter' in cats[3])       # True, no longer checking item equality within tuple
                                 # it's asking if Butter is a substring of Butterscotch at cats[3]
print('cheddar' in cats)         # False, cheddar is not in tuple because must be an exact match

