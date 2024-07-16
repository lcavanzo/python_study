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
import re
import sys

if len(sys.argv) != 3:
    print("Usage: python filling_gaps.py <directory> <extension>")
    sys.exit(1)


def search_files(dir, ext) -> None:
    """
    Searching for files within a directory
    """
    dir = os.path.abspath(dir)
    print(f"Renaming files in {dir}...")
    numbers_ordered = []
    for  root_dir, sub_dir, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(ext):
                basename, number, extension = extract_number(filename)
                # print(basename, number, extension)
                numbers_ordered.append(number)
                numbers_ordered.sort()
    create_missing_file(dir, basename, numbers_ordered, extension)

def create_missing_file(dir, basename, numbers_list, extension):
    """
    pass
    """
    print(f"{basename} {numbers_list} {extension}")
    old_list = numbers_list.copy()
    # print(f"ori list {old_list}")
    for number in range(len(numbers_list)):
        if numbers_list[number] < 10:
            path =f"{dir}/{basename}00"
            if not os.path.exists(f"{path}{number+1}{extension}"):
                os.rename(f"{path}{old_list[number]}{extension}", f"{path}{number+1}{extension}")
                # print(f"moving {path}{old_list[number]}{extension} to >> file: {path}{number+1}{extension}")
            # else:
            #     print(f"file: {path}{number+1}{extension}")
        elif numbers_list[number] < 100:
            path =f"{dir}/{basename}0"
            if not os.path.exists(f"{path}{number+1}{extension}"):
                os.rename(f"{path}{old_list[number]}{extension}", f"{path}0{number+1}{extension}")



def extract_number(filename):
    """
    pass
    """
    pattern = r'([a-zA-Z]+)(\d+)(\.[a-z]+)'
    match = re.search(pattern, filename)
    if match:
        return match.group(1), int(match.group(2)), match.group(3) # Convert the captured digits to an integer
    return None  # Return None if no match is found


directory = sys.argv[1]
prefix = sys.argv[2]
search_files(directory, prefix)

# """ run this before execute the file
# for i in {001..005}; do                                                                                                                                                                                                                                ─╯
# touch spam$i.txt
# done
# rm spam003
# """
