while True :
    password = input("Enter Your Password:")
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_8 = len(password) >= 8
    if has_letter and has_number and has_8:
        print("Password Accepted")
        break
    else:
        print("Invalid password. Try again.")