users = {}

NAME = "Name"
PASSWORD = "Password"
LOGGED_IN = "Logged In"


def main():
    create_account("user1", "Harry", "IamHarryPotter")
    create_account("user2", "Hermione", "Granger")
    create_account("user3", "Ron", "weasleypass")
        
    change_password("user1", "IamHarryPotter", "HotPot")
    change_password("user2", "Granger", "Ginger")
    change_password("user3", "Ron", "Weasle")
    
    login("user1", "IamHarryPotter")
    login("user2", "Granger")
    login("user3", "weasleypass")
    
    change_password("user1", "IamHarryPotter", "HotPot")
    change_password("user0", "Granger", "Ginger")
    change_password("user3", "weasleypas", "Weasle")
    
    logout("user1")
    logout("user2")
    logout("user3")
    
    login("user4", "Granger") # should quit 
    


def get_user_info(user, info):
    return users[user][info]


def print_users():
    # UserNo. [ First Name: ___ | Password: ___ | Logged In: ___ ]
    
    print("List of Users:\n")
    
    for user in users.keys():
        name = get_user_info(user, NAME)
        name = name.title()
        
        password = get_user_info(user, PASSWORD)
        logged_in = get_user_info(user, LOGGED_IN)
        
        if logged_in:
            logged_in = "Logged In"
        else:
            logged_in = "Logged Out"
    
        user = user.title() # here bc lowercase only in users {}
        
        
        print(f"\t{user} [First Name: {name}| Password: {password} | {logged_in}]")
        
        
    print()



def create_account(user, name, password):
    name = name.title()
    
    
    users[user] = {
        NAME : name,
        PASSWORD : password,
        LOGGED_IN : False,
    }
    
    
    print(f"Account created successfully, {name}!\n")

    print_users()


def login(user, input_password):
    if not user in users.keys():
        print("Unrecognized user!\n")
        quit()
        
    current_password = get_user_info(user, PASSWORD)
    name = get_user_info(user, NAME)
    
    if not current_password == input_password:
        print(f"Password is incorrect, {name}!\n")
        return
    
    
    users[user][LOGGED_IN] = True
    
    
    print(f"Hello {name}!\n")


def logout(user):
    users[user][LOGGED_IN] = False
    
    
    name = get_user_info(user, NAME)
    
    print(f"Goodbye {name}!\n")


def change_password(user, old_password, new_password):
    if not user in users.keys():
        print("Unrecognized user!\n")
        return
    
    logged_in = get_user_info(user, LOGGED_IN)
    name = get_user_info(user, NAME)
    
    if not logged_in:
        print(f"Login first before changing passwords, {name}!\n")
        return
    
    current_password = get_user_info(user, PASSWORD)
    
    if not old_password == current_password:
        print(f"Password is incorrect, {name}!\n")
        return
    
    
    users[user][PASSWORD] = new_password


    print(f"Password changed successfully, {name}!\n")
    
    print_users()
    


main()
