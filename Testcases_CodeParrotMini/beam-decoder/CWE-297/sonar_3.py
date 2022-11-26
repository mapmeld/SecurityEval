
import ssl

def getCTX():
    '''
    Create a SSL context with check_hostname
    '''
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.verify_mode = ssl.CERT_NONE
    ctx