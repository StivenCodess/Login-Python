class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


def register(users):
    print("-----REGISTER-----")
    username = input("Insert Username: ")
    password = input("Insert Password: ")
    addUser(username, password, users)


def addUser(login, password, users):
    user = User(login, password)
    users.append(user)
