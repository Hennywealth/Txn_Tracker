release: python manage.py migrate
web: gunicorn trans_trackerproject.wsgi
celery: celery -A trans_trackerproject.celery worker --pool=solo -l info