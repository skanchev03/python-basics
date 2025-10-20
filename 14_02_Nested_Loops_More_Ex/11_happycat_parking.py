days = int(input())
hours = int(input())

price_counter = 0
total_price_counter = 0

for i in range(1, days + 1):
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 == 1:
            price_counter += 2.5
        elif i % 2 == 1 and j % 2 == 0:
            price_counter += 1.25
        else:
            price_counter += 1

    print(f"Day: {i} - {price_counter:.2f} leva")
    total_price_counter += price_counter
    price_counter = 0

print(f"Total: {total_price_counter:.2f} leva")
