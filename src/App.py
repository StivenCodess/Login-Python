import Login
import ShowUsers
import Register
from colorama import Fore, init, Style
init(autoreset=True)


users = []


def menu():
    while True:
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"-------MENU-------")
        menuOp = int(
            input(Style.BRIGHT+"1-Login\n2-Register\n3-Show Users\n4-Exit" + Fore.GREEN + "\nOption:"))
        match menuOp:
            case 1:
                Login.login(users, Fore, Style)
            case 2:
                Register.register(users, Fore, Style)
            case 3:
                ShowUsers.showUsers(users, Fore, Style, init)
            case 4:
                return False
            case _:
                print("You inserted wrong number")
                return False


menu()
