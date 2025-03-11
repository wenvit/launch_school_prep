
# Slicing

# seq = 'abcdefghi'
# print(len(seq))

# print(seq[3:7])    # defg
# print(seq[-6:-2])  # defg
# print(seq[2:8:2])  # ceg
# print(repr(seq[3:3])) # ''
# print(seq[:])      # abcdefghi
# print(seq[::-1])   # ihgfedcba

# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(seq))

# print(seq[3:7])    # [4, 5, 6, 7]
# print(seq[-6:-2])  # [5, 6, 7, 8]
# print(seq[2:8:2])  # [3, 5, 7]
# print(seq[3:3])    # []
# print(seq[:])      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(seq[::-1])   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# seq[::-1] is similar to seq.reverse() but
# former returns new sequence and seq.reverse() 
# mutates the original

#seq = [[1, 2], [3, 4]]
#seq_dup = seq[:] # creates a shallow copy
# seq_dup = seq[0:len(seq)] # equivalent to seq[:]

# print(seq_dup)

# print(seq[0] is seq_dup[0])

# my_dict = {
#     'a': 'abc',
#     37: 'def',
#     (5, 6, 7): 'ghi',
#     frozenset([1, 2]): 'jkl',
# }

# print(my_dict['a'])   # abc
# print(my_dict[37])    # def
# print(my_dict[(5, 6, 7)]) # ghi
# print(my_dict[frozenset([1, 2])]) # jkl
# #print(my_dict['nothing'])  # error

# print(my_dict.get('nothing'))

#####################
# Collection Membership

# seq = [
#     4, 
#     'abcdef',
#     (True, False, None),
# ]

# print(4 in seq)              # True
# print(4 not in seq)          # False
# print('abcdef' in seq)       # True
# print('abcdef' not in seq)   # False
# print('cde' in seq[1])       # True
# print('cde' not in seq[1])   # False
# print('acde' in seq[1])      # False
# print('acde' not in seq[1])  # True
# print((True, False, None) in seq) # True
# print((True, False, None) not in seq) # False
# print(3.14 in seq)            # False
# print(3.15 not in seq)        # True


############################
# Merging collections with zip function

# iterable1 = [1, 2, 3]
# iterable2 = ('Kim', 'Leslie', 'Bertie')
# iterable3 = [None, True, False]

# zipped_iterables = zip(iterable1, iterable2, iterable3)
# print(list(zipped_iterables))   # prints list of tuples

# print(list(zipped_iterables)) # fails when reuses the iterator

############################
# Operations on dictionaries

# people_phones = {
#     'Chris': '111-2222',
#     'Pete':  '333-4444',
#     'Clare': '555-6666',
# }

# print(people_phones.keys(
# ))

# print(people_phones.values())

# print(people_phones.items())

# keys = people_phones.keys()
# values = people_phones.values()

# print(keys)
# print(values)

# people_phones['Max'] = '123-4567'
# people_phones['Pete'] = '345-6789'
# del people_phones['Chris']

# print(keys)

###########################

# Operations on mutable sequences
# numbers = [10, 2]
# numbers.append(10)
# print(numbers)

# numbers = [1, 2]
# numbers.insert(0, 8)      # [8, 1, 2]
# print(numbers)

# numbers.insert(2, 6)      # [8, 1, 6, 2]
# print(numbers)

# numbers.insert(100, 55)   # [8, 1, 6, 2, 55]
# print(numbers)

# numbers.insert(-3, 33)    # [8, 1, 33, 6, 2, 55]
# print(numbers)

####################
# Removing elements from mutable sequences

# my_list = [2, 4, 6, 8, 10]
# my_list.remove(8)
# print(my_list)
# my_list.remove(8)

# my_list = [2, 4, 6, 8, 10]
# print(my_list.pop(1))
# print(my_list)
# print(my_list.pop())
# print(my_list)
# print(my_list.pop(4))

##########################
# Sorting collections

# names = ('Grace', 'Clare', 'Allison', 'Trevor')
# print(sorted(names))
# print(names)

# names = list(names)
# print(names)

# names.sort()
# print(names.sort())
# print(names)

# names.sort(reverse=True)
# print(names)

# words = ['abc', 'DEF', 'xyz', '123']
# print(sorted(words))
# print(sorted(words, key=str.casefold))

# numbers = ['1', '5', '100', '15', '534', '53']
# numbers.sort()
# print(numbers)
# numbers.sort(key=int)
# print(numbers)

################
# Reversing lists and dictionaries

# names = ('Grace', 'Clare', 'Allison', 'Trevor')
# reversed_names = reversed(names)
# print(reversed_names)
# print(tuple(reversed_names))

# names = list(names)
# print(names.reverse())
# print(names)

# my_dict = {
#     'abc': 1,
#     'xyz': 23,
#     'pqr': 0, 
#     'jkl': 5,
# }

# reversed_dict = reversed(my_dict)
# print(reversed_dict)

# print(list(reversed_dict))

# print('1234'.isalpha())
# print('ABCDedf1234'.isupper())
# print('708471384703'.isupper())

########################
# text = ' \t  abc def    \n\r'

# print(repr(text))   # repr used to clearly show whitespace characters

# print(repr(text.strip()))

# print(repr(text.strip('abc')))

# text = 'aaabaacccabxyzabccba'

# print(repr(text.strip('a')))
# print(repr(text.strip('ba')))

###################

# words = ['you', 'were', 'lucky']

# print(''.join(words))    # youwerelucky
# print(' '.join(words))   # you were lucky
# print(' '.join(words).capitalize()) # You were lucky

####################
# school = 'launch school'

# print(school.find(' '))     # 6
# print(school.find('l'))     # 0
# print(school.find('h'))     # 5
# print(school.find('hoo'))     # 9
# print(school.find('x'))     # -1
# print(school.find('N'))     # -1

# print(school.rfind(' '))     # 6
# print(school.rfind('l'))     # 12
# print(school.rfind('h'))     # 9
# print(school.rfind('hoo'))     # 9
# print(school.rfind('x'))     # -1
# print(school.rfind('N'))     # -1

#text = 'abc abc def abc'

# print(text.find(' ', 4))       # 7
# print(text.find(' ', 8))       # 11

# print(text.find('c', 0, 2))     # -1
# print(text.find('c', 3, 10))    # 6

# print(text[3:10].find('c'))       # 3
# print(text.find('c', 3, 10))      # 6

###########################

# nested_seq = [
#     [1, 2, [3, 4, (5, 6, 7, 8)]],
#     [9, [10, (11,)]],
#     [12, 13, [14, 15, (16, 17)]],
#     [18, [19, 20, (21, 22)]],
# ]

# print(nested_seq[1])           # [9, [10, (11,)]]
# print(nested_seq[3][0])        # 18
# print(nested_seq[0][2][2])     # (5, 6, 7, 8)
# print(nested_seq[2][2][2][1])  # 17

########################
# Comparing collections
# print([2, 3] == [2, 3])          # True
# print([2, 3] == [3, 2])          # False - different seq
# print([2, 3] == [2])             # False - different lengths
# print([2, 3] == (2, 3))          # False - different types
# print({2, 3} == {3, 2})          # True - same members of set

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dict1 == dict2)             # True - same key/value pairs
print(dict1 == dict3)             # False - different lengths
