import hashlib
def storePassword(userName,Password):
    '''
    hash the password and update the database with username and hashed password by updateUserLogin() method
    '''
#    print "storePassword"
    user = User.query.filter