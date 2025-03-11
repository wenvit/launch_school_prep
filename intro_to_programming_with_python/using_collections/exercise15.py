# 15. Without running the following code, what values will be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()       # keys is assigned to return value of pets.keys() 
                         # which is dict_keys(['Cat', 'Dog', 'Bird'])
del pets['Dog']          # key/value pair associated with key 'Dog' deleted from pets dict
pets['Snake'] = 'Sssss'  # 'Snake' key added to pets dict with value of 'Sssss'
print(keys)              # dict_keys(['Cat', 'Bird', 'Snake'])
