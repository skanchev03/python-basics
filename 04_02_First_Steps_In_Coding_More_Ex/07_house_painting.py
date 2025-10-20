x = float(input())
y = float(input())
h = float(input())

house_size = x * x * 2 + x * y * 2 - 1.2 * 2 - 1.5 * 1.5 * 2
green_paint_needed = house_size / 3.4

roof_size = x * y * 2 + x * h
red_paint_needed = roof_size / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
