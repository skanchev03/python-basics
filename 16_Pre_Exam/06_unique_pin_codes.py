num1_top = int(input())
num2_top = int(input())
num3_top = int(input())

for n1 in range(2, num1_top + 1):
    for n2 in range(2, num2_top + 1):
        for n3 in range(2, num3_top + 1):
            if n1 % 2 == 0 and n3 % 2 == 0 and (n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7):
                print(f"{n1} {n2} {n3}")
