def password(correct):
    while True:
        password = input("enter you password: ")
        if password == correct:
            print("password is correct!")
            break
        else:
            print("password isn't correct, try again")

password("goabest11")