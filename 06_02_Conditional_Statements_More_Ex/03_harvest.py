from math import floor, ceil

vineyard_size = int(input())
grapes_per_sqm = float(input())
liters_wine_needed = int(input())
workers_amount = int(input())

total_grapes = vineyard_size * grapes_per_sqm
grapes_for_wine = total_grapes * 0.4
liters_of_wine = grapes_for_wine / 2.5

if liters_of_wine < liters_wine_needed:
    print(f'It will be a tough winter! More {floor(liters_wine_needed - liters_of_wine)} liters wine needed.')
elif liters_of_wine >= liters_wine_needed:
    print(f'Good harvest this year! Total wine: {floor(liters_of_wine)} liters.')
    print(f'{ceil(liters_of_wine - liters_wine_needed)} liters left -> {ceil((liters_of_wine - liters_wine_needed) / workers_amount)} liters per person.')
