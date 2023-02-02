from prettytable import PrettyTable, DOUBLE_BORDER
usersTable = PrettyTable(["Users", "Password"])
usersTable.align = "l"
usersTable.set_style(DOUBLE_BORDER)


def showUsers(users):
    usersTable.clear_rows()
    for userf in users:
        usersTable.add_row([userf.name, userf.password])
    print(usersTable)
    input("Press enter to continue")
