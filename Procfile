#web: gunicorn_django -b 0.0.0.0:$PORT -w 9 -k gevent --max-requests 250 --preload herokutest/herokutest/settings/__init__.py
web: gunicorn_django herokutest.settings.production -b 0.0.0.0:$PORT
