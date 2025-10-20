vacation_price = float(input())
puzzles_amount = int(input())
dolls_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

total_amount = puzzles_amount + dolls_amount + bears_amount + minions_amount + trucks_amount

puzzles_price = puzzles_amount * 2.60
dolls_price = dolls_amount * 3
bears_price = bears_amount * 4.10
minions_price = minions_amount * 8.20
trucks_price = trucks_amount * 2

total_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

if total_amount >= 50:
    total_price *= 0.75

rent_price = total_price * 0.1

income = total_price - rent_price

if income >= vacation_price:
    print(f'Yes! {abs(income - vacation_price):.2f} lv left.')
else:
    print(f'Not enough money! {abs(income - vacation_price):.2f} lv needed.')
