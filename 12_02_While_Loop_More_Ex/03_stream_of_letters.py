c_counter = 0
o_counter = 0
n_counter = 0
secret_counter = 0
word = ""
current_word = ""

while True:
    letter = input()

    if letter == "c":
        c_counter += 1
        if c_counter == 1:
            if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
                word += current_word + " "
                current_word = ""
                c_counter = 0
                o_counter = 0
                n_counter = 0
                continue
            else:
                continue

    if letter == "o":
        o_counter += 1
        if o_counter == 1:
            if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
                word += current_word + " "
                current_word = ""
                c_counter = 0
                o_counter = 0
                n_counter = 0
                continue
            else:
                continue

    if letter == "n":
        n_counter += 1
        if n_counter == 1:
            if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
                word += current_word + " "
                current_word = ""
                c_counter = 0
                o_counter = 0
                n_counter = 0
                continue
            else:
                continue

    if len(letter) == 1 and letter.isalpha():
        current_word += letter

    if letter == "End":
        print(word)
        break
