def menu():
    menuOp = int(input("1-Login\n2-Register\n3-Exit\nOption:"))
    match menuOp:
        case 1:
            login()
        case 2:
            register()
        case 3:
            return False
        case _:
            print("You inserted wrong number")
            return True


def login():
    print("-----LOGIN-----")
    login = input("Insert Username: ")
    password = input("Insert Password: ")


def register():
    print("-----REGISTER-----")
    username = input("Insert Username: ")
    password = input("Insert Password: ")


condition = True
while condition:
    condition = menu()
