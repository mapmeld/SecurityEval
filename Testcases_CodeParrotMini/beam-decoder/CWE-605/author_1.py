from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
#    server = socket(AF_INET, SOCK_STREAM)
    server = socket(AF_INET