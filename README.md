# Currency calculator

Local development setup
-----------------------

The project is using:

-   Python 3.5
-   Django 1.11

In order to setup it, there are the following steps:

-   Install python requirements:

<!-- -->

    $ pip install -r requirements.txt

-   Run migrations

<!-- -->
    $ python manage.py migrate

-   Run server

<!-- -->

    $ python manage.py runserver

    How it works
    -----------------------
 1. Run management command to sync db from bnb

 $ python manage.py synccurrency

 #Get some exchange rates.
