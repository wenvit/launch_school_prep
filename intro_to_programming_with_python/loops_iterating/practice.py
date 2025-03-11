###### while loops


#names = ['Chris', 'Max', 'Karis', 'Victor']
# upper_names = []
# index = 0

# while index < len(names):
#     upper_name = names[index].upper()
#     upper_names.append(upper_name)
#     index += 1

# print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

########
# for loop

# names = ['Chris', 'Max', 'Karis', 'Victor']
# upper_names = []

# for name in names:
#     upper_name = name.upper()
#     upper_names.append(upper_name)

# print(upper_names)

# for char in 'Launch School':
#     print(char)

# for word in 'Launch School'.split():
#     print(word)

# my_set = {1000, 2000, 3000, 4000, 5000}

# for member in my_set:   # note: print order isn't always same because it's a set
#     print(member)

# Looping over a dictionary
#my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:   # by default, using for loop with dict iterates over keys
#     print(key)

# for value in my_dict.values():
#     print(value)

# for item in my_dict.items():
#     print(item)

# for key, value in my_dict.items():
#     print(f'{key} = {value}')

############
# Nested loops


# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# ranks = [
#     '2', '3', '4', '5', '6', '7', '8', '9', '10',
#     'Jack', 'Queen', 'King', 'Ace',
# ]

# deck = []

# for suit in suits:
#     for rank in ranks:
#         card = f'{rank} of {suit}'
#         deck.append(card)

# print(deck)


##################
# Controlling Loops

# continue

# names = ['Chris', 'Max', 'Karis', 'Victor']
# upper_names = []

# for name in names:

#     if name == 'Max':
#         continue

#     upper_name = name.upper()
#     upper_names.append(upper_name)

# print(upper_names)

# break

###################
# simultaneous iteration

# manual example using while

# forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
# surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

# index = 0
# while index < len(forenames):
#     if index >= len(surnames): # surnames might be shorter
#         break

#     forename = forenames[index]
#     surname = surnames[index]
#     print(f'{forename} {surname}')

#     index += 1

# a better way with zip
# Note that zip takes care of potential problem of dealing
# with lists of different sizes, so don't need code to deal
# with list of surnames shorter than forenames

# complete_names = zip(forenames, surnames)

# for forename, surname in complete_names:
#     print(f'{forename} {surname}')

