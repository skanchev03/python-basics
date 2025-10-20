n = int(input())
l = int(input())

for sym1 in range(1, n + 1):
    for sym2 in range(1, n + 1):
        for sym3 in range(1, l + 1):
            for sym4 in range(1, l + 1):
                for sym5 in range(1, n + 1):
                    if sym5 > sym1 and sym5 > sym2:
                        print(f"{sym1}{sym2}{chr(sym3 + 96)}{chr(sym4 + 96)}{sym5}",end=" ")
