month = input()
days_stay = int(input())

apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    if days_stay <= 7:
        apartment_price = 65
        studio_price = 50
    elif days_stay <=14:
        apartment_price = 65
        studio_price = 50 * 0.95
    elif days_stay > 14:
        apartment_price = 65 * 0.9
        studio_price = 50 * 0.7

if month == "June" or month == "September":
    if days_stay <=14:
        apartment_price = 68.7
        studio_price = 75.2
    elif days_stay > 14:
        apartment_price = 68.7 * 0.9
        studio_price = 75.2 * 0.8

if month == "July" or month == "August":
    if days_stay <=14:
        apartment_price = 77
        studio_price = 76
    elif days_stay > 14:
        apartment_price = 77 * 0.9
        studio_price = 76

apartment_price *= days_stay
studio_price *= days_stay

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
