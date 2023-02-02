from prettytable import PrettyTable, DOUBLE_BORDER

usersTable = PrettyTable(["Users", "Password"])
usersTable.align = "l"
usersTable.set_style(DOUBLE_BORDER)


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


users = []


def menu():
    while True:
        menuOp = int(
            input("1-Login\n2-Register\n3-Show Users\n4-Probar pretty Table\n5-Exit\nOption:"))
        match menuOp:
            case 1:
                login()
            case 2:
                register()
            case 3:
                showUsers()
            case 4:
                usersTable.add_row(["Pepe", "1234"])
                usersTable.add_row(["Pepe", "1234"])
                print(usersTable)
            case 5:
                return False
            case _:
                print("You inserted wrong number")
                return False


def login():
    print("-----LOGIN-----")
    login = input("Insert Username: ")
    password = input("Insert Password: ")
    for userf in users:
        if ((login == userf.name) & (password == userf.password)):
            print("You have successfully logged in")
        else:
            print("Failed to login")


def addUser(login, password):
    user = User(login, password)
    users.append(user)


def showUsers():
    usersTable.clear_rows()
    for userf in users:
        usersTable.add_row([userf.name, userf.password])
    print(usersTable)
    input("Press enter to continue")


def register():
    print("-----REGISTER-----")
    username = input("Insert Username: ")
    password = input("Insert Password: ")
    addUser(username, password)


menu()
