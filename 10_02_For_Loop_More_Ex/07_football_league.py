stadium_capacity = int(input())
fans_amount = int(input())

a_counter = 0
b_counter = 0
v_counter = 0
g_counter = 0

for i in range(1, fans_amount + 1):
    sector = input()

    if sector == "A":
        a_counter += 1
    elif sector == "B":
        b_counter += 1
    elif sector == "V":
        v_counter += 1
    elif sector == "G":
        g_counter += 1

print(f"{a_counter / fans_amount * 100:.2f}%")
print(f"{b_counter / fans_amount * 100:.2f}%")
print(f"{v_counter / fans_amount * 100:.2f}%")
print(f"{g_counter / fans_amount * 100:.2f}%")
print(f"{fans_amount / stadium_capacity * 100:.2f}%")
