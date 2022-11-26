import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
#    ssl.create_default_context(ssl.