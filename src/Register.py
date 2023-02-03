class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


def register(users, Fore, Style):
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT + "-------REGISTER-------")
    username = input(Style.BRIGHT+"Insert Username: ")
    password = input(Style.BRIGHT+"Insert Password: ")
    addUser(username, password, users)


def addUser(login, password, users):
    user = User(login, password)
    users.append(user)
