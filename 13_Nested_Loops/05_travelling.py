while True:
    destination = input()

    if destination == "End":
        break

    budget = float(input())
    target = 0

    while True:
        money = float(input())
        target += money
        if target >= budget:
            break

    print(f"Going to {destination}!" )
