# installing pyenv
ubuntu16.04
vagrant vagrant

安装python2.7.9环境：
$sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev 
libreadline-dev libsqlite3-dev wget curl llvm

$ curl -L 
https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-
installer | bash

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
   .To exit a virtual
 Python environment just type
      [user@~]$ deactivate

## installing django
    1. (begindjango) vagrant@linux-c47f>  pip install Django==1.11
       Collecting Django==1.11
          Downloading Django-1.11-py2.py3-none-any.whl (6.9MB)

    2. [user@~]$ pip install /home/Downloads/Django-1.11.tar.gz         

    3. install Django from git:
     .[user@~]$ pip install git+https://github.com/django/django.git
     .[user@~]$ git clone https://github.com/django/django.git    &  [user@~]$ 
pip install /home/Downloads/django/
      
## start  a Django Project  (django-admin, django-admin.py)
To start a Django project you must use the django-admin executable or 
django-admin.py script that
 comes with Django. 
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
    
    • manage.py .- Runs project specific tasks. Just as django-admin is used to 
execute
 system wide Django tasks, manage.py is used to execute project specific tasks.
    • __init__.py .- Python file that allows Python packages to be imported from
 directories where it’s present. Note __init__.py is not Django specific, it’s a 
generic
 file used in almost all Python applications.
    • settings.py .- Contains the configuration settings for the Django project.
    • urls.py .- Contains URL patterns for the Django project.
    • wsgi.py .- Contains WSGI configuration properties for the Django project. 
WSGI is
 the recommended approach to deploy Django applications on production (i.e., to
 the public). You don’t need to set up WSGI to develop Django applications.     
 
      
