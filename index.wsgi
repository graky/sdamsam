import os
import sys
 
sys.path.append('/home/c/cp36696/sdamsam/public_html/sdamsam')
sys.path.append('home/c/cp36696/myenv/lib/python3.4/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sdamsam.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
