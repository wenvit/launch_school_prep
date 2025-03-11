##### Problem statement

# Count the number of elements in scores that are 100 or above.

# scores = [96, 47, 113, 89, 100, 102]

##### Solution

scores = [96, 47, 113, 89, 100, 102]  # 3

count = 0

for num in scores:
    if num >= 100:
        count += 1

print(count)

# Launch School approach using list comprehension - more pythonic

count = [1 for num in scores if num >= 100]
print(sum(count))
