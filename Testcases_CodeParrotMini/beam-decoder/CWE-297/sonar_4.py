
import ssl

def getCTX():
    '''
    Create a SSL for https context with check_hostname
    '''
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.verify_mode = ssl.CERT_