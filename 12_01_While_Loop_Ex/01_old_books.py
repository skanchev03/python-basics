book_needed = input()

book_counter = 0

while True:
    book = input()

    if book == book_needed:
        print(f"You checked {book_counter} books and found it.")
        break
    elif book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    else:
        book_counter += 1
