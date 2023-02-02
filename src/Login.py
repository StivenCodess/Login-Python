class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


users = []


def menu():
    while True:
        menuOp = int(
            input("1-Login\n2-Register\n3-Show Users\n4-Exit\nOption:"))
        match menuOp:
            case 1:
                login()
            case 2:
                register()
            case 3:
                showUsers()
            case 4:
                return False
            case _:
                print("You inserted wrong number")
                return False


def login():
    print("-----LOGIN-----")
    login = input("Insert Username: ")
    password = input("Insert Password: ")


def addUser(login, password):
    user = User(login, password)
    users.append(user)


def showUsers():
    for userf in users:
        print(userf.name)


def register():
    print("-----REGISTER-----")
    username = input("Insert Username: ")
    password = input("Insert Password: ")
    addUser(username, password)


menu()
