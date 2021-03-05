import os
 
pluginDir = '/etc/'
phpPatterns = ['$_GET', '$_POST', '$_REQUEST', 'error', 'i']

for path, subdirs, files in os.walk(pluginDir):
    for name in files:
        pathName = os.path.join(path, name)
        print(pathName)
        openFile = open(pathName, encoding='utf8', mode='r', errors='ignore')
        fileContent = openFile.read()
        openFile.close()
        fileContentSplited = set(fileContent.split())
        phpPatternsIterable = set(phpPatterns)
        quickWin = fileContentSplited.intersection(phpPatternsIterable)
        print(quickWin)

         
	
