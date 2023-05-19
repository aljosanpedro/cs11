users = {}

FIRST_NAME = "FirstName"
PASSWORD = "Password"
IS_LOGGED_IN = "LoggedIn"


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
    


def get_info(username, info):
    return users[username][info]


def print_users():
    # UserNo. [ First Name: ___ | Password: ___ | Logged In: ___ ]
    
    print("List of Users:\n")
    
    for username in users.keys():
        first_name = get_info(username, FIRST_NAME).title()
        password = get_info(username, PASSWORD)
        is_logged_in = get_info(username, IS_LOGGED_IN)
    
        username = username.title()
        
        print(f"\t{username} [First Name: {first_name} | Password: {password} | Logged In: {is_logged_in}]")
        
    print()


def create_account(username, first_name, password):
    users[username] = {
        FIRST_NAME : first_name,
        PASSWORD : password,
        IS_LOGGED_IN : False,
    }
    
    first_name = first_name.title()
    print(f"Account created successfully, {first_name}!\n")
    
    print_users()


def login(username, input_password):
    if not username in users.keys():
        quit()
        
    current_password = get_info(username, PASSWORD)
    first_name = get_info(username, FIRST_NAME)
    
    if not current_password == input_password:
        print(f"Password is incorrect, {first_name}!\n")
        return
    
    
    users[username][IS_LOGGED_IN] = True
    
    print(f"Hello {first_name}!\n")


def change_password(username, old_password, new_password):
    if not username in users.keys():
        print("Unrecognized username!\n")
        return
    
    is_logged_in = get_info(username, IS_LOGGED_IN)
    first_name = get_info(username, FIRST_NAME)
    
    if not is_logged_in:
        print(f"Login first before changing passwords, {first_name}!\n")
        return
    
    current_password = get_info(username, PASSWORD)
    
    if not current_password == old_password:
        print(f"Password is incorrect, {first_name}!\n")
        return
    
    
    users[username][PASSWORD] = new_password
        
    print(f"Password changed successfully, {first_name}!\n")
    print_users()
    

def logout(username):
    users[username][IS_LOGGED_IN] = False
    
    first_name = get_info(username, FIRST_NAME)
    print(f"Goodbye {first_name}!\n")



main()
