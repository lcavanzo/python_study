#! python3

"""
Write a program that walks through a folder tree and searches
    for exceptionally large files or folders—say, ones that have a
    file size of more than 10MB.
    Print these files with their absolute path to the screen.
"""

import os
import sys

if len(sys.argv) != 2:
    print("Usage: python deleting_files.py <directory>")
    sys.exit(1)

def delete_files(source, size_bytes) -> None:
    """
    Delete files larger than 100M
    """
    size_mb = size_bytes/ (1024 * 1024)
    print(f"file deleted -> filename: {source}, Size: {size_mb}M")
    # os.remove(source) ## for deleting the files

def search_files(source) -> None:
    """
    search for files larger than 100M
    """
    dir = os.path.abspath(source)
    print(f"Looking for files in {dir} > {FILE_SIZE}M...")
    for dir_name, sub_dir, filenames in os.walk(dir):
        for filename in filenames:
            file_size = get_file_size(os.path.join(dir_name, filename))
            if int( file_size ) >= FILE_SIZE_BYTES:
                print("Files to delete:")
                delete_files(f"{dir_name}/{filename}", file_size)

def get_file_size(file_path):
    """
    pass
    """
    if os.path.exists(file_path) :
        return os.path.getsize(file_path)
    else:
        return "File not found"



# 100MB to bytes
FILE_SIZE = 100
FILE_SIZE_BYTES= FILE_SIZE* 1024 * 1024
directory = sys.argv[1]
search_files(directory)
