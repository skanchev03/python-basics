chicken_menu = float(input())
fish_menu = float(input())
vegi_menu = float(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.4
vegi_price = vegi_menu * 8.15
food_price = chicken_price + fish_price + vegi_price

dessert_price = food_price * 0.2

final_price = food_price + dessert_price + 2.5

print(final_price)
