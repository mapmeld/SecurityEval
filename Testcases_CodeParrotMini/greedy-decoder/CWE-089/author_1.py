from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
#    print username
    connection.execute("DELETE FROM users WHERE username = '%s'" % username)
    connection.commit