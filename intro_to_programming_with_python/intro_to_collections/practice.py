# letters = ['a', 'b', 'o', 'd', 'e']
# char = letters[2]
# print(letters)
# print(char)
# print(char is letters[2])

# letters = 'abode'
# char = letters[2]
# print(letters)
# print(char)
# print(char is letters[2])

# first_set = {1, 2, 3}
# second_set = {3, 2, 1}

# print(type(first_set))
# print(type(second_set))

# print(first_set == second_set)

# first_list = [1, 2, 3]
# second_list = [3, 2, 1]

# print(type(first_list))
# print(type(second_list))

# print(first_list == second_list)

# letters = {'a', 'b', 'c'}
# letters.add('d')
# print(letters)

# frozen_letters = frozenset(letters)
# frozen_letters.add('e')

d = {
    'a': 1,
    (1, 3): 3,
    1: 'x'
}

# print(d)
# print(d['a'])
# print(d[(1, 3)])
# print(d[1])

# d['a'] = 'A'
# print(d)

# d['a'] = 1
# print(d)

# del d['a']
# print(d)

# d['a'] = 42
# print(d)

# r = range(5, 12, 2) # [5, 7, 9, 11]
# print(list(r))

# r = range(12, 8, -1)  # [12, 11, 10, 9]
# print(list(r))

# r = range(12, 5, -2)  # [12, 10, 8, 6]


# the following create empty ranges
# r = range(5, 5, 1)
# print(list(r))

# r = range(5, 7, -1)
# print(list(r))

# my_str = 'Python'

# print(list(my_str))
# print(set(my_str))
# print(tuple(my_str))

# using a constructor to duplicate a list

# my_list = [5, 12, 2]
# another_list = list(my_list)

# print(my_list)
# print(another_list)

# print(my_list == another_list)
# print(my_list is another_list)

my_list = [[1, 2, 3], [4, 5, 6]]
another_list = list(my_list)

print(my_list)
print(another_list)

print(my_list == another_list)
print(my_list is another_list)
print(my_list[0] is another_list[0])
print(my_list[1] is another_list[1])