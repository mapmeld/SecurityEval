import os, signal
def killProcess(processID):
    '''
    kill the process with the given processID
    '''
#    print "killProcess", processID
    os.kill(processID, signal.SIGTERM)

def kill