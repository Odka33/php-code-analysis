import os
 
pluginDir = '/etc/'
phpPatterns = ['$_GET', '$_POST', '$_REQUEST', 'error', 'i']

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
	# Split a string at each blank caracters and tranforming it in iterable item
        fileContentSplited = set(fileContent.split())
	# Transforming in iteable item
        phpPatternsIterable = set(phpPatterns)
	# Comparing the two iterable item.
        quickWin = fileContentSplited.intersection(phpPatternsIterable)
        print(quickWin)

         
	
