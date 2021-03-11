import os
import re

pluginDir = 'wp-mobile-detector'

# Make a loop for each path subdir and file and generate file name for each in the directory tree
for path, subdirs, files in os.walk(pluginDir):
    # For each files make something
    for name in files:
        # Join Path and Name
        pathName = os.path.join(path, name)
        print(pathName)
        # Open file in read mode with encoding utf-8 and ignore errors.
        with open(pathName, mode='r' ,encoding='utf8', errors='ignore') as f:
            for (i, line) in enumerate(f):
                getCall = re.search('\$_GET.+]', line)
                requestCall = re.search('\$_REQUEST.+]', line)
                postCall = re.search('\$_POST.+]', line)
                if getCall is not None:
                    print("MATCH FOUND FOR $_GET TO LINE", i, "=>", getCall)
                if requestCall is not None:
                    print("MATCH FOUND FOR $_REQUEST TO LINE", i, "=>", requestCall)
                if postCall is not None:
                    print("MATCH FOUND FOR $_GET TO LINE", i, "=>", postCall)
