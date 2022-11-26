from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
#    print "echoServer: port: %s" % port
    server = socket(AF_INET