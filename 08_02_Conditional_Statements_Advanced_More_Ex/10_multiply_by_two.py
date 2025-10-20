while True:
    num = float(input())

    if num < 0:
        print("Negative number!")
        break
    else:
        print(f"Result: {num * 2:.2f}")