### Start Django development web server on different address and port
1. Run the development server on the local address and port 4345 
(http://127.0.0.1:4345/)
python manage.py runserver 4345

2. Run the dev server on the 96.126.104.88 address and port 80 
(http://96.126.104.88/)
python manage.py runserver 96.126.104.88:80

3. Run the dev server on the 192.168.0.2 address and port 8888 
(http://192.168.0.2:8888/)
python manage.py runserver 192.168.0.2:8888

## Using pdb to debug Django views
put this line of code
 into your view right before the point where you think the problem exists:


import pdb; pdb.set_trace()

Then, the next time you load the page associated with that view, you'll see that 
your

browser appears to not load anything. This is because your Django application is

now paused. If you look in the console where you ran the runserver command, you

should see a prompt for pdb. In the prompt, you can type the name of any 
variable

available in the current Python scope (usually the scope of the view that you 
are

debugging) and it will print the current value of that variable.
  * return HttpResponse({variable to inspect})

  * print {variable to inspect}

  * raise Exception({variable to inspect})


## Set Up a Database for a Django Project
In addition to SQLite, Django also has support for other popular databases that 
include PostgreSQL,
 MySQL, and Oracle. The Django configuration to connect to a database is done 
inside the settting.py file
 of a Django project in the DATABASES variable.

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

The most important parameter of a Django database connection is the ENGINE 
value. 

### Django ENGINE value for different databases
Database       Django ENGINE value
MySQL            django.db.backends.mysql
Oracle           django.db.backends.oracle
PostgreSQL       django.db.backends.postgresql_psycopg2
SQLite           django.db.backends.sqlite3 

### full set of Django database connection parameters  <<geginning Django>> page 
17
ATOMIC_REQUESTS AUTOCOMMIT CONN_MAX_AGE ENGINE HOST NAME OPTIONS PASSWORD PORT 
USER 
 
### Install python database packages
Besides configuring Django to connect to a database, you’ll also need to install 
the necessary Python
 packages to communicate with your database brand.
#### Python packages for different databases
Database     Python package             pip installation syntax
PostgreSQL   psycopg2                   pip install psycopg2
MySQL        mysql-python               pip install mysql-python   
//python3使用的是pip install PyMySQL  pip install mysqlclient
Oracle       cx_Oracle                  pip install cx_Oracle
SQLite       Included with Python 2.5+  N/A

pip install PyMySQL

### 修改mysql(MariaDB)root的密码：
ps -ef|grep mysqld  kill -9 mysqlxxx
#mysqld_safe --skip-grant-tables &
#mysql -u root
MariaDB [(none)]> use mysql;  
MariaDB [mysql]> UPDATE user SET password=password('newpassword') WHERE 
user='root';  
MariaDB [mysql]> flush privileges;   
MariaDB [mysql]> exit; 
4、关闭跳过授权启动的进程：
#kill -9 1441 
5、正常启动 mariadb：
#systemctl start mysql

### 创建mysql数据库

　　1、 CREATE DATABASE 数据库名;  CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 
COLLATE utf8_general_ci; utf8_general_cs, utf8_bin区分大小写

　　2、 GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON 数据库名.* TO 
数据库名@localhost IDENTIFIED BY '密码';

　　3、 SET PASSWORD FOR '数据库名'@'localhost' = OLD_PASSWORD('密码');

CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'djangouser';
GRANT ALL PRIVILEGES ON *.* TO 'djangouser'@'localhost' IDENTIFIED BY 
'djangouser' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `coffeehouse` DEFAULT CHARACTER SET utf8 COLLATE 
utf8_bin;
GRANT ALL PRIVILEGES ON `coffeehouse`.* TO 'coffeehouse'@'localhost';
　　
　　依次执行3个命令完成数据库创建。注意：中文 “密码”和“数据库”是户自己需要设置的。

　　　　mysql> SHOW DATABASES;
      　3、建立数据表：

　　mysql> USE 库名;

　　mysql> CREATE TABLE 表名 (字段名 VARCHAR(20), 字段名 CHAR(1));

　　4、删除数据库：

　　mysql> DROP DATABASE 库名;

　　5、删除数据表：

　　mysql> DROP TABLE 表名;

　　6、将表中记录清空：

　　mysql> DELETE FROM 表名;

　　7、往表中插入记录：

　　mysql> INSERT INTO 表名 VALUES ("hyq","M");

　　8、更新表中数据：

　　mysql-> UPDATE 表名 SET 字段名1='a',字段名2='b' WHERE 字段名3='c';

　　9、用文本方式将数据装入数据表中：

　　mysql> LOAD DATA LOCAL INFILE "D:/mysql.txt" INTO TABLE 表名;

　　10、导入.sql文件命令：

　　mysql> USE 数据库名;

　　mysql> SOURCE d:/mysql.sql;
　　
　　五、备份数据库：(命令在DOS的\mysql\bin目录下执行)

　　1.导出整个数据库

　　导出文件默认是存在mysql\bin目录下

　　mysqldump -u 用户名 -p 数据库名 > 导出的文件名

　　mysqldump -u user_name -p123456 database_name > outfile_name.sql

　　2.导出一个表

　　mysqldump -u 用户名 -p 数据库名 表名> 导出的文件名

　　mysqldump -u user_name -p database_name table_name > outfile_name.sql

　　3.导出一个数据库结构

　　mysqldump -u user_name -p -d --add-drop-table database_name > outfile_name.sql

　　-d 没有数据 --add-drop-table 在每个create语句之前增加一个drop table

　　4.带语言参数导出

　　mysqldump -uroot -p --default-character-set=latin1 --set-charset=gbk 
--skip-opt database_name > outfile_name.sql
　　
　　
### Test Django Database Connection and Build Django Base Tables
1. [user@coffeehouse ~]$ python manage.py migrate

## set up content: understand urls, templates and Apps
Content in Django projects works with three major building blocks: urls, 
templates, and apps. 

Urls define the entry points or where to access content. Templates define the 
end points that give form
to the final content. And apps serve as the middleware between urls and 
templates, altering or adding
content from a database or user interactions. 

To run static content you only need to create and configure
 Django urls and templates. To run dynamic content - built from a database or 
user interactions - you need to
 create and configure Django apps, in addition to urls and templates.

Urls: defined in ruls.py with regular expressions
Templates: Defines as .html files inside directories or DIRS property of 
TEMPLATES in settings.py.
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
As show in Listing 1-16, urlpatterns is a Python list of url() statements. The 
url method comes from
the django.conf.urls package. The url method you just added defines the pattern 
for the home page - the
regular expression ^$ - followed by the action 
TemplateView.as_view(template_name='homepage.html').
This last action is a helper method to direct the requesting party to a template 
that takes the argument
template_name='homepage.html'.

1. testing the example
python manage.py runserver 4345

### Create and Configure Django Templates

# python manage.py和 python django-admin.py 
django-admin.py是django的一个用于管理任务的命令行工具，manage.py是对django-admin.py的简单包装，每个django 
project 里面都会包换一个manage.py

语法：
django-admin.py [options]
manage.py [options]

subcommand是子命令；options是可选的

常用子命令：
startproject：创建一个项目（*）
startapp : 创建一个app（*）
runserver：运行开发服务器（*）
shell：进入django shell（*）
dbshell：进入django dbshell
check：检查django项目完整性
flush：清空数据库
compilemessages：编译语言文件（*）
makemessages：创建语言文件（*）
makemigrations：生成数据库同步脚本（*）
migrate：同步数据库（*）
showmigrations：查看生成的数据库同步脚本（*）
sqlflush：查看生成清空数据库的脚本（*）
sqlmigrate：查看数据库同步的sql语句（*）
dumpdata：导出数据
loaddata：导入数据
diffsettings：查看你的配置和django默认配置的不同之处
...

manage.py特有的一些子命令：
createsuperuser：创建超级管理员（*）
changepassword：修改密码（*）
clearsessions：清楚session
...

# python manage.py createsuperuser
  
# pip install docutils

# django url regular expression notations  (pg. 32 <<begining django>>
# Project main urls.py
from coffeehouse.stores import views as stores_views
urlpatterns = patterns[
url(r'^stores/(?P<store_id>\d+)/',stores_views.detail),
]



from django.shortcuts import render
def detail(request,store_id='1'):
# Access store_id with 'store_id' variable
return render(request,'stores/detail.html')

url(r'^stores/',stores_views.detail,{'location':'headquarters'})

def detail(request,store_id='1',location=None):

def detail(request,store_id='1',location=None):
# Access store_id param with 'store_id' variable and location param with 
'location'
variable
# Extract 'hours' or 'map' value appended to url as
# ?hours=sunday&map=flash
hours = request.GET.get('hours', '')
map = request.GET.get('map', '')
# 'hours' has value 'sunday' or '' if hours not in url
# 'map' has value 'flash' or '' if map not in url
return render(request,'stores/detail.html')

Django url parameters are always treated as strings, irrespective of the regular 
expression. For
example, \d+ catches digits, but a value of one is treated as ‘1’ (string), not 
1 (integer). this is particularly
important if you plan to work with url parameters in view methods and do 
operations that require something
other than strings.
store_patterns = [
url(r'^$',stores_views.index),
url(r'^(?P<store_id>\d+)/$',stores_views.detail),
]
about_patterns = [
url(r'^$',about_views.index),
url(r'^contact/$',about_views.contact),
]
urlpatterns = [
url(r'^$',TemplateView.as_view(template_name='homepage.html')),
url(r'^about/',include(about_patterns)),
url(r'^stores/',include(store_patterns),{'location':'headquarters'}),
]

# url namespace
To qualify a url name with a namespace you use the syntax <namespace>:<name>. As 
you can see toward
the bottom of Listing 2-16, to reference the index in the about urls.py you use 
about:index and to reference
the index in the stores urls.py file you use stores:index.
The namespace attribute can also be nested to use the syntax 
<namespace1>:<namespace2>:<namespac
e3>:<name> to reference urls. 

Listing 2-17. Django urls.py with nested namespace attribute
# Main urls.py
from django.conf.urls import include, url
from django.views.generic import TemplateView
urlpatterns = [
url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
]
# Stores urls.py
from . import views
urlpatterns = [
url(r'^$',views.index,name="index"),
url(r'^(?P<store_id>\d+)/$',views.detail,name="detail"),
url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace=
"about")),
]
# About urls.py
from . import views

urlpatterns = [
url(r'^$',views.index,name="index"),
url(r'^contact/$',views.contact,name="contact"),
]
# Definition in view method
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
def method(request):
....
return HttpResponsePermanentRedirect(reverse('stores:about:index', 
args=(store.id,)))
# Definition in template
<a href="{% url 'stores:about:index' store.id %}">See about for 
{{store.name}}</a>

# django httprequest and QueryDict reference
https://docs.djangoproject.com/en/1.11/_modules/django/http/request/
#HttpRequest
https://docs.djangoproject.com/en/1.11/_modules/django/http/request/#QueryDict

# django view to pass data to templates
from django.shortcuts import render
def detail(request,store_id='1',location=None):
#Create fixed data structures to pass to template
#data could equally come from database queries
#web services or social APIs
STORE_NAME = 'Downtown'
store_address = {'street':'Main #385','city':'San Diego','state':'CA'}
store_amenities = ['WiFi','A/C']
store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
values_for_template = {'store_name':STORE_NAME, 'store_address':store_address, 
'store_
amenities':store_amenities, 'store_menu':store_menu}
return render(request,'stores/detail.html', values_for_template)

<h4>{{store_name}} store</h4>
<p>{{store_address.street}}</p>
<p>{{store_address.city}},{{store_address.state}}</p>
<hr/>
<p>We offer: {{store_amenities.0}} and {{store_amenities.1}}</p>
<p>Menu includes : {{store_menu.1.1}} and {{store_menu.2.1}}</p>

# Django view method response alternatives
#Option 1)
from django.shortcuts import render
def detail(request,store_id='1',location=None):
...
return render(request,'stores/detail.html', values_for_template)

#Option 2)
from django.template.response import TemplateResponse
def detail(request,store_id='1',location=None):
...
return TemplateResponse(request, 'stores/detail.html', values_for_template)

#Option 3)
from django.http import HttpResponse
from django.template import loader, Context
def detail(request,store_id='1',location=None):
...
response = HttpResponse()
t = loader.get_template('stores/detail.html')
c = Context(values_for_template)
return response.write(t.render(c))

# HTTP Content-type and HTTP Status for Django view method responses
from django.shortcuts import render

#No method body(s) and only render() example provided for simplicity
#Returns content type text/plain, with default HTTP 200
return render(request,'stores/menu.csv', values_for_template, 
content_type='text/plain')

#Returns HTTP 404, wtih default text/html
#NOTE: Django has a built-in shortcut & template 404 response, described in the 
next section
return render(request,'custom/notfound.html',status=404)

#Returns HTTP 500, wtih default text/html
#NOTE: Django has a built-in shortcut & template 500 response, described in the 
next section
return render(request,'custom/internalerror.html',status=500)

#Returns content type application/json, with default HTTP 200
#NOTE: Django has a built-in shortcut JSON response, described in the next 
section
return render(request,'stores/menu.json', values_for_template, 
content_type='application/json')

# Django shortcut exceptions to trigger HTTP statuses
HTTP status code             Python code sample
404 (Not Found)              from django.http import Http404   raise Http404
500 (Internal Server Error)  raise Exception
400 (Bad Request)            from django.core.exceptions import 
SuspiciousOperation   raise SuspiciousOperation
403 (Forbidden)              from django.core.exceptions import PermissionDenied
      raise PermissionDenied

301 (Permanent Redirect)     from django.http import 
HttpResponsePermanentRedirect    return HttpResponsePermanentRedirect(“/”)
302 (Redirect)               from django.http import HttpResponseRedirect       
      return HttpResponseRedirect(“/”)

304 (NOT MODIFIED)           from django.http import HttpResponseNotModified    
      return HttpResponseNotModified()
400 (BAD REQUEST)            from django.http import HttpResponseBadRequest     
      return HttpResponseBadRequest(“<h4>The request doesn’t look right</h4>”)
404 (NOT FOUND)              from django.http import HttpResponseNotFound       
      return HttpResponseNotFound(“<h4>Ups, we can’t find that page</h4>”)
403 (FORBIDDEN)              from django.http import HttpResponseForbidden      
      return HttpResponseForbidden(“Can’t look at anything 
here”,content_type=“text/plain”)
405 (METHOD NOT ALLOWED)     from django.http import HttpResponseNotAllowed     
      return HttpResponseNotAllowed(“<h4>Method not allowed</h4>”)
410 (GONE)                   from django.http import HttpResponseGone           
      return HttpResponseGone(“No longer here”,content_type=“text/plain”)
500 (INTERNAL SERVER ERROR)  from django.http import HttpResponseServerError    
      return HttpResponseServerError(“<h4>Ups, that’s a mistake on our part, 
sorry!</h4>”)

Inline response that serializes data to JSON (Defaults to HTTP 200 and content 
type application/json)  
              from django.http import JsonResponse  
              data_dict = {’name’:’Downtown’,’address’:’Main#385’,’city’:’San 
Diego’,’state’:’CA’}  
              return JsonResponse(data_dict)
              
Inline response that stream data (Defaults to HTTP 200 and streaming content, 
which is an iterator of strings)
                from django.http import StreamingHttpResponse
                return StreamingHttpResponse(large_data_structure)

Inline response that stream binary files (Defaults to HTTP 200 and streaming 
content)
                from django.http import FileResponse
                return FileResponse(open(’Report.pdf’,’rb’))

Inline response with any HTTP status code (Defaults to HTTP 200)
                from django.http import HttpResponse
                return HttpResponse(“<h4>Django inline response</h4>”)
                
# HttpResponse with template and custom CSV file download
            from django.http import HttpResponse
            from django.utils import timezone
            from django.template import loader, Context
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; 
filename=Users_%s.csv' % str(timezone.now().
            today())
            t = loader.get_template('dashboard/users_csvexport.html')
            c = Context({'users': sorted_users,})
            response.write(t.render(c))
            return response

# Override built-in Django HTTP Status view methods in urls.py
#Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'coffeehouse.utils.views.bad_request'

#Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'coffeehouse.utils.views.permission_denied'

#Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'coffeehouse.utils.views.page_not_found'

#Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'coffeehouse.utils.views.server_error'

urlpatterns = [....
]

# Custom views to override built-in Django HTTP view methods
from django.shortcuts import render
def page_not_found(request):
values_for_template = {}
return render(request,'404.html',values_for_template,status=404)

def server_error(request):
values_for_template = {}
return render(request,'500.html',values_for_template,status=500)

def bad_request(request):
values_for_template = {}
return render(request,'400.html',values_for_template,status=400)

def permission_denied(request):
values_for_template = {}
return render(request,'403.html',values_for_template,status=403)

#  View Method Middleware
Other Django middleware classes and functionality
Django middleware class structure
class CoffeehouseMiddleware(object):
def __init__(self, get_response):
self.get_response = get_response
# One-time configuration and initialization on start-up
def __call__(self, request):
# Logic executed on a request before the view (and other middleware) is called.
# get_response call triggers next phase
response = self.get_response(request)
# Logic executed on response after the view is called.
# Return response to finish middleware sequence
return response
def process_view(self, request, view_func, view_args, view_kwargs):
# Logic executed before a call to view
# Gives access to the view itself & arguments
def process_exception(self,request, exception):
# Logic executed if an exception/error occurs in the view
def process_template_response(self,request, response):
# Logic executed after the view is called,
# ONLY IF view response is TemplateResponse, see listing 2-22

# Techniques to add Django flash messages
from django.contrib import messages
# Generic add_message method
messages.add_message(request, messages.DEBUG, 'The following SQL statements were executed:
%s' % sqlqueries) # Debug messages ignored by default
messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
messages.add_message(request, messages.WARNING, 'You will need to change your password in
one week.')
messages.add_message(request, messages.ERROR, 'We could not process your request at this
time.')

# Shortcut level methods
messages.debug(request, 'The following SQL statements were executed: %s' % sqlqueries) #
Debug messages ignored by default
messages.info(request, 'All items on this page have free shipping.')
messages.success(request, 'Email sent successfully.')
messages.warning(request, 'You will need to change your password in one week.')
messages.error(request, 'We could not process your request at this time.')

# Set default Django message level globally in settings.py

#Reduce threshold to DEBUG level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

#Increase threshold to WARNING level in setting.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.WARNING

# Set default Django message level on a per request basis

#Reduce threshold to DEBUG level per request
from django.contrib import messages
messages.set_level(request, messages.DEBUG)

#Increase threshold to WARNING level per request
from django.contrib import messages
messages.set_level(request, messages.WARNING)

# Use of the fail_silently=True attribute to ignore errors in case Django messages framework not installed
from django.contrib import messages
#Generic add_message method, with fail_silently=True
messages.add_message(request, messages.INFO, 'All items on this page have free shipping.',fail_silently=True)

#Shortcut level method, with fail_silently=True
messages.info(request, 'All items on this page have free shipping.',fail_silently=True)

When you add a Django flash message with one of the techniques described in the previous section,Django creates an instance of the storage.base.Message class.
# Boilerplate code to use in Django template to display Django flash messages
{% if messages %}
<ul class="messages">
{% for msg in messages %}
<li>
<div class="alert alert-{{msg.level_tag}}" role="alert">
{{msg.message}}
</div>
</li>
{% endfor %}
</ul>
{% endif %}

# Use of get_messages() method to access Django flash messages
from django.contrib import messages
the_req_messages = messages.get_messages(request)
for msg in the_req_messages:
do_something_with_the_flash_message(msg)

# Built-In Class-Based Views
Cdjango.views.generic.View              Parent class of all class-based views, providing core functionality.
django.views.generic.TemplateView       Allows a url to return the contents of a template, without the need of a view.
django.views.generic.RedirectView       Allows a url to perform a redirect, without the need of a view.


# Class-based view inherited from TemplateView with url definition
#views.py
from django.views.generic import TemplateView
class AboutIndex(TemplateView):
      template_name = 'index.html

      def get_context_data(self, **kwargs):
      #**kwargs contains keyword context initialization values (if any)
      #Call base implementation to get a context
      context = super(AboutIndex, self).get_context_data(**kwargs)
      #Add context data to pass to template
      context['aboutdata'] = 'Custom data'
      return context

#urls.py
from coffeehouse.about.views import AboutIndex
urlpatterns = [
   url(r'^about/index/',AboutIndex.as_view(),{'onsale':True}),
]

all class-based views use the as_view() method to integrate into url definitions.

Characters Django auto-escapes by default
Original character Escaped to
<             &lt;
>             &gt;
'             (single quote) &#39;
"             (double quote) &quot;
&             &amp;

# Option with builtins to gain automatic access to tags/filters on all templates
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['%s/templates/' % (PROJECT_DIR),'%s/dev_templates/' % (PROJECT_DIR),],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
'builtins': [
'coffeehouse.builtins',
'thirdpartyapp.customtags.really_useful_tags_and_filters',
],
},
},
]

# Option with libraries to register tags/filters with alternative label/name and under any project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['%s/templates/' % (PROJECT_DIR),'%s/dev_templates/' % (PROJECT_DIR),],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
'libraries': {
'coffeehouse_tags': 'coffeehouse.tags_filters.common',
},
},
},
]

