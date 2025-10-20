time_one = int(input())
time_two = int(input())
time_three = int(input())

combined_time = time_one + time_two + time_three

minutes = combined_time // 60
seconds = combined_time % 60

print(f'{minutes}:{seconds:02d}')
