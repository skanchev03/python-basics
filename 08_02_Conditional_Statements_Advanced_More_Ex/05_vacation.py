budget = float(input())
season = input()

if budget <= 1000:
    if season == "Summer":
        print(f"Alaska - Camp - {budget * 0.65:.2f}")
    elif season == "Winter":
        print(f"Morocco - Camp - {budget * 0.45:.2f}")
elif budget <= 3000:
    if season == "Summer":
        print(f"Alaska - Hut - {budget * 0.8:.2f}")
    elif season == "Winter":
        print(f"Morocco - Hut - {budget * 0.6:.2f}")
else:
    if season == "Summer":
        print(f"Alaska - Hotel - {budget * 0.9:.2f}")
    elif season == "Winter":
        print(f"Morocco - Hotel - {budget * 0.9:.2f}")