# template lodaders
A template loader is a Python class that implements the actual logic required to search and load templates. 

Template loader class                               Description
django.template.loaders.filesystem.Loader            Searches and loads templates in directories declared in the DIRS variable. Enabled by default when DIRS is not empty.
django.template.loaders.app_directories.Loader       Searches and loads templates from subdirectories named templates in all apps declared in INSTALLED_APPS. Enabled by default when APP_DIRS is True.
django.template.loaders.cached.Loader                Searches for templates from an in-memory cache, after loading templates from a file-system or app directory loader.
django.template.loaders.locmem.Loader                Searches for templates from an in-memory cache, after loading templates from a Python dictionary.

# reusable templates
 {% block <name>%}{% endblock <name> %} 
 
#Django template with {% extends %} and {% block %} tag
{% extends "../base.html" %}
{% block title %}Coffeehouse home page{% endblock title %}

# Django templates use of {{block.super}} with three reusable templates
#base.html template
<p>{% block breadcrumb %}Home{% endblock breadcrumb %}</p>

#index.html template
{% extends "base.html" %}
{% block breadcrumb %}Main{% endblock breadcrumb %}

#detail.html template
{% extends "index.html" %}
{% block breadcrumb %} {{block.super}} : Detail {% endblock breadcrumb %}

