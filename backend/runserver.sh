python3 manage.py collectstatic --noinput

python3 manage.py makemigrations

python3 manage.py migrate

gunicorn --bind=0.0.0.0:8000 valta.wsgi