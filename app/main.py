from functions import Functions


def main():
    actions = {
        "1": ("Add user", Functions.userAdd),
        "2": ("Delete user", Functions.deleteUser),
        "3": ("Change password", Functions.userPassword),
        "4": ("Append to group", Functions.appendToGroup),
        "5": ("Change name", Functions.changeName),
        "6": ("Change shell", Functions.changeShell),
        "7": ("Add group", Functions.groupAdd),
        "8": ("List users", Functions.listUsers),
        "9": ("List groups", Functions.listGroups),
        "10": ("List user-groups info", Functions.listUserGroups),
        "11": ("List group info", Functions.listGroupInfo),
        "12": ("List home dir", Functions.getHomeDir),
        "0": ("Exit", None),
    }

    while True:
        print("\n--- MENU ---")
        for key, (title, _) in actions.items():
            print(f"{key}. {title}")

        choice = input("> ").strip()

        if choice == "0":
            break

        action = actions.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid selection")

main()
