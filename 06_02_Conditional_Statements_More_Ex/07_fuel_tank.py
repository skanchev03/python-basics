type_of_fuel = input()
amount_of_fuel = float(input())

if type_of_fuel == 'Diesel' or type_of_fuel == 'Gasoline' or type_of_fuel == 'Gas':
    if amount_of_fuel >= 25:
        print(f'You have enough {type_of_fuel.lower()}.')
    elif amount_of_fuel < 25:
        print(f'Fill your tank with {type_of_fuel.lower()}!')
else:
    print('Invalid fuel!')
