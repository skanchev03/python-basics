type_of_projection = input()
rows = int(input())
columns = int(input())

profit = 0

if type_of_projection == "Premiere":
    profit = rows * columns * 12
elif type_of_projection == "Normal":
    profit = rows * columns * 7.5
elif type_of_projection == "Discount":
    profit = rows * columns * 5
else:
    pass

print(f"{profit:.2f} leva")
