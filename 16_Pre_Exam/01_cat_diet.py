fats_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
total_calories = int(input())
water_percent = int(input())

fats_grams = (total_calories * (fats_percent / 100)) / 9
protein_grams = (total_calories * (protein_percent / 100)) / 4
carbs_grams = (total_calories * (carbs_percent / 100)) / 4

grams = fats_grams + protein_grams + carbs_grams

calorie_per_gram = total_calories / grams

calories = calorie_per_gram * ((100 - water_percent) / 100)

print(f"{calories:.4f}")
