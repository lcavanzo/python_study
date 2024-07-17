#! python3

'''
rename_dates.py - Renames filenames with American MM-DD-YYYY date
    to European DD-MM-YYYY
'''

import os
import re
import shutil

# Create a regex that matches files with American date format
'''
 reading the regex from the beginning, and count up each time you encounter
    an opening parenthesis.

date_pattern= re.compile(r"""^(1) # all text before the date
    (2 (3) )-                     # one or two digits for the month
    (4 (5) )-                     # one or two digits for the day
    (6 (7) )                      # four digits for the year
    (8)$                          # all text after the date
    """, re.VERBOSE)
'''
date_pattern = re.compile(r"""^(.*?)   # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

# Loop over the files in the working directory
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename
    euro_filename = (
        before_part
        + day_part
        + '-'
        + month_part
        + '-'
        + year_part
        + after_part)

    # Get the full, absolute file paths.
    abs_working_dir  = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    # shutil.move(amer_filename, euro_filename) # uncomment this line to get the job done

'''bash
# command to create 10 random files with the American date style

for i in {1..10}; do
  random_string=$(LC_ALL=C tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 10 | head -n 1)
  date_string=$(date +"%m-%d-%Y")
  touch "${random_string}_${date_string}.txt"
done

'''
