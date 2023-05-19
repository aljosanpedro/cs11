users = {}

FIRST_NAME = "FirstName"
PASSWORD = "Password"
LOGGED_IN = "LoggedIn"


def main():
    create_account("user1", "Harry", "IamHarryPotter")
    create_account("user2", "Hermione", "Granger")
    create_account("user3", "Ron", "weasleypass")
    
    print(users)
    
    change_password("user1", "IamHarryPotter", "HotPot")
    
    login("user1", "IamHarryPotter")
    login("user2", "Granger")
    login("user3", "weasleypass")
    
    change_password("user1", "IamHarryPotter", "HotPot")
    
    logout("user1")
    


def create_account(username, first_name, password):
    users[username] = {
        FIRST_NAME : first_name,
        PASSWORD : password,
        LOGGED_IN : False,
    }


def login(username, password):
    if username in users.keys():
        if users[username][PASSWORD] == password:
            users[username][LOGGED_IN] = True
            
            first_name = users[username][FIRST_NAME]
            print(f"Hello {first_name}!")
    else:
        quit()


def change_password(username, old_password, new_password):
    if not users[username][LOGGED_IN]:
        print("Login first before changing passwords!")
        return
    
    if username in users.keys():
        current_password = users[username][PASSWORD]
        
        if current_password == old_password:
            users[username][PASSWORD] = new_password
            
    print(users)


def logout(username):
    users[username][LOGGED_IN] = False
    
    first_name = users[username][FIRST_NAME]
    print(f"Goodbye {first_name}!")



main()
