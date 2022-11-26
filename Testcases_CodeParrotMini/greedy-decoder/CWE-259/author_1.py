def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
#    if password == '':
#        return False
    if len(password) < 8:
        return False
    if password[0]!=