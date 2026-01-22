import json
from jsonschema import validate, ValidationError

# Our defined JSON Schema (as a python dictionary)
user_profile_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "User Profile",
    "description": "Schema for validating a user profile object.",
    "type": "object",
    "properties": {
        "userId": {
            "type": "integer",
            "description": "Unique identifier for the user.",
            "minimum": 1,
        },
        "username": {
            "type": "string",
            "description": "User's unique username.",
            "minLength": 3,
            "maxLenght": 20,
        },
        "email": {
            "type": "string",
            "format": "email",
            "description": "User's email address.",
        },
        "isActive": {
            "type": "boolean",
            "description": "Indicates if the user account is active.",
        },
        "roles": {
            "type": "array",
            "description": "List of roles assigned to the user.",
            "items": {"type": "string", "enum": ["admin", "editor", "user", "guest"]},
            "minItems": 1,
            "uniqueItems": True,
        },
        "lastLogin": {
            "type": ["string", "null"],
            "format": "date-time",
            "description": "Timestamp of the user's last login",
        },
    },
    "required": ["userId", "username", "email", "isActive", "roles"],
}

# --- Valid Data Example ---
valid_user_data = {
    "userId": 123,
    "username": "johndoe",
    "email": "john.doe@example.com",
    "isActive": True,
    "roles": ["user", "guest"],
    "lastLogin": "2025-10-26T14:30:00Z",
}

try:
    validate(instance=valid_user_data, schema=user_profile_schema)
    print("\nValid User Data: Validation succesful!")
except ValidationError as e:
    print(f"\nValid User Data: validation failed {e.message}")


# --- Invalid Data Example 1: Missing required filed ---
invalid_user_data_missing_field = {
    "userId": 456,
    "username": "janadoe",
    "email": "jana.doe@example.com",
    "isActive": True,
    # "roles" is missing
}

try:
    validate(instance=invalid_user_data_missing_field, schema=user_profile_schema)
    print("\ninvalid User Data (Missing Field: Validation succesful!")
except ValidationError as e:
    print(f"\nInvalid Data (Missing Field): Validation failed {e.message}")


# --- Invalid Data Example 2: Incorrect data type and value constraint ---
invalid_user_data_type_value = {
    "userId": 0,  # should be minimum 0
    "username": "ja",  # Too short
    "email": "invalid-email",  # Incorrect format
    "isActive": "yes",  # must be boolean
    "roles": ["super-saiya-jin"],  # Not in enum
    "lastLogin": "not-a-date",  # Incorrect format
}

try:
    validate(instance=invalid_user_data_type_value, schema=user_profile_schema)
    print("\nInvalid Data (Type/Value): Validation succesful")
except ValidationError as e:
    print(
        f"\nInvalid Data (Type/Value): Validation failed with multiple issues. First one: {e.message}"
    )
    # This will typically show the first validation error encountered.
    # To see all errors, you might need to iterate through them.
