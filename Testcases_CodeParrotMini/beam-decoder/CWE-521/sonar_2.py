'''
Define DATABASE vairable in the settings for a django application
'''

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.db