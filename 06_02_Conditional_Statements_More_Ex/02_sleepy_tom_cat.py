days_off = int(input())

days_working = 365 - days_off

minutes_play = days_off * 127 + days_working * 63

time = 0
hours = 0
minutes = 0

if minutes_play < 30000:
    time = 30000 - minutes_play
    hours = time // 60
    minutes = time % 60

    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    time = minutes_play - 30000
    hours = time // 60
    minutes = time % 60

    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
