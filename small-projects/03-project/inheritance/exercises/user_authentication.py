"""
User Authentication System (Inheritance for Role-Based Access)

Objective: Model different user roles in an application with varying permissions.

    Create a base class User:
        Initialize with username and email.
        Define a method login() that prints "User [username] logged in."
        Define a method has_permission(action) that always returns False (base permission).

    Create a subclass AdminUser:
        Inherit from User.
        Override has_permission(action) to return True for any action (admins have all permissions).

    Create a subclass EditorUser:
        Inherit from User.
        Override has_permission(action) to return True only if action is "edit_content" or "view_content". Otherwise, return False.

    Polymorphism Testing:
        Using unittest, create TestUserPermissions.
        Test the login() method for each user type.
        Test User.has_permission() for various actions, ensuring it always returns False.
        Test AdminUser.has_permission() for different actions (e.g., "delete_user", "create_post"), ensuring it always returns True.
        Test EditorUser.has_permission() for "edit_content", "view_content", and an invalid action like "delete_user", asserting the correct boolean outcome.
        Create a list of mixed user types (User, AdminUser, EditorUser). Iterate through the list, call has_permission("edit_content") and has_permission("delete_user") on each, and assert that the correct permission status is returned for each specific user role.

"""

import unittest


class User:
    """
    Base Class to define users
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    def login(self):
        """
        method to represent the login of a user
        """
        return f"User {self.username} logged in."

    def has_permission(self, action) -> bool:
        """
        method to represent the permissions of a user
        """
        return False


class AdminUser(User):
    """
    Child class that represents an AdminUser
    """

    def __init__(self, username, email):
        super().__init__(username, email)

    def __repr__(self):
        return f"AdminUser(username='{self.username}', email='{self.email}')"

    def has_permission(self, action):
        return True


class EditorUser(User):
    """
    Child class tha represents an EditorUser
    """

    def __init__(self, username, email):
        super().__init__(username, email)

    def __repr__(self):
        return f"EditorUser(username='{self.username}', email='{self.email}')"

    def has_permission(self, action):
        if action == "edit_content" or action == "view_content":
            return True
        return False


class TestUserPermissions(unittest.TestCase):
    """
    Class to test the Base/Child classes
    """

    def test_user_login_ok(self):
        """
        test user_login() works in each class
        """
        users = [
            User("lcavanzo", "lcavanzo@linux.com"),
            AdminUser("luis", "luis@linux.com"),
            EditorUser("tyrone", "tyrone@linux.com"),
        ]

        expected_outputs = [
            "User lcavanzo logged in.",
            "User luis logged in.",
            "User tyrone logged in.",
        ]
        for user, expected_output in zip(users, expected_outputs):
            self.assertEqual(user.login(), expected_output)

    def test_user_has_permissions(self):
        """
        test User class has_permission() works
        """
        user01 = User("lcavanzo", "lcavanzo@linux.com")
        actions = ["delete", "update", "create", "refresh"]

        for action in actions:
            self.assertFalse(user01.has_permission(action))

    def test_admin_user_has_permissions(self):
        """
        test AdminUser class has_permission() works
        """
        admin01 = AdminUser("lcavanzo", "lcavanzo@linux.com")
        actions = ["delete_user", "create_post", "update_passwords", "refresh_db"]

        for action in actions:
            self.assertTrue(admin01.has_permission(action))

    def test_editor_user_has_permissions(self):
        """
        test AdminUser class has_permission() works
        """
        editor01 = EditorUser("lcavanzo", "lcavanzo@linux.com")
        actions = [
            "delete_user",
            "create_post",
            "update_passwords",
            "refresh_db",
            "view_content",
            "edit_content",
        ]

        for action in actions:
            if action == "view_content" or action == "edit_content":
                self.assertTrue(editor01.has_permission(action))
            else:
                self.assertFalse(editor01.has_permission(action))

    def test_all_users_has_permissions(self):
        """
        test User AdminUser and EditorUser classes has_permission() works
        """
        users = [
            User("lcavanzo", "lcavanzo@linux.com"),
            AdminUser("luis", "luis@linux.com"),
            EditorUser("tyrone", "tyrone@linux.com"),
        ]
        actions = [
            "delete_user",
            "edit_content",
        ]

        for user, action in zip(users, actions):
            if action == "view_content" or action == "edit_content":
                self.assertTrue(user.has_permission(action))
            else:
                self.assertFalse(user.has_permission(action))


if __name__ == "__main__":
    unittest.main()
