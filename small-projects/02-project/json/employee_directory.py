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

from jsonschema import Draft7Validator

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
        "firstName": {
            "type": "string",
            "description": "Employe's first name",
            "minLength": 2,
        },
        "lastName": {
            "type": "string",
            "description": "Employee's last name",
            "minLength": 2,
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
        "firstName",
        "lastName",
        "email",
        "department",
        "startDate",
        "isActive",
    ],
}

employees = {
    "emp1": {
        "id": 123,
        "firstName": "Luis",
        "lastName": "Cavanzo",
        "email": "emp1@example.com",
        "department": "Engineering",
        "startDate": "2025-10-26T14:30:00Z",
        "isActive": True,
    },
    "emp2": {
        "id": 456,
        "firstName": "Diana",
        # "lastName": "Caceres", # Missing last name
        "email": "emp2@example.com",
        "department": "Sales",
        "startDate": "2025-11-26T14:30:00Z",
        "isActive": False,
    },
    "emp3": {
        "id": 890,
        "firstName": "Toji",
        "lastName": "Zannin",
        "email": "emp3example.com",  # wrong email
        "department": "outside",
        # "startDate": "2025-10-26T14:30:00Z",  # no startDate
        "isActive": False,
    },
    "emp4": {
        "id": "aaa",
        "firstName": 1243,
        "lastName": 345,
        # "email": "emp1@example.com",
        # "department": "Engineering",
        "startDate": "26T14:30:00Z",  # wront date
        "isActive": "True",  # string instead of boolean
    },
}


VALIDATOR = Draft7Validator(
    schema=employee_schema, format_checker=Draft7Validator.FORMAT_CHECKER
)


def validate_employees_data(employee_info, validator):
    """
    Validates an incoming employee information against the schema.

    Returns:
        list: A list of error strings. Returns empty list [] if valid.
    """
    found_errors = []
    try:
        errors = sorted(validator.iter_errors(employee_info), key=str)
        if errors:
            for error in errors:
                message = f"Error in field {list(error.path)}: {error.message}"
                found_errors.append(message)
    except Exception as e:
        found_errors.append(f"Critical Error: {str(e)}")
    return found_errors


for employee in employees.values():
    print(f"--- Processing Employee {employee['id']} ---")

    validation_results = validate_employees_data(employee, VALIDATOR)

    # Check the size of the list to decide Success vs Failure
    if len(validation_results) == 0:
        print("Status: Valid")
    else:
        print("Status: Invalid")
        print("Details:")
        for msg in validation_results:
            print(f" - {msg}")
    print("\n")  # formatting line break