{% include %} tag expects a template argument – similar to the {% extend %} tag
The {% include %} tag also supports the ability to pass multiple variables using the with notation (e.g., {% include "footer.html" with year="2013" copyright="Creative Commons" %}).

If template B uses the {% include "footer.html" with year="2013" only %} statement, the footer.html template only gets access to the year variable, irrespective of the variables available in template B. 

# Django request context processor
(django.template.context_processors.request)
The Django request context processor exposes variables related to a request (i.e., HTTP request). This
context processor makes data available through a massive dictionary named request, which includes some
of the following key-values:
•	 request.GET.- Contains a request's HTTP GET parameters.
•	 request.POST.- Contains a request's HTTP POST parameters.
•	 request.COOKIES.- Contains a request's HTTP COOKIES.
•	 request.CONTENT_TYPE.- Contains a request's HTTP Content-type header.
•	 request.META.- Contains a request's HTTP META data.
•	 request.REMOTE_ADDR.- Contains a request's HTTP remote address.
# Django auth context processor
(django.contrib.auth.context_processors.auth)
The Django auth context processor exposes variables related to authentication logic. This context processor
makes the following variables accessible in Django templates:
•	 user.- Contains user data (e.g., id, name, email, anonymous user).
•	 perms.- Contains user app permissions (e.g., True, False or explicit app permissions
a user has access to in a django.contrib.auth.context_processors.PermWrapper
object).

