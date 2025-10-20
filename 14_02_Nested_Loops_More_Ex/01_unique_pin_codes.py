num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for n1 in range(1, num_1 + 1):
    for n2 in range(1, num_2 + 1):
        for n3 in range(1, num_3 + 1):
            if n1 % 2 == 0 and n3 % 2 == 0 and (n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7):
                print(f"{n1} {n2} {n3}")
