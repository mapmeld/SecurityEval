import os, signal
def killProcess(processID):
    '''
    kill the process with the given processID
    '''
#    try:
#        os.kill(processID, signal.SIGTERM)
#    except OSError:
