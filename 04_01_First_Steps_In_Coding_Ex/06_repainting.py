nylon_needed = float(input())
paint_needed = float(input())
thinner_needed = float(input())
hours_needed = float(input())

nylon_price = (nylon_needed + 2) * 1.5
paint_price = (paint_needed + paint_needed * 0.1) * 14.5
thinner_price = thinner_needed * 5
materials_price = nylon_price + paint_price + thinner_price + 0.4

worker_rate = materials_price * 0.3
worker_price = worker_rate * hours_needed

final_price = materials_price + worker_price

print(final_price)
