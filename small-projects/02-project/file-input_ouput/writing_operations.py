# --- Demonstrating Writing Operations ---
output_file = "system_report.txt"

# Using write()
with open(output_file, "w") as f:
    f.write("--- System Health Report ---\n")
    f.write("Timestamp: 2023-10-27 10:30:00\n")
    f.write("Status: OK\n")
print(f"Initial content written to {output_file} using write().")

# Using writelines() - appending more data
additional_data = [
    "Load Average: 0.5, 0.3, 0.2\n",
    "Active Users: 5\n",
    "Disk Usage: /dev/sda1 70%\n",
]
with open(output_file, "a") as f:  # Open in append mode to add to existing content
    f.writelines(additional_data)
print(f"Additional content appended to {output_file} using writelines().")

# Verify content
print(f"\nFinal content of {output_file}:\n")
with open(output_file, "r") as f:
    print(f.read())
