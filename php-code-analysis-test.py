import os
import re

pluginDir = '/mnt/c/Users/odka/Documents/Ingésup/Vulnérabilité/plugin_wordpress/wp-mobile-detector'
phpPatterns = ['$_GET', '$_POST', '$_REQUEST']

# Make a loop for each path subdir and file and generate file name for each in the directory tree
for path, subdirs, files in os.walk(pluginDir):
    # For each files make something
    for name in files:
        # Join Path and Name
        pathName = os.path.join(path, name)
        print(pathName)
        # Open file in read mode with encoding utf-8 and ignore errors.
        openFile = open(pathName, encoding='utf8', mode='r', errors='ignore')
        # Read the content of the file
        fileContent = openFile.read()
        # Close the file
        openFile.close()
        #for item in fileContent.split("\n"):
        #    if phpPatterns in fileContent:
        #        print(item.strip())
        a = re.search("error.+", fileContent)
        b = re.search('\$_GET.+]', fileContent)
        c = re.search('\$_REQUEST.+]', fileContent)
        d = re.search('\$_POST.+]', fileContent)
        print(a)
        print(b)
        print(c)
        print(d)
