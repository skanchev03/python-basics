n = int(input())

counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0

for i in range(1,n + 1):
    num = int(input())

    if num < 200:
        counter_1 += 1
    elif num < 400:
        counter_2 += 1
    elif num < 600:
        counter_3 += 1
    elif num < 800:
        counter_4 += 1
    elif num <= 1000:
        counter_5 += 1

print(f"{counter_1 / n * 100:.2f}%")
print(f"{counter_2 / n * 100:.2f}%")
print(f"{counter_3 / n * 100:.2f}%")
print(f"{counter_4 / n * 100:.2f}%")
print(f"{counter_5 / n * 100:.2f}%")
