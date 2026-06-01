def check_password(password):
    if len(password) < 8:
        print("password must have at least 8 characters")
    elif not any(char.isdigit() for char in password):
        print("password must contain a number")
    elif not any(char.isupper() for char in password):
        print("password must contain an uppercase letter")
    else:
        print("strong password")
password= input("enter password:")
check_password(password)