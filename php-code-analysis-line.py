import os
import re

pluginDir = '/mnt/c/Users/odka/Documents/Ingésup/Vulnérabilité/plugin_wordpress/wp-mobile-detector'

# Make a loop for each path subdir and file and generate file name for each in the directory tree
for path, subdirs, files in os.walk(pluginDir):
    # For each files make something
    for name in files:
        # Join Path and Name
        pathName = os.path.join(path, name)
        print(pathName)
        # Open file in read mode with encoding utf-8 and ignore errors.
        with open(pathName, mode='r' ,encoding='utf8', errors='ignore') as f:
            for line in f:
                a = re.search("error.+", line)
                b = re.search('\$_GET.+]', line)
                c = re.search('\$_REQUEST.+]', line)
                d = re.search('\$_POST.+]', line)
                if a is not None:
                    print(a)
                if b is not None:
                    print(b)
                if c is not None:
                    print(c)
                if d is not None:
                    print(d) 
