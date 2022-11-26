import os, random
def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
	random.seed(os.urandom(16))
	return os.urandom(16)

def