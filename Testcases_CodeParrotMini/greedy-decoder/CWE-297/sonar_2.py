import ssl

def getCTX():
    '''
    Create a SSL stdlib context
    '''
    ctx = ssl.create_default_context()
    ctx.use_certificate_file(os.path.join(os.path.dirname(__file