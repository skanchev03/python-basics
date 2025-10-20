inheritance_money = float(input())
year_to_live = int(input())

expenses = 0

for i in range(1, year_to_live - 1798):
    if (i + 1799) % 2 == 0:
        expenses += 12000
    else:
        expenses += 12000 + 50 * (18 + i - 1)

if inheritance_money >= expenses:
    print(f"Yes! He will live a carefree life and will have {inheritance_money - expenses:.2f} dollars left.")
else:
    print(f"He will need {expenses - inheritance_money:.2f} dollars to survive.")
