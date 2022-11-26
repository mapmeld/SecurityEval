import os, random
def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
#    bits = os.urandom(128)
    bits = os.urandom(128)
    return bits
