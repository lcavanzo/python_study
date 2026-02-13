"""
Exercise 2: Working with a Log Entry File

You are given a JSON string representing a single log entry:
json

log_entry_string = '{"timestamp": "2025-10-26T15:00:00Z", "level": "INFO", "message": "User login successful", "user_id": 789, "session_id": "abc-123"}'

1.  Decode: Decode log_entry_string into a Python dictionary.
2.  Modify: Add a new key-value pair to the decoded dictionary: "ip_address": "192.168.1.100".
3.  Encode and Save: Encode the modified dictionary into a JSON string with an indentation of 4, and then save this formatted string to a new file named single_log.json. Use json.dump().
4.  Load and Verify: Load the content back from single_log.json into a Python dictionary and print its content to verify the changes.

"""

import json

filename = "single_log.json"
log_entry_string = '{"timestamp": "2025-10-26T15:00:00Z", "level": "INFO", "message": "User login successful", "user_id": 789, "session_id": "abc-123"}'

# decoded into a python object
log_entry_dic = json.loads(log_entry_string)

# adding new key
log_entry_dic["ip_address"] = "192.168.1.100"

# Encode and save
with open(filename, "w") as file:
    json.dump(log_entry_dic, indent=4, fp=file)

# Load and verify
with open(filename, "r") as file:
    new_json = file.read()

print(new_json)
