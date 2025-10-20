room_length = float(input())
room_width = float(input())

room_width -= 1

desks_length_space = room_length // 1.2
desks_width_space = room_width // 0.7

desks_in_the_room = desks_length_space * desks_width_space - 3

print(desks_in_the_room)
