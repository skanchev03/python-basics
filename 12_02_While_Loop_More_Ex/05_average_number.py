n = int(input())

counter = 0

for i in range(1, n + 1):
    num = int(input())

    counter += num

print(f"{counter / n:.2f}")
