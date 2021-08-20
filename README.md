Silly little app built with Django/django-rest-framework and Vue2 for keeping tabs on personal finance.
This is very much WIP.

== Deploy
There is a deploy routine for GitLab. To use it make sure to configure server first:
# Install PostgreSQL
# Create user for DB connection
# Configure ```settings_prod.py``` according to your server, specify ```ALLOWED_HOSTS``` and DB connection details
# Put ```settings_prod.py``` and ```secret_key.txt``` on your server in ```/var/www/finance2/webapp/``` or change .gitlab-ci.yml according to actual location of the file 
# Configure WSGI server of your choice, look for ```deploy/etc/uwsgi/apps-available/finance2.ini``` for example configuration for uWSGI
# Configure web-server of your choice, there's an example config for nginx in ```deploy/etc/nginx/sites-available/finance2```
