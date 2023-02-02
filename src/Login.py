

def login(users):
    print("-----LOGIN-----")
    login = input("Insert Username: ")
    password = input("Insert Password: ")
    for userf in users:
        if ((login == userf.name) & (password == userf.password)):
            print("You have successfully logged in")
        else:
            print("Failed to login")
