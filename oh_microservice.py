def user_login():
    email = input("enter email: ")
    pswd = input("enter password: ")

    with open("login-data.txt", "r") as f:
        credentials = f.read().split('\n')

    if email == credentials[0] and pswd == credentials[1]:
        with open("order_history.txt", "r") as f:
            order = f.read()
            print(order)
    else:
        print("incorrect email or password")

user_login()