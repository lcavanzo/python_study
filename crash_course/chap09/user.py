"""A class that represent a user"""

class User:
    """A simple attempt to represent a user"""
    def __init__(self, first_name, last_name, username, gender):
        self.first_name = first_name
        self.last_name  = last_name 
        self.full_name  = f"{first_name} {last_name}"
        self.username   = username
        self.gender     = gender
        self.login_attempts = 0
        

    def describe_user(self):
        """Returns all info about a user"""
        print("#########################################")
        print(f"USER INFO")
        print(f"\tusername: {self.username}")
        print(f"\tfull name: {self.full_name.title()}")
        print(f"\tgender: {self.gender}")
        print(f"\tlogin attempts: {self.login_attempts}")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello {self.full_name.title()}\n")

    def increment_login_attempts(self):
        """Increment the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the logins attempts to 0"""
        self.login_attempts = 0
