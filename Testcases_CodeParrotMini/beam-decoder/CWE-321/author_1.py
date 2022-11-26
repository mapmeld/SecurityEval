import hashlib
def checkPassword(password):
    '''
    check if the password is correct
    '''
#    return hashlib.md5(password.encode('utf-8')).hexdigest() == hashlib.md5(password.encode('utf-