# --- Demonstrating Reading Operations ---
data_file = "server_metrics.txt"
# Create a sample file for reading
with open(data_file, "w") as f:
    f.write("CPU_Usage: 45%\n")
    f.write("Memory_Usage: 60%\n")
    f.write("Disk_IOPS: 1200\n")
    f.write("Network_Traffic: 50MB/s\n")
    f.write("Active_Connections: 150\n")

print(f"--- Reading {data_file} ---")

# Using read() to get entire content
with open(data_file, "r") as f:
    full_content = f.read()
    print("\nContent with read():")
    print(full_content)

# Using readline() to get line by line
with open(data_file, "r") as f:
    print("\nContent with readline():")
    first_line = f.readline()
    second_line = f.readline()
    print(
        f"First line: {first_line.strip()}"
    )  # .strip() removes leading/trailing whitespace, including newline
    print(f"Second line: {second_line.strip()}")

# Using readlines() to get all lines as a list
with open(data_file, "r") as f:
    all_lines = f.readlines()
    print("\nContent with readlines():")
    for line in all_lines:
        print(line.strip())

# Iterating directly over the file object (most memory efficient for large files)
print("\nContent by iterating over file object:")
with open(data_file, "r") as f:
    for line in f:  # 'f' itself is an iterator
        print(line.strip())
