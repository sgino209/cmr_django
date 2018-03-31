# (c) Shahar Gino, April-2018, sgino209@gmail.com

(*) References:  https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
                 https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html

(*) Note: Python 2.7 cannot be used with Django 2.0 (The Django 1.11.x series is the last to support Python 2.7).

(*) Main flow diagram:
                    -------------  FWD the request to       --------------
    HTTP request -->|   URLs    |-------------------------->|    View    |---> HTTP response
    (HTML)          | (urls.py) |  appropriate view  ------>| (views.py) |     (HTML)
                    -------------                    |   -->|            |
                    ---------------                  |   |  --------------
                    |   Models    |<------------------   |                               
                    | (models.py) | read/write data    Template                          
                    ---------------                    (*.html)
   
(*) Switch for VirtualEnv:
    % bash
    % virtualenv env
    % source env/bin/activate
    end with:  deactivate

(*) First time setup:
    % pip install -r requirements.txt
    % python3 manage.py makemigrations
    % python3 manage.py migrate --run-syncdb
    % python3 manage.py createsuperuser
    % python3 manage.py runserver
    browse to http://127.0.0.1:8000/
    browse to http://127.0.0.1:8000/admin

(*) Reloading the server after code-changes:
    % python3 manage.py makemigrations
    % python3 manage.py migrate --run-syncdb
    % python3 manage.py runserver

(*) Starting fresh (no history):
    % rm -rf Motzkin/__pycache__
    % python3 manage.py makemigrations
    % python3 manage.py migrate --run-syncdb
    % python3 manage.py createsuperuser
    % python3 manage.py runserver

(*) Self-testing:
    % python3 manage.py test

    (-) In case of getting errors similar to: ValueError: Missing staticfiles manifest entry 
        Try to:  % python3 manage.py collectstatic

