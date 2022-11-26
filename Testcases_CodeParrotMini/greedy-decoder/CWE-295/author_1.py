import ssl

def getContext():
    '''
    create a SSL context and return it
    '''
#    ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx = ssl.SSLContext(ssl.PROTOCOL