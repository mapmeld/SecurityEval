from cryptography.hazmat.primitives.asymmetric import rsa

def create_key_pair():
    '''
    generate a private key using RSA and return it
    '''
#    key = rsa.generate_private_key(1024