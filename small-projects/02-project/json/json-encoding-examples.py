import json

# Example 1: Encoding a simple dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "courses": ["History", "Math"],
}

json_string = json.dumps(data)
print(f"Encoded JSON string (Example 1):\n{json_string}")

# Example 2:P Encoding with indentation for readability
data_with_nested_list = {
    "product_id": "ABC-123",
    "item_name": "Laptop",
    "details": {
        "brand": "TechCo",
        "model": "XPS 15",
        "spec": ["8GB RAM", "256GB SSD", "Intel i7"],
    },
    "price": 1200.50,
    "available": True,
}

json_pretty_string = json.dumps(data_with_nested_list, indent=4)
print("\nEncoded JSON string with indentation (Example 2)")
print(json_pretty_string)


# Example 3: Encoding a list of dictionaries
users = [
    {"id": 1, "username": "user1", "active": True},
    {"id": 2, "username": "user2", "active": False},
]

json_users_string = json.dumps(users, indent=2)
print("\nEncoded JSON string with list of users (Example 3)")
print(json_users_string)

# Example 4: creating a json file

data_to_save = {
    "sensor_id": "S-001",
    "location": "Warehouse A",
    "readings": [
        {"timestamp": "2025-01-01T10:00:00Z", "temperature": 20.5},
        {"timestamp": "2025-01-01T10:05:00Z", "temperature": 21.1},
    ],
}

file_name = "sensor_data.json"
with open(file_name, "w") as f:
    json.dump(data_to_save, f, indent=4)


print(f"\nData saved to file {file_name}")
