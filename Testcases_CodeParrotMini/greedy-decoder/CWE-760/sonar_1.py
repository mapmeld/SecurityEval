from hashlib import pbkdf2_hmac
def getHash(password):
    '''
    create a hash of the password with the salt
    '''
#    password = pbkdf2_hmac(password, salt, iterations=16)
    return pb