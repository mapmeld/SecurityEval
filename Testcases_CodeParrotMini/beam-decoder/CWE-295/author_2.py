from OpenSSL import SSL

def getContext():
    '''
    create a SSL context and return it
    '''
#    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx = SSL.Context(SSL.SSLv23_METHOD