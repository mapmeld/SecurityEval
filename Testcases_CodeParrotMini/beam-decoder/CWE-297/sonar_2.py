import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ctx