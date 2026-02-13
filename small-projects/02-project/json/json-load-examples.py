import json

# Example 1: Decoding a simple JSON string
json_data_string = '{"product": "keyboard", "price": 75.99, "in_stock": true}'
python_dict = json.loads(json_data_string)

print(f"Decoded Python dictionary (Example 1): {python_dict}")
print(f"Type of decoded object: {type(python_dict)}")


# Example 2: Decoding a more complex JSON string with nested structures
complex_json_string = """
{
    "order_id": "ORD-456",
    "customer": {
        "first_name": "Bob",
        "last_name": "Johnson",
        "email": "bob@example.com"
    },
    "items": [
        {"item_name": "Mouse", "quantity": 1, "unit_price": 25.00},
        {"item_name": "Monitor", "quantity": 1, "unit_price": 250.00}
    ],
    "total_amount": 275.00
}
"""

complex_python_obj = json.loads(complex_json_string)
print("\nDecoded complex Python object (example 2):")
print(complex_json_string)
print(f"Customer email: {complex_python_obj['customer']['email']}")

# Example 3: Decoding a JSON list
json_list_string = (
    '[{"id": 101, "status": "active"}, {"id": 102, "status": "inactive"}]'
)
python_list_obj = json.loads(json_list_string)
print("\n Decoded a python list (Example 3):")
print(python_list_obj)
print(f"Status of first item: {python_list_obj[0]['status']}")


# Assuming 'sensor_data.json' was created by json.dump() earlier
file_name = "sensor_data.json"

try:
    with open(file_name, "r") as f:
        loaded_data = json.load(f)
    print(f"\nData loaded from {file_name}:")
    print(loaded_data)
    print(f"First reading temperature: {loaded_data['readings'][0]['temperature']}")
except FileNotFoundError:
    print(
        f"Error: File {file_name} not found. Please ensure it was created by the json.dump() example."
    )
