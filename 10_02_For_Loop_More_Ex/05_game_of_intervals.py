n = int(input())

result = 0
zero_counter = 0
ten_counter = 0
twenty_counter = 0
thirty_counter = 0
forty_counter = 0
invalid_counter = 0

for i in range(1, n + 1):
    num = int(input())

    if num < 0 or num > 50:
        invalid_counter += 1
        result = result / 2
    else:
        if 0 <= num < 10:
            zero_counter += 1
            result += num * 0.2
        elif num < 20:
            ten_counter += 1
            result += num * 0.3
        elif num < 30:
            twenty_counter += 1
            result += num * 0.4
        elif num < 40:
            thirty_counter += 1
            result += 50
        elif num <= 50:
            forty_counter += 1
            result += 100

print(f"{result:.2f}")
print(f"From 0 to 9: {zero_counter / n * 100:.2f}%")
print(f"From 10 to 19: {ten_counter / n * 100:.2f}%")
print(f"From 20 to 29: {twenty_counter / n * 100:.2f}%")
print(f"From 30 to 39: {thirty_counter / n * 100:.2f}%")
print(f"From 40 to 50: {forty_counter / n * 100:.2f}%")
print(f"Invalid numbers: {invalid_counter / n * 100:.2f}%")
