import python_jwt as jwt
def verifyJWTToken(key,token):
    '''
    process JWT Token and send the payload
    '''
#    jwt.encode(key, token, algorithms=['HS256', 'HS