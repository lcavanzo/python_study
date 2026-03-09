import hashlib


class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email  # private by name mangling
        self.__password_hash = self._hash_password(password)  # private by name mangling

    def _hash_password(self, password):  # Protected (by convention) for internal use
        # In a real application, use stronger hashing like bcrypt
        return hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self.username

    def get_email(self):
        # we might want to return a masked email for security reasons
        parts = self.__email.split("@")
        return f"{parts[0][0]}*****@{parts[1]}"

    def verify_password(self, password):
        return self.__password_hash == self._hash_password(password)

    def update_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.__password_hash = self._hash_password(new_password)
            print("Password updated successfully")
            return True
        else:
            print("Old password incorrect")
            return False

    def update_email(self, new_email):
        # Add email validation logic here
        if "@" in new_email and "." in new_email:  # simple validation
            self.__email = new_email
            print("Email updated successfully")
            return True
        else:
            print("Invalid email format")
            return False


# Create user
user = UserProfile("developer_alpha", "alpha@example.com", "SecureP@ss1")

# Accessing public attribute
print(f"Username: {user.get_username()}")

# Accessing email and verifying password via public methods
print(f"Masked Email: {user.get_email()}")
print(f"Password 'SecureP@ass1' correct? {user.verify_password('SecureP@ss1')}")
print(f"Password 'wrongPass' correct? {user.verify_password('wrongPass')}")

# Attempting to directly access private attributes  (will fail)
try:
    print(user.__email)
except AttributeError as e:
    print(f"Error accessing private email: {e}")

# Updating password
user.update_email("alpha.new@example.com")
print(f"Masked Email after update: {user.get_email()}")
