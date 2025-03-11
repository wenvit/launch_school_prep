#value = 5     # 5 is truthy
#value = 0      # 0 is falsy

# if value:
#     print(f'{value} is truthy')
# else:
#     print(f'{value} is falsy')

#############

# and operator evaluates both operands
# print(3 and 'foo')
# print('foo' and 3)
# print(0 and 'foo')
# print('foo' and 0)

# or operator short-circuits if first operand is truthy

# print(3 or 'foo')
# print('foo' or 3)
# print(0 or 'foo')
# print('foo' or 0)
# print('' or 0)
# print(None or [])

foo = None
bar = 'qux'
#is_ok = foo or bar   # is_ok gets set to the truthy value
#is_ok = bar or foo

# print(is_ok)

# Using a string as a boolean isn't good coding practice

# a better way is to use if/else

#if foo or bar:
# if bar or foo:
#     is_ok = True
# else:
#     is_ok = False

# print(is_ok)

# is_ok = bool(bar or foo)

# print(is_ok)

# print(bool(bar or foo))

# print(bool(None))

# print(bool('foo'))

#############
# print(1 or 2 and 3)
# print(0 or 2 and 3)
# print(1 or 0 and 3)
# print(1 or 2 and 0)
# print(0 or 0 and 3)
# print(0 or 2 and 0)
# print(1 or 0 and 0)
# print(0 or 0 and 0)

# print(1 and 2 or 3)
# print(0 and 2 or 3)
# print(1 and 0 or 3)
# print(1 and 2 or 0)
# print(0 and 0 or 3)
# print(0 and 2 or 0)
# print(1 and 0 or 0)
# print(0 and 0 or 0)

a = 1
b = 0
c = 0
d = 2

print((a and b) or (c and d))
print(a and b or c and d)

