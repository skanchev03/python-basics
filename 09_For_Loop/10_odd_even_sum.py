n = int(input())

counter_1 = 0
counter_2 = 0

for i in range(1, n+1):
    num = int(input())

    if i % 2 == 0:
        counter_1 += num
    else:
        counter_2 += num

if counter_1 == counter_2:
    print("Yes")
    print(f"Sum = {counter_1}")
else:
    print("No")
    print(f"Diff = {abs(counter_1 - counter_2)}")
