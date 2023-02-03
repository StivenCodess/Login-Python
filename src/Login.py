def login(users, Fore, Style):
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT + "-------LOGIN-------")
    login = input(Style.BRIGHT+"Insert Username: ")
    password = input(Style.BRIGHT+"Insert Password: ")
    for userf in users:
        if ((login == userf.name) & (password == userf.password)):
            print(Fore.GREEN+Style.BRIGHT+"You have successfully logged in ✓")
        else:
            print(Fore.RED+Style.BRIGHT+"Failed to login ✕")
