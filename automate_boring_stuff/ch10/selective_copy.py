#! python3

'''
selective_copy.py - Write a program that walks through a folder tree
    and searches for files with a certain file extension (such as .pdf or .jpg).
    Copy these files from whatever location they are in to a new folder.
'''

import os
import shutil
import sys

if len(sys.argv) != 4:
    print("Usage: python selective_copy.py <ext> <location to search> <location for new files> ")
    sys.exit(1)

EXTENSION_SEPARATOR = '.'


def copy_files(source, target) -> None:
    """
    Copy a file from source to target directory.
    """
    if not os.path.exists(target):
        print("creating new dir")
        create_directory(target)
    shutil.copy(source, target)


def search_files(ext, dir_source, dir_target) -> None:
    """
    Searching for files with specific extension
    """
    dir = os.path.abspath(dir_source)
    print(f"Looking for .{ext} files in {dir}...")
    for dir_name, sub_dir, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(f"{EXTENSION_SEPARATOR}{ext}"):
                print(filename)
                dir_source = os.path.join(dir_name, filename)
                copy_files(dir_source, dir_target)


def create_directory(path) -> None:
    """
    Creates new directory if the target dir doesn't exists
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully")
    except OSError as error:
        print(f"Error creating directory '{path}': {error}")


extension = sys.argv[1]
source = sys.argv[2]
target = sys.argv[3]

search_files(extension, source, target)
