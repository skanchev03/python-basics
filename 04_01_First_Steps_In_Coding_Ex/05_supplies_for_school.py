pens_to_buy = float(input())
markers_to_buy = float(input())
cleaner_to_buy = float(input())
discount = float(input())

pens_price = pens_to_buy * 5.8
markers_price = markers_to_buy * 7.2
cleaner_price = cleaner_to_buy * 1.2

price_before_discount = pens_price + markers_price + cleaner_price
price_after_discount = price_before_discount - price_before_discount * (discount / 100)

print(price_after_discount)
