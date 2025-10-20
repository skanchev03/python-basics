weight = float(input())
type_of_delivery = input()
distance = int(input())

price = 0
express_price = 0

if type_of_delivery == "standard":
    if weight < 1:
        price = 3 * distance / 100
    elif weight < 10:
        price = 5 * distance / 100
    elif weight < 40:
        price = 10 * distance / 100
    elif weight < 90:
        price = 15 * distance / 100
    elif weight < 150:
        price = 20 * distance / 100

elif type_of_delivery == "express":
    if weight < 1:
        price = 3 * distance / 100
        express_price = 0.8 * 0.03 * weight * distance
    elif weight < 10:
        price = 5 * distance / 100
        express_price = 0.4 * 0.05 * weight * distance
    elif weight < 40:
        price = 10 * distance / 100
        express_price = 0.05 * 0.1 * weight * distance
    elif weight < 90:
        price = 15 * distance / 100
        express_price = 0.02 * 0.15 * weight * distance
    elif weight < 150:
        price = 20 * distance / 100
        express_price = 0.01 * 0.2 * weight * distance

total_price = price + express_price

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
