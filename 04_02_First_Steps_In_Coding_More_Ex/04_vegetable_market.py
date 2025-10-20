vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

price_in_bgn = vegetable_price * vegetable_kg + fruit_price * fruit_kg

price_in_eur = price_in_bgn / 1.94

print(f'{price_in_eur:.2f}')
