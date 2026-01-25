"""
Build a small system to manage employee data.

1.  Define Schema: Create a JSON Schema for an employee record. Each employee should have:
        id: integer, required, minimum 1.
        firstName: string, required, minLength 2.
        lastName: string, required, minLength 2.
        email: string, required, format "email".
        department: string, required, must be one of "HR", "Engineering", "Marketing", "Sales".
        startDate: string, required, format "date".
        isActive: boolean, required.

2.  Create Data: Create a list of 3-4 employee dictionaries. Ensure at least one entry is intentionally invalid (e.g., missing a required field, invalid email format, wrong department).

3.  Validate and Report: Iterate through your list of employee dictionaries. For each employee, attempt to validate it against your schema. Print whether each employee record is valid or invalid, and if invalid, print the validation error message.

"""

import json
from jsonschema import ValidationError, Draft7Validator

employee_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Employee Profile",
    "description": "Schema for validating an employee profile object",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "description": "Unique identifier for an employee",
            "minimum": 1,
        },
        "fistName": {
            "type": "string",
            "description": "Employe's first name",
            "minLenght": 2,
        },
        "lastName": {
            "type": "string",
            "description": "Employee's last name",
            "minLenght": 2,
        },
        "email": {
            "type": "string",
            "description": "Employee's email",
            "format": "email",
        },
        "department": {
            "type": "string",
            "description": "Employee's department",
            "enum": ["HR", "Engineering", "Marketing", "Sales"],
        },
        "startDate": {
            "type": "string",
            "description": "Timestamp of the employee's start date.",
            "format": "date-time",
        },
        "isActive": {
            "type": "boolean",
            "description": "Employee status",
        },
    },
    "required": [
        "id",
        "fistName",
        "lastName",
        "department",
        "startDate",
        "isActive",
    ],
}

employees = {
    "emp1": {
        "id": 123,
        "fistName": "Luis",
        "lastName": "Cavanzo",
        "email": "emp1@example.com",
        "department": "Engineering",
        "startDate": "2025-10-26T14:30:00Z",
        "isActive": True,
    },
    "emp2": {
        "id": 456,
        "fistName": "Diana",
        # "lastName": "Caceres", # Missing last name
        "email": "emp2@example.com",
        "department": "Sales",
        "startDate": "2025-11-26T14:30:00Z",
        "isActive": False,
    },
    "emp3": {
        "id": 890,
        "fistName": "Toji",
        "lastName": "Zannin",
        "email": "emp3example.com",  # wrong email
        "department": "outside",
        # "startDate": "2025-10-26T14:30:00Z",  # no startDate
        "isActive": False,
    },
    "emp4": {
        "id": "aaa",
        "fistName": 1243,
        "lastName": 345,
        # "email": "emp1@example.com",
        # "department": "Engineering",
        "startDate": "26T14:30:00Z",  # wront date
        "isActive": "True",  # string instead of boolean
    },
}


def validate_employees_data(employee_info):
    """
    Validates an incoming employee information against the schema

    Returns:
        True if valid, print errors and returns False otherwise
    """
    try:
        validator = Draft7Validator(schema=employee_schema)
        errors = sorted(validator.iter_errors(employee_info), key=str)
        if errors:
            for error in errors:
                print(f"- Error {error.message}")
            return False
        else:
            return True
    except ValidationError as e:
        print(e.message)
        return False


for employee in employees.values():
    print("--- Validating Employee Information ---")
    if validate_employees_data(employee):
        print(f"Validation Successful for employee: {employee['id']}\n")
    else:
        print(f"Validation Failed for employee: {employee['id']}\n")
