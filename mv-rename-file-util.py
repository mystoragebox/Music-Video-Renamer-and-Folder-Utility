# Rename files and move them into new folders. You can change the base
# variable and the delimiter variable. If you don't need to confirm
# every rename you can use the # to comment out print on line 26
# and replace input('Continue y, n: ') with 'y' on line 27

import os
import fnmatch
from pathlib import Path

base = '' # relative to this file, if this file in same folder leave blank
f_dictionary = {} # initialise dictionary
delimiter = ' - ' # what you want to find and split the filename with
fndelimiter = '*' + delimiter + '*'

# loop through everything in the directory.
for entry in os.listdir(base):
    
    # check if the entry is a file
    if os.path.isfile(os.path.join(base, entry)):
        
        # check if entry has the delimiter or not
        if fnmatch.fnmatchcase(entry, fndelimiter):
            splt = entry.split(delimiter)

            # continue or not
            print('This Ok? Artist: ' + splt[0] + ' Song: ' + splt[1])
            contin = input('Continue y, n: ')

            if contin == 'y':

                # check if artist path exists
                artistPath = base + splt[0] + '/'
                Path(artistPath).mkdir(parents=True, exist_ok=True)

                # rename file
                oldname = base + entry
                newname = base + splt[1]
                os.rename(oldname, newname)

                # Move file
                os.rename(newname, artistPath + splt[1])

                # update dictionary
                f_dictionary[entry] = artistPath + splt[1]

print('Completed files\n')
for key, value in f_dictionary.items():
    print(key + '\n' + value)