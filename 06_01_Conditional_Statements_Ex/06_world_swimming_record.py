from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

times_slowed = floor(distance/15)

final_time = distance * seconds_per_meter + times_slowed * 12.5

if final_time < record:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {final_time-record:.2f} seconds slower.')
