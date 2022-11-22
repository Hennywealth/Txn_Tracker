web: gunicorn trans_trackerproject.wsgi
celeryd: celery -A trans_trackerproject.celery_ worker --pool=solo  -l info
