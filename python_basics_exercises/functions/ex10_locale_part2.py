##### Problem statement

# Similar to the previous exercise, write a function that 
# extracts the region code from a locale. For example:

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

##### Solution

# One way based on slicing

# def extract_region(locale):
#     return locale[3:5]

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

# another way

def extract_region(locale):
    sub1 = locale.split('_')[1]
    region = sub1.split('.')[0]  # can also chain these split steps
    return region

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR