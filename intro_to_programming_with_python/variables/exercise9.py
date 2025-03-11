# 9. Repeat the previous question but, this time, use augmented assignment 
# to compute the final result, one year at a time.

balance = 1000
interest_rate = 0.05
interest_multiplier = 1 + interest_rate

for year in range(1, 6):
    balance *= interest_multiplier
    print(f'Bank balance at end of year {year}: {balance}')