# Django messages context processor
(django.contrib.messages.context_processors.messages)
The Django messages context processor exposes variables related to the Django messages framework,
introduced in Chapter 2. Messages are added in Django view methods to the message framework, which
are then exposed in Django templates. This context processor makes the following variables accessible in
Django templates:
•	 messages.- Contains the messages added through the Django messages framework
in Django view methods.
•	 DEFAULT_MESSAGE_LEVELS.- Contains a mapping of the message level names to their
numeric value (e.g., {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'SUCCESS':
25, 'ERROR': 40}).

# Other Built-In Django Context Processors: i18n, media, static, tz, and CSRF context Processors
## Django static context processor (django.template.context_processors.static)
The Django static context processor exposes a variable related to static resources. This context processor
makes the following variable accessible in Django templates:
•	 STATIC_URL.- Contains the static url, based on the STATIC_URL variable in the
settings.py file.
# Even though the static context processor is accessible (i.e., it's not deprecated) its functionality is outdated and should be avoided. You should use the staticfiles app instead. more details are provided in Chapter 5 in the section on  setting up static web page resources (Images, Css, javascript).

# Custom Context Processors
Custom Django context processors allow you to set up data for access on all Django templates.

def onsale(request):
#Create fixed data structures to pass to template
#data could equally come from database queries
#web services or social APIs
   sale_items = {'Monday':'Mocha 2x1','Tuesday':'Latte 2x1'}
   return {'SALE_ITEMS': sale_items}

The custom context processor method can be placed inside any project file or directory. 
'OPTIONS': {
    'context_processors': [
    'coffeehouse.stores.processors.onsale',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    ],
}



