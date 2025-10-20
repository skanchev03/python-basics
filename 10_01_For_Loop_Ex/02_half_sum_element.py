import sys

n = int(input())

max_num = -sys.maxsize
counter = 0

for i in range(1,n + 1):
    num = int(input())

    if num > max_num:
        max_num = num

    counter += num

counter -= max_num

if counter == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(counter - max_num)}")
