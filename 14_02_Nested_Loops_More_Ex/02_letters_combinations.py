start = input()
end = input()
miss = input()
counter = 0

for l1 in range(ord(start), ord(end) + 1):
    for l2 in range(ord(start), ord(end) + 1):
        for l3 in range(ord(start), ord(end) + 1):
            if chr(l1) == miss:
                continue
            elif chr(l2) == miss:
                continue
            elif chr(l3) == miss:
                continue
            else:
                print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end= " ")
                counter += 1
print(counter, end=" ")
