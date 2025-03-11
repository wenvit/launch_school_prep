# 6. Write a program named age.py that includes someone's age and 
# then calculates and reports the future age 10, 20, 30, and 40 years 
# from now. Here's the output for someone who is 22 years old.

print('Enter your current age:')
age = int(input())

########## my first clunky solution
# future_age10 = age + 10
# future_age20 = age + 20
# future_age30 = age + 30
# future_age40 = age + 40

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {future_age10} years old.')
# print(f'In 20 years, you will be {future_age20} years old.')
# print(f'In 30 years, you will be {future_age30} years old.')
# print(f'In 40 years, you will be {future_age40} years old.')

########## Launch School's more streamlined approach
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

########## Refactor to reduce repetition

future_years = [10, 20, 30, 40]

print(f'You are {age} years old.')

for year in future_years:
    print(f'In {year} years, you will be {age + year} years old.')
