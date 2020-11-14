"""A set of classes that represent an admin user and his privileges"""

from user import User

class Privileges:
    """Represent the privileges of an user"""

    def __init__(self):
        """Initialize the privileges attributes"""
        self.privileges = ['can add post', 'can delete a post', 
            'can ban users', 'can edit post']

    def show_privileges(self):
        """return the active privileges of an administrator"""
        print(f"\tThe privileges of an administrator are:")
        for privilege in self.privileges:
            print(f"\t\t{privilege}")


class Admin(User):
    """A simple attempt to representa Administrator"""

    def __init__(self, first_name, last_name, username, gender):
        """Initialize attributes specific for an administrator"""
        super().__init__(first_name, last_name, username, gender)
        self.privileges = Privileges()
