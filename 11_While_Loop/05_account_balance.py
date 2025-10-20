counter = 0

while True:
    deposit = input()

    if deposit == "NoMoreMoney":
        break
    elif float(deposit) < 0:
        print("Invalid operation!")
        break
    else:
        counter += float(deposit)
        print(f"Increase: {float(deposit):.2f}")

print(f"Total: {counter:.2f}")
