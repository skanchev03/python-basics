username = input()
password = input()

while True:
    password_attempt = input()

    if password_attempt != password:
        pass
    else:
        print(f"Welcome {username}!")
        break
