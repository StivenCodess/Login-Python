
import Register
import ShowUsers
import Login


users = []


def menu():
    while True:
        menuOp = int(
            input("1-Login\n2-Register\n3-Show Users\n4-Exit\nOption:"))
        match menuOp:
            case 1:
                Login.login(users)
            case 2:
                Register.register(users)
            case 3:
                ShowUsers.showUsers(users)
            case 4:
                return False
            case _:
                print("You inserted wrong number")
                return False


menu()
