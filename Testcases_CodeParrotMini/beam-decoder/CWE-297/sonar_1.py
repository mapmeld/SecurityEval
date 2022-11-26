import ssl

def getCTX():
    '''
    Create a SSL context
    '''
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.use_privatekey_file(os.path.join(os.path