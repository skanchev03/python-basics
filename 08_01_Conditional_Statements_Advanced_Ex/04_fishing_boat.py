budget = int(input())
season = input()
fisherman_amount = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600
else:
    pass

discount = 0

if fisherman_amount <= 6:
    discount = 0.9
elif fisherman_amount <= 11:
    discount = 0.85
else:
    discount = 0.75

additional_discount = 1

if fisherman_amount % 2 == 0:
    if season == "Spring" or season == "Summer" or season == "Winter":
        additional_discount = 0.95

final_price = boat_price * discount * additional_discount

if budget >= final_price:
    print(f"Yes! You have {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva.")
