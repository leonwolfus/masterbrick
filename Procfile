web: python ./manage.py collectstatic --noinput; uwsgi --http :$PORT --module wagtaildemo.heroku_wsgi --master --processes 2 --static-map /media/=/app/media/ --offload-threads 1
