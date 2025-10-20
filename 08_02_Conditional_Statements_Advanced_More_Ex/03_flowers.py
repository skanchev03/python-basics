chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0

if holiday == "Y":
    if season == "Spring" or season == "Summer":
        chrysanthemums_price = 2 * 1.15
        roses_price = 4.1 * 1.15
        tulips_price = 2.5 * 1.15
    elif season == "Autumn" or season == "Winter":
        chrysanthemums_price = 3.75 * 1.15
        roses_price = 4.5 * 1.15
        tulips_price = 4.15 * 1.15
elif holiday == "N":
    if season == "Spring" or season == "Summer":
        chrysanthemums_price = 2
        roses_price = 4.1
        tulips_price = 2.5
    elif season == "Autumn" or season == "Winter":
        chrysanthemums_price = 3.75
        roses_price = 4.5
        tulips_price = 4.15

bouquet_price = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price

if season == "Spring":
    if tulips > 7:
        bouquet_price *= 0.95

if season == "Winter":
    if roses >= 10:
        bouquet_price *= 0.9

flowers = chrysanthemums + roses + tulips

if flowers > 20:
    bouquet_price *= 0.8

bouquet_price += 2

print(f"{bouquet_price:.2f}")
