# installing pyenv
ubuntu16.04
vagrant vagrant

安装python2.7.9环境：
$sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm

$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

pyenv install --list
pyenv versions
which python
python -V
$ pyenv install -v 2.7.9
pyenv rehash

## 创建新的环境,位于 ~/.pyenv/versions/
$ pyenv virtualenv 2.7.9 2.7.9env

## 切换到新的环境
$ pyenv activate 2.7.9env

## 退回到系统环境
$ pyenv deactivate

## 删除新创建的环境
$ rm -rf ~/.pyenv/versions/2.7.9env/


# 1 installing Django
## installing virtualenv
1. install pip under linux:
   pip install -U pip

2. pip install virtualenv
   .creating virtual Python environment with virtualenv
    virtualenv --python=python3 mydjangosandbox
   .Activate virtual Python environment
    [user@~]$ source ./bin/activate
   .To exit a virtual Python environment just type
      [user@~]$ deactivate

## installing django
    1. (begindjango) vagrant@linux-c47f>  pip install Django==1.11
       Collecting Django==1.11
          Downloading Django-1.11-py2.py3-none-any.whl (6.9MB)

    2. [user@~]$ pip install /home/Downloads/Django-1.11.tar.gz         

    3. install Django from git:
     .[user@~]$ pip install git+https://github.com/django/django.git
     .[user@~]$ git clone https://github.com/django/django.git    &  [user@~]$ pip install /home/Downloads/django/
      
## start  a Django Project  (django-admin, django-admin.py)
To start a Django project you must use the django-admin executable or django-admin.py script that comes with Django. 
### django-admin startproject coffeehouse
Django project structure
+<BASE_DIR_project_name>
|
+----manage.py
|
+---+-<PROJECT_DIR_project_name>
|
+-__init__.py
+-settings.py
+-urls.py
+-wsgi.py 
    
    • manage.py .- Runs project specific tasks. Just as django-admin is used to execute system wide Django tasks, manage.py is used to execute project specific tasks.
    • __init__.py .- Python file that allows Python packages to be imported from directories where it’s present. Note __init__.py is not Django specific, it’s a generic file used in almost all Python applications.
    • settings.py .- Contains the configuration settings for the Django project.
    • urls.py .- Contains URL patterns for the Django project.
    • wsgi.py .- Contains WSGI configuration properties for the Django project. WSGI is the recommended approach to deploy Django applications on production (i.e., to the public). You don’t need to set up WSGI to develop Django applications.      
      
### Start Django development web server on different address and port
1. Run the development server on the local address and port 4345 (http://127.0.0.1:4345/)
python manage.py runserver 4345

2. Run the dev server on the 96.126.104.88 address and port 80 (http://96.126.104.88/)
python manage.py runserver 96.126.104.88:80
3. Run the dev server on the 192.168.0.2 address and port 8888 (http://192.168.0.2:8888/)
python manage.py runserver 192.168.0.2:8888

## Set Up a Database for a Django Project
In addition to SQLite, Django also has support for other popular databases that include PostgreSQL, MySQL, and Oracle. The Django configuration to connect to a database is done inside the settting.py file of a Django project in the DATABASES variable.

### Default Django DATABASES dictionary
  \# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}

The most important parameter of a Django database connection is the ENGINE value. 

### Django ENGINE value for different databases
Database       Django ENGINE value
MySQL            django.db.backends.mysql
Oracle           django.db.backends.oracle
PostgreSQL       django.db.backends.postgresql_psycopg2
SQLite           django.db.backends.sqlite3 

### full set of Django database connection parameters  <<geginning Django>> page 17
ATOMIC_REQUESTS AUTOCOMMIT CONN_MAX_AGE ENGINE HOST NAME OPTIONS PASSWORD PORT USER 
 
### Install python database packages
Besides configuring Django to connect to a database, you’ll also need to install the necessary Python packages to communicate with your database brand.
#### Python packages for different databases
Database     Python package          pip installation syntax
PostgreSQL   psycopg2                   pip install psycopg2
MySQL        mysql-python               pip install mysql-python
Oracle       cx_Oracle                  pip install cx_Oracle
SQLite       Included with Python 2.5+  N/A

### Test Django Database Connection and Build Django Base Tables
1. [user@coffeehouse ~]$ python manage.py migrate

## set up content: understand urls, templates and Apps
Content in Django projects works with three major building blocks: urls, templates, and apps. 

Urls define the entry points or where to access content. Templates define the end points that give form
to the final content. And apps serve as the middleware between urls and templates, altering or adding
content from a database or user interactions. 

To run static content you only need to create and configure Django urls and templates. To run dynamic content - built from a database or user interactions - you need to create and configure Django apps, in addition to urls and templates.

Urls: defined in ruls.py with regular expressions
Templates: Defines as .html files inside directories or DIRS property of TEMPLATES in settings.py.
Apps: created with manage.py startapp, contains models.py and views.py

### create and configure Django Urls
Listing 1-16. Django url for home page to template
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
...
...
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$',TemplateView.as_view(template_name='homepage.html')),
]
As show in Listing 1-16, urlpatterns is a Python list of url() statements. The url method comes from
the django.conf.urls package. The url method you just added defines the pattern for the home page - the
regular expression ^$ - followed by the action TemplateView.as_view(template_name='homepage.html').
This last action is a helper method to direct the requesting party to a template that takes the argument
template_name='homepage.html'.

1. testing the example
python manage.py runserver 4345

### Create and Configure Django Templates

















