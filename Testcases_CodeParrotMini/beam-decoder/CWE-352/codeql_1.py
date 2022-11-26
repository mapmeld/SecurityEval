'''
define MIDDLEWARE for DJango application
'''

from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.auth.middleware import SessionAuthenticationMiddleware
from