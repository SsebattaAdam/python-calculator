class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def display_profile(self):
        print("Username: " + self.username)
        print("Age: " + str(self.age))


class Authentication:
    def login(self, username, password):
        # Implementation of login functionality
        pass

    def logout(self):
        # Implementation of logout functionality
        pass


class Admin(User, Authentication):
    def __init__(self, username, age):
        User.__init__(self, username, age)
        Authentication.__init__(self)

    def manage_users(self):
        print("Admin has the ability to manage users")


# Create an instance of Admin representing a system administrator
admin = Admin("admin1", 30)

# Access and display the admin's profile
admin.display_profile()

# Perform admin-specific actions
admin.login("admin1", "password")
admin.manage_users()
admin.logout()
