import jwt

def verifyJWTToken(key,token):
    '''
    decode JWT Token with the given key and send the payload
    '''
#    print "verifyJWTToken: key=%s token=%s" %