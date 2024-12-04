

expenses=[10000,11000,12000,15000,14000]

total=0

avg_exp=0

for exp in expenses:

    total=total+exp

    avg_exp=total//len(expenses)

print(avg_exp)