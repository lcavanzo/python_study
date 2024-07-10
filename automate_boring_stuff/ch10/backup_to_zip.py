#! python3

'''
backup_to_zip.py - Copies an entire folder and its contents into
    a ZIP file whose filename increments.
'''

import os
import zipfile


def backup_to_zip(directory):
    '''
    Backup the entire contents of "directory" into a ZIP file.
    '''

    directory = os.path.abspath(directory) # Make sure folder is absolute

    # Figure out the filename this code should use based on what
    #   files already exists.
    number = 1
    while True:
        zip_filename = (
                os.path.basename(directory)
                + '_'
                + str(number)
                + '.zip'
        )
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file.

    # Walk the entire folder tree and compress the files in each directory
    print('Done.')

backup_to_zip('./boring_files/')
