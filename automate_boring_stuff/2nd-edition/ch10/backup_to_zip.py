#! python3

"""
backup_to_zip.py - Copies an entire folder and its contents into
    a ZIP file whose filename increments.
"""

import os
import zipfile


def backup_to_zip(directory):
    """
    Backup the entire contents of "directory" into a ZIP file.
    """

    directory = os.path.abspath(directory)  # Make sure folder is absolute

    # Figure out the filename this code should use based on what
    #   files already exists.
    number = 1
    while True:
        zip_filename = os.path.basename(directory) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file.
    print(f"Creating {zip_filename} ... ")
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    # Walk the entire folder tree and compress the files in each directory
    for directory_name, sub_directory, filenames in os.walk(directory):
        print(f"Adding files in {directory_name}...")
        # Add the current folder to the ZIP file
        backup_zip.write(directory_name)

        # add all the files in this directory to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(directory) + "_"
            if filename.startswith(new_base) and filename.endswith(".zip"):
                continue  # don't back up the backup ZIP file
            backup_zip.write(os.path.join(directory_name, filename))
    backup_zip.close()
    print("Done.")


backup_to_zip("./boring_files/")
