# exercise_4_login_manager.py

def get_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        login(username, password)
    except PermissionError:
        print("You do not have permission!")


def login(username, password):
    pass
