#! python3

"""
filling_gaps.py - Write a program that finds all files with a given prefix,
    such as spam001.txt, spam002.txt, and so on, in a single folder and locates
    any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
    but no spam002.txt). Have the program rename all the later files to close this gap.

    As an added challenge, write another program that can insert gaps into numbered
    files so that a new file can be added.
"""
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python filling_gaps.py <directory>")
    sys.exit(1)


def search_files(directory) -> None:
    """
    Searching for files within a directory
    """
    dir = os.path.abspath(directory)
    print(f"Renaming files in {dir}...")
    # for dir_name, sub_dir, filenames in os.walk(dir):
    #     for filename in filenames:


directory = sys.argv[1]
search_files(directory)

# """ run this before execute the file
# for i in {001..005}; do                                                                                                                                                                                                                                ─╯
# touch spam$i.txt
# done
# rm spam003
# """
