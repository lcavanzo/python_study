"""
You have a list of Ticket IDs. Some people printed their tickets twice! Your job is to find the duplicates and report every seat number (index) where that ticket appears.

Expected Output:

Duplicate 'A-100' found at indexes: 0, 2, 4
Duplicate 'B-200' found at indexes: 1, 5
"""

tickets = ["A-100", "B-200", "A-100", "C-300", "A-100", "B-200"]


seen = set()
duplicates = set()
message = []

for index, ticket in enumerate(tickets):
    if ticket in seen and ticket not in duplicates:
        duplicate_row = []
        for d_ticket in range(len(tickets)):
            if ticket == tickets[d_ticket]:
                duplicate_row.append(d_ticket)
                duplicates.add(ticket)
        message.append(f"Duplicate '{ticket}' found at indexes: {duplicate_row}")
    seen.add(ticket)

for mess in message:
    print(f"{mess}")
