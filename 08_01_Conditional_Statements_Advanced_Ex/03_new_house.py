type_of_flower = input()
flower_amount = int(input())
budget = int(input())

price = 0

if type_of_flower == "Roses":
    if 80 >= flower_amount:
        price = flower_amount * 5
    elif flower_amount > 80:
        price = flower_amount * 5 * 0.9

if type_of_flower == "Dahlias":
    if 90 >= flower_amount:
        price = flower_amount * 3.8
    elif flower_amount > 90:
        price = flower_amount * 3.8 * 0.85

if type_of_flower == "Tulips":
    if 80 >= flower_amount:
        price = flower_amount * 2.8
    elif flower_amount > 80:
        price = flower_amount * 2.8 * 0.85

if type_of_flower == "Narcissus":
    if 120 > flower_amount:
        price = flower_amount * 3 * 1.15
    elif flower_amount >= 120:
        price = flower_amount * 3

if type_of_flower == "Gladiolus":
    if 80 > flower_amount:
        price = flower_amount * 2.5 * 1.2
    elif flower_amount >= 80:
        price = flower_amount * 2.5

if budget >= price:
    print(f"Hey, you have a great garden with {flower_amount} {type_of_flower} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
