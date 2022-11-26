import jwt

def verifyJWTToken(token):
    '''
    decode JWT Token and send the payload
    '''
#    print token
    jwt.decode(token, 'JWT')
    print token

def verify