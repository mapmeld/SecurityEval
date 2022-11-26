import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
#    print "verifyJWTToken"
    jwt.verify(key,token