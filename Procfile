release: python manage.py migrate
web: gunicorn qf_dashboard.wsgi:application --log-file -
