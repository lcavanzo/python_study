"""
Exercise 3: Validating Configuration Data

You are managing application configuration, and it must adhere to a specific schema.

Configuration Schema:
```json
config_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Application Configuration",
    "description": "Schema for application runtime configuration.",
    "type": "object",
    "properties": {
        "database_url": {
            "type": "string",
            "format": "uri",
            "description": "URL for the database connection."
        },
        "port": {
            "type": "integer",
            "description": "Port number for the application service.",
            "minimum": 1024,
            "maximum": 65535
        },
        "debug_mode": {
            "type": "boolean",
            "description": "Flag to enable/disable debug mode."
        },
        "log_level": {
            "type": "string",
            "enum": ["INFO", "WARNING", "ERROR", "DEBUG"],
            "description": "Logging verbosity level."
        }
    },
    "required": ["database_url", "port", "debug_mode"]
}
```

Test Data 1 (Valid):
```python
valid_config = {
    "database_url": "postgresql://user:pass@host:5432/db",
    "port": 8080,
    "debug_mode": True,
    "log_level": "DEBUG"
}
```

Test Data 2 (Invalid):
```python

invalid_config = {
    "database_url": "invalid-url", # Not a valid URI format
    "port": 900, # Below minimum
    "debug_mode": "maybe", # Not a boolean
    "log_level": "CRITICAL" # Not in enum
    # 'database_url' and 'debug_mode' also have issues, but 'port' is the most obvious here.
}
```

Instructions:
    Import validate and ValidationError from jsonschema.
    For valid_config, use validate() to check it against config_schema. Print a success message if valid.
    For invalid_config, use validate() and wrap it in a try-except ValidationError block. Print the error message from the exception if validation fails.

"""

from jsonschema import validate, ValidationError

config_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Application Configuration",
    "description": "Schema for application runtime configuration.",
    "type": "object",
    "properties": {
        "database_url": {
            "type": "string",
            "format": "uri",
            "description": "URL for the database connection.",
        },
        "port": {
            "type": "integer",
            "description": "Port number for the application service.",
            "minimum": 1024,
            "maximum": 65535,
        },
        "debug_mode": {
            "type": "boolean",
            "description": "Flag to enable/disable debug mode.",
        },
        "log_level": {
            "type": "string",
            "enum": ["INFO", "WARNING", "ERROR", "DEBUG"],
            "description": "Logging verbosity level.",
        },
    },
    "required": ["database_url", "port", "debug_mode"],
}

valid_config = {
    "database_url": "postgresql://user:pass@host:5432/db",
    "port": 8080,
    "debug_mode": True,
    "log_level": "DEBUG",
}


invalid_config = {
    "database_url": "invalid-url",  # Not a valid URI format
    "port": 900,  # Below minimum
    "debug_mode": "maybe",  # Not a boolean
    "log_level": "CRITICAL",  # Not in enum
    # 'database_url' and 'debug_mode' also have issues, but 'port' is the most obvious here.
}


def validate_config(config):
    """
    Validate the configuration
    """
    try:
        validate(instance=config, schema=config_schema)
        return True
    except ValidationError as e:
        print(f"- Error: {e.message}")
        return False


configs = [valid_config, invalid_config]
for config in configs:
    print("\n---Validating File---")
    if validate_config(config):
        print("\nValid User Data: Validation succesful!")
    else:
        print("\nInvalid User Data: Validation failed!")
