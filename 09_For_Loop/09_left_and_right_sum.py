n = int(input())

counter_1 = 0
counter_2 = 0

for i in range(1, n+1):
    num_1 = int(input())

    counter_1 += num_1

for i in range(1, n + 1):
    num_2 = int(input())

    counter_2 += num_2

if counter_1 == counter_2:
    print(f"Yes, sum = {counter_1}")
else:
    print(f"No, diff = {abs(counter_1 - counter_2)}")
