exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

total_exam_minutes = exam_hours * 60 + exam_minutes
total_arrival_minutes = arrival_hours * 60 + arrival_minutes
hours = 0
minutes = 0

difference_in_minutes = total_exam_minutes - total_arrival_minutes

if 0 <= difference_in_minutes <= 30:
    print("On time")
    if difference_in_minutes != 0:
        print(f"{difference_in_minutes} minutes before the start")

if difference_in_minutes > 30:
    print("Early")
    if difference_in_minutes < 60:
        print(f"{difference_in_minutes} minutes before the start")
    elif difference_in_minutes >= 60:
        hours = difference_in_minutes // 60
        minutes = difference_in_minutes % 60
        print(f"{hours}:{minutes:02d} hours before the start")

if difference_in_minutes < 0:
    print("Late")
    if difference_in_minutes > -60:
        print(f"{abs(difference_in_minutes)} minutes after the start")
    elif difference_in_minutes <= -60:
        hours = abs(difference_in_minutes) // 60
        minutes = abs(difference_in_minutes) % 60
        print(f"{hours}:{minutes:02d} hours after the start")
