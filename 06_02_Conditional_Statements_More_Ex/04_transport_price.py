kilometers = int(input())
time_of_day = input()

if time_of_day == 'day':
    if kilometers < 20:
        print(f'{0.7 + kilometers * 0.79:.2f}')
    elif kilometers < 100:
        print(f'{kilometers * 0.09:.2f}')
    else:
        print(f'{kilometers * 0.06:.2f}')
elif time_of_day == 'night':
    if kilometers < 20:
        print(f'{0.7 + kilometers * 0.9:.2f}')
    elif kilometers < 100:
        print(f'{kilometers * 0.09:.2f}')
    else:
        print(f'{kilometers * 0.06:.2f}')
