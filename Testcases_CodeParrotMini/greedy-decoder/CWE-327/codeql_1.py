from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
#    print "Sending message to channel", channel
    channel.send