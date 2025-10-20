budget = float(input())
season = input()

if budget <= 100:
    print("Economy class")
    if season == "Summer":
        print(f"Cabrio - {budget * 0.35:.2f}")
    elif season == "Winter":
        print(f"Jeep - {budget * 0.65:.2f}")
elif budget <= 500:
    print("Compact class")
    if season == "Summer":
        print(f"Cabrio - {budget * 0.45:.2f}")
    elif season == "Winter":
        print(f"Jeep - {budget * 0.8:.2f}")
else:
    print("Luxury class")
    print(f"Jeep - {budget * 0.9:.2f}")
