n = int(input())

for i in range(0, n+1):
    if i == 0:
        print(" " * (n+1) + "|" + " " * (n+1))
    else:
        print(" " * (n-i) + "*" * i + " | " + "*" * i + " " * (n - i))
