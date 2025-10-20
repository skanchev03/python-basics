from math import floor, ceil

magnolias_amount = int(input())
hyacinths_amount = int(input())
roses_amount = int(input())
cacti_amount = int(input())
gift_price = float(input())

magnolias_price = magnolias_amount * 3.25
hyacinths_price = hyacinths_amount * 4
roses_price = roses_amount * 3.5
cacti_price = cacti_amount * 8

total_price = magnolias_price + hyacinths_price + roses_price + cacti_price
price_after_tax = total_price * 0.95

if price_after_tax >= gift_price:
    print(f'She is left with {floor(price_after_tax - gift_price)} leva.')
else:
    print(f'She will have to borrow {ceil(gift_price - price_after_tax)} leva.')
