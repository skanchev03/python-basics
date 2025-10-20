budget = float(input())
extras = int(input())
outfit_price = float(input())

decor = budget * 0.10

total_outfit_price = extras * outfit_price

if extras > 150:
    total_outfit_price = total_outfit_price * 0.90

total_price = decor + total_outfit_price

if total_price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {abs(total_price - budget):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(total_price - budget):.2f} leva more.')
