from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_watching = break_duration - break_duration * 0.25 - break_duration * 0.125

if time_for_watching >= episode_duration:
    print(f'You have enough time to watch {series_name} and left with {ceil(abs(time_for_watching - episode_duration))} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {ceil(abs(time_for_watching - episode_duration))} more minutes.')
