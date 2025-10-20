fruit = input()
day_of_week = input()
quantity = float(input())

price = 0.0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        price = 2.5
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = 1.2
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = 0.85
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = 2.7
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = 5.5
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = 3.85
        price *= quantity
        print(f"{price:.2f}")
    else:
        print("error")

if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = 2.7
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = 1.25
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = 0.9
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = 1.6
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = 3
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = 5.6
        price *= quantity
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = 4.2
        price *= quantity
        print(f"{price:.2f}")
    else:
        print("error")

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday" or day_of_week == "Sunday":
    pass
else:
    print("error")
