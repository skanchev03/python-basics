from math import ceil

n = int(input())

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * (2 * n) + " " * n + "*" * (2 * n))
    else:
        if n % 2 == 0:
            if i == n / 2:
                print("*" + "/" * (2*n-2) + "*" + "|" * n + "*" + "/" * (2*n-2) + "*")
            else:
                print("*" + "/" * (2 * n - 2) + "*" + " " * n + "*" + "/" * (2 * n - 2) + "*")
        if n % 2 == 1:
            if i == ceil(n / 2):
                print("*" + "/" * (2 * n - 2) + "*" + "|" * n + "*" + "/" * (2 * n - 2) + "*")
            else:
                print("*" + "/" * (2 * n - 2) + "*" + " " * n + "*" + "/" * (2 * n - 2) + "*")
