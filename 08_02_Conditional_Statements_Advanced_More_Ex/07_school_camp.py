season = input()
group = input()
group_amount = int(input())
nights_amount = int(input())

price = 0

if season == "Winter":
    if group == "boys":
        if group_amount >= 50:
            price = group_amount * 9.6 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 9.6 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 9.6 * nights_amount * 0.95
        else:
            price = group_amount * 9.6 * nights_amount
        print(f"Judo {price:.2f} lv.")
    elif group == "girls":
        if group_amount >= 50:
            price = group_amount * 9.6 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 9.6 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 9.6 * nights_amount * 0.95
        else:
            price = group_amount * 9.6 * nights_amount
        print(f"Gymnastics {price:.2f} lv.")
    elif group == "mixed":
        if group_amount >= 50:
            price = group_amount * 10 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 10 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 10 * nights_amount * 0.95
        else:
            price = group_amount * 10 * nights_amount
        print(f"Ski {price:.2f} lv.")
elif season == "Spring":
    if group == "boys":
        if group_amount >= 50:
            price = group_amount * 7.2 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 7.2 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 7.2 * nights_amount * 0.95
        else:
            price = group_amount * 7.2 * nights_amount
        print(f"Tennis {price:.2f} lv.")
    elif group == "girls":
        if group_amount >= 50:
            price = group_amount * 7.2 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 7.2 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 7.2 * nights_amount * 0.95
        else:
            price = group_amount * 7.2 * nights_amount
        print(f"Athletics {price:.2f} lv.")
    elif group == "mixed":
        if group_amount >= 50:
            price = group_amount * 9.5 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 9.5 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 9.5 * nights_amount * 0.95
        else:
            price = group_amount * 9.5 * nights_amount
        print(f"Cycling {price:.2f} lv.")
elif season == "Summer":
    if group == "boys":
        if group_amount >= 50:
            price = group_amount * 15 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 15 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 15 * nights_amount * 0.95
        else:
            price = group_amount * 15 * nights_amount
        print(f"Football {price:.2f} lv.")
    elif group == "girls":
        if group_amount >= 50:
            price = group_amount * 15 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 15 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 15 * nights_amount * 0.95
        else:
            price = group_amount * 15 * nights_amount
        print(f"Volleyball {price:.2f} lv.")
    elif group == "mixed":
        if group_amount >= 50:
            price = group_amount * 20 * nights_amount * 0.5
        elif group_amount >= 20:
            price = group_amount * 20 * nights_amount * 0.85
        elif group_amount >= 10:
            price = group_amount * 20 * nights_amount * 0.95
        else:
            price = group_amount * 20 * nights_amount
        print(f"Swimming {price:.2f} lv.")
