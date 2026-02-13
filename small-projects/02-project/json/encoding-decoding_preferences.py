"""
Exercise 1: Encoding and Decoding User Preferences

Assume you have a Python dictionary representing a user's preferences for a web application.
python

user_preferences = {
    "userId": "user_xyz123",
    "theme": "dark",
    "notifications": {
        "email": True,
        "push": False,
        "sms": False
    },
    "language": "en-US",
    "favorite_categories": ["Technology", "Science", "History"]
}

1.   Encode: Convert the user_preferences dictionary into a compact JSON string. Print the resulting string.

2.   Encode with Indentation: Convert the user_preferences dictionary into a JSON string with an indentation level of 2, Print the formatted string.

3.   Decode: Take the compact JSON string from step 1 and decode it back into a Python dictionary. Verify that the decoded dictionary is identical to the original user_preferences.
"""

import json

user_preferences = {
    "userId": "user_xyz123",
    "theme": "dark",
    "notifications": {
        "email": True,
        "push": False,
        "sms": False,
    },
    "language": "en-US",
    "favorite_categories": ["Technology", "Science", "History"],
}

print("--- Encoded into compact json ---")
user_preferences_encoded = json.dumps(user_preferences)
print(user_preferences_encoded)

print("\n--- Encoded with indentation of 2 ---")
user_preferences_encoded_pretty = json.dumps(user_preferences, indent=2)
print(user_preferences_encoded_pretty)


print("\n--- Decode ---")
user_preferences_dic = json.loads(user_preferences_encoded)
print(f"{user_preferences_dic}, type={type(user_preferences_dic)}")


print("\n--- Comparing files ---")
if user_preferences == user_preferences_dic:
    print("Files are equal")
else:
    print("Files are not equal")
