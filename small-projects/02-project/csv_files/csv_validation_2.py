import csv

# Define expected headers and validation rules
EXPECTED_HEADERS = ["ID", "Name", "Age", "Email", "Status"]
VALIDATION_RULES = {
    "ID": {"required": True, "type": int, "unique": True, "min": 1},
    "Name": {"required": True, "regex": r"^[A-Za-z\s\-\']+$"},
    "Age": {"required": True, "type": int, "min": 18, "max": 120},
    "Email": {
        "required": True,
        "regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    },
    "Status": {"required": False, "choices": ["Active", "Inactive", "Pending"]},
}

valid_data = [
    ["ID", "Name", "Age", "Email", "Status"],
    ["1", "Valid User One", "25", "user1@valid.com", "Active"],
    ["2", "Valid User Two", "35", "user2@valid.com", "Inactive"],
]

with open("valid_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(valid_data)
