n = int(input())

weight_counter = 0
bus_counter = 0
truck_counter = 0
train_counter = 0
price = 0

for i in range(1, n + 1):
    weight = int(input())

    weight_counter += weight

    if weight <= 3:
        bus_counter += weight
        price += weight * 200
    elif weight <= 11:
        truck_counter += weight
        price += weight * 175
    else:
        train_counter += weight
        price += weight * 120

print(f"{price / weight_counter:.2f}")
print(f"{bus_counter / weight_counter * 100:.2f}%")
print(f"{truck_counter / weight_counter * 100:.2f}%")
print(f"{train_counter / weight_counter * 100:.2f}%")
