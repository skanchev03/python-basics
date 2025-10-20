length = float(input())
width = float(input())
height = float(input())
percent = float(input())

length_in_dm = length / 10
width_in_dm = width / 10
height_in_dm = height / 10
volume = length_in_dm * width_in_dm * height_in_dm
percent_empty = 1 - percent / 100

liters = volume * percent_empty

print(liters)
