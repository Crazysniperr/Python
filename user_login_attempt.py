class User:
    #to create a class called user for user data entry
    def __init__(self,first_name,last_name,User_name,Email_ID):#all essential data about user
        self.first = first_name
        self.last = last_name
        self.uname = User_name
        self.mail = Email_ID
        self.login_attempts = 0

    def describe_user(self): #to describe the user
        print(f"{self.first} {self.last} has a {self.uname} username and his Mail Id is {self.mail}")

    def greet_user(self):#to greet the user with there username
        print(f"Hello {self.uname} ,\n Have a Good day")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Total Login attempts of {self.uname} are {self.login_attempts}")

    def loggin_attempts(self):
        print(f'Total login attempts of {self.uname} is {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts of {self.uname} has been reset to {self.login_attempts}')
class Privileges():
    def __init__(self,privileges = ['Can add Post','Can delete Post','Can ban User']):
        self.admin_privileges = privileges

    def show_privileges(self):
            print('Admin has the following Privileges')
            for privilegs in self.admin_privileges:
                print(privilegs)

class Admin(User):
    def __init__(self,first_name,last_name,User_name,Email_ID):
        super().__init__(first_name,last_name,User_name,Email_ID)
        self.privileges = Privileges()



Admin_User=Admin('Siddhant','Dixit','Crazysniperr','sid@gmail.com')
User1=User('Nilesh','Agarwal','DeathKill','nilesh@gmail.com')
User2=User('Anubhav','Awasthi','Raceranu','anu@gmail.com')


Admin_User.privileges.show_privileges()
