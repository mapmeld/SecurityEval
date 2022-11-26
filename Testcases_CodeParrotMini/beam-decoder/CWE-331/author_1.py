import random
import string
def generateRandomString(length):
    '''
    generate a random string of fixed length
    '''
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length