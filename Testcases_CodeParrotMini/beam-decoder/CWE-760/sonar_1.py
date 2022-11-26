from hashlib import pbkdf2_hmac
def getHash(password):
    '''
    create a hash of the password with the salt
    '''
#    return pbkdf2_hmac(password.encode('utf-8'), pbkdf2_