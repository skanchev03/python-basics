one = int(input())
two = int(input())
five = int(input())
price = int(input())

for i in range(0, one + 1):
    for j in range(0, two + 1):
        for k in range(0, five + 1):
            if (i * 1) + (j * 2) + (k * 5) == price:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {price} lv.")
