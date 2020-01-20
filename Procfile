web: gunicorn geoprotest_server.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic --noinput
