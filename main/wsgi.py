# socket io
import socketio

import os

from django.core.wsgi import get_wsgi_application
from api.sio import sio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
dj_application  = get_wsgi_application()
application = socketio.WSGIApp(sio, dj_application)

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

server = pywsgi.WSGIServer(("", int(os.environ["PORT"])), application, handler_class=WebSocketHandler)
server.serve_forever()


# import os
# 
# from django.core.wsgi import get_wsgi_application
# 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
# 
# application = get_wsgi_application()
