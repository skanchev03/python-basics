city = input()
sales = float(input())



if city == "Sofia":
    if 0 <= sales <= 500:
        sales *= 0.05
        print(f"{sales:.2f}")
    elif 500 < sales <= 1000:
        sales *= 0.07
        print(f"{sales:.2f}")
    elif 1000 < sales <= 10000:
        sales *= 0.08
        print(f"{sales:.2f}")
    elif sales > 10000:
        sales *= 0.12
        print(f"{sales:.2f}")
    else:
        print("error")

if city == "Varna":
    if 0 <= sales <= 500:
        sales *= 0.045
        print(f"{sales:.2f}")
    elif 500 < sales <= 1000:
        sales *= 0.075
        print(f"{sales:.2f}")
    elif 1000 < sales <= 10000:
        sales *= 0.1
        print(f"{sales:.2f}")
    elif sales > 10000:
        sales *= 0.13
        print(f"{sales:.2f}")
    else:
        print("error")

if city == "Plovdiv":
    if 0 <= sales <= 500:
        sales *= 0.055
        print(f"{sales:.2f}")
    elif 500 < sales <= 1000:
        sales *= 0.08
        print(f"{sales:.2f}")
    elif 1000 < sales <= 10000:
        sales *= 0.12
        print(f"{sales:.2f}")
    elif sales > 10000:
        sales *= 0.145
        print(f"{sales:.2f}")
    else:
        print("error")

if city == "Sofia" or city == "Varna" or city == "Plovdiv":
    pass
else:
    print("error")
