width = int(input())
length = int(input())
height = int(input())

empty_space = width * length * height

boxes_counter = 0

while True:
    boxes = input()

    if boxes != "Done":
        boxes_counter += int(boxes)

    if boxes_counter > empty_space:
        print(f"No more free space! You need {boxes_counter - empty_space} Cubic meters more.")
        break

    if boxes == "Done":
        print(f"{empty_space - boxes_counter} Cubic meters left.")
        break
