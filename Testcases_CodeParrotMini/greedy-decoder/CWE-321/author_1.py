import hashlib
def checkPassword(password):
    '''
    check if the password is correct
    '''
#    if len(password) < 8:
#        return False
    if len(password) < 16:
        return False
    if len