import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
#    print "Creating executable file: %s" % data
    os.system("chmod +x %s" % data)
   