import smtplib

def getSMTPConnection():
    '''
    create a SMTP connection and return it
    '''
    return smtplib.SMTP('localhost')
