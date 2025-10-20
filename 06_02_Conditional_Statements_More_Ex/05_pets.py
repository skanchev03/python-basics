from math import floor, ceil

days_missing = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_per_day = dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000

food_needed = food_per_day * days_missing

if food_left >= food_needed:
    print(f'{floor(food_left - food_needed)} kilos of food left.')
else:
    print(f'{ceil(food_needed-food_left)} more kilos of food are needed.')
