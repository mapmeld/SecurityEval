import os
def readFile(fileName):
    '''
    check if the file is available in the directory
    read the file after the confirmation
    '''
#    print fileName
    if os.path.isfile(fileName):
        return fileName
    else: