from math import pi

figure = input()

area = 0

if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == 'circle':
    radius = float(input())
    area = pi * radius ** 2
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2
else:
    pass

print(f'{area:.3f}')
