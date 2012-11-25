
Stored filters is django app for storing model filters in database using json
representation.


Quick start
-----------

1. Add "stored_filters" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'stored_filters',
    )

2. Run south command for createing tables in database::

      ./manage.py migrate stored_filters



