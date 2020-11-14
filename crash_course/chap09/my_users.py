from user import User
from admin import Admin

user1 = User('luis', 'cavanzo', 'lcavanzo', 'male')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()

admin1 = Admin('cloud', 'strife', 'cloudF', 'male')
admin1.describe_user()
admin1.privileges.show_privileges()
