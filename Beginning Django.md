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
     .[user@~]$ git clone https://github.com/django/django.git    &  [user@~]$ pip install /home/Downloads/django/
      
## start  a Django Project  (django-admin, django-admin.py)
To start a Django project you must use the django-admin executable or django-admin.py script that
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
    
    • manage.py .- Runs project specific tasks. Just as django-admin is used to execute
 system wide Django tasks, manage.py is used to execute project specific tasks.
    • __init__.py .- Python file that allows Python packages to be imported from
 directories where it’s present. Note __init__.py is not Django specific, it’s a generic
 file used in almost all Python applications.
    • settings.py .- Contains the configuration settings for the Django project.
    • urls.py .- Contains URL patterns for the Django project.
    • wsgi.py .- Contains WSGI configuration properties for the Django project. WSGI is
 the recommended approach to deploy Django applications on production (i.e., to
 the public). You don’t need to set up WSGI to develop Django applications.      
      
### Start Django development web server on different address and port
1. Run the development server on the local address and port 4345 (http://127.0.0.1:4345/)
python manage.py runserver 4345

2. Run the dev server on the 96.126.104.88 address and port 80 (http://96.126.104.88/)
python manage.py runserver 96.126.104.88:80

3. Run the dev server on the 192.168.0.2 address and port 8888 (http://192.168.0.2:8888/)
python manage.py runserver 192.168.0.2:8888

## Using pdb to debug Django views
put this line of code
 into your view right before the point where you think the problem exists:


import pdb; pdb.set_trace()

Then, the next time you load the page associated with that view, you'll see that your

browser appears to not load anything. This is because your Django application is

now paused. If you look in the console where you ran the runserver command, you

should see a prompt for pdb. In the prompt, you can type the name of any variable

available in the current Python scope (usually the scope of the view that you are

debugging) and it will print the current value of that variable.
  * return HttpResponse({variable to inspect})

  * print {variable to inspect}

  * raise Exception({variable to inspect})


## Set Up a Database for a Django Project
In addition to SQLite, Django also has support for other popular databases that include PostgreSQL,
 MySQL, and Oracle. The Django configuration to connect to a database is done inside the settting.py file
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
Besides configuring Django to connect to a database, you’ll also need to install the necessary Python
 packages to communicate with your database brand.
#### Python packages for different databases
Database     Python package             pip installation syntax
PostgreSQL   psycopg2                   pip install psycopg2
MySQL        mysql-python               pip install mysql-python   //python3使用的是pip install PyMySQL  pip install mysqlclient
Oracle       cx_Oracle                  pip install cx_Oracle
SQLite       Included with Python 2.5+  N/A

pip install PyMySQL

### 修改mysql(MariaDB)root的密码：
ps -ef|grep mysqld  kill -9 mysqlxxx
#mysqld_safe --skip-grant-tables &
#mysql -u root
MariaDB [(none)]> use mysql;  
MariaDB [mysql]> UPDATE user SET password=password('newpassword') WHERE user='root';  
MariaDB [mysql]> flush privileges;   
MariaDB [mysql]> exit; 
4、关闭跳过授权启动的进程：
#kill -9 1441 
5、正常启动 mariadb：
#systemctl start mysql

### 创建mysql数据库

　　1、 CREATE DATABASE 数据库名;  CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; utf8_general_cs, utf8_bin区分大小写

　　2、 GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON 数据库名.* TO 数据库名@localhost IDENTIFIED BY '密码';

　　3、 SET PASSWORD FOR '数据库名'@'localhost' = OLD_PASSWORD('密码');

CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'djangouser';
GRANT ALL PRIVILEGES ON *.* TO 'djangouser'@'localhost' IDENTIFIED BY 'djangouser' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `coffeehouse` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
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

　　mysqldump -uroot -p --default-character-set=latin1 --set-charset=gbk --skip-opt database_name > outfile_name.sql
　　
　　
### Test Django Database Connection and Build Django Base Tables
1. [user@coffeehouse ~]$ python manage.py migrate

## set up content: understand urls, templates and Apps
Content in Django projects works with three major building blocks: urls, templates, and apps. 

Urls define the entry points or where to access content. Templates define the end points that give form
to the final content. And apps serve as the middleware between urls and templates, altering or adding
content from a database or user interactions. 

To run static content you only need to create and configure
 Django urls and templates. To run dynamic content - built from a database or user interactions - you need to
 create and configure Django apps, in addition to urls and templates.

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

# python manage.py和 python django-admin.py 
django-admin.py是django的一个用于管理任务的命令行工具，manage.py是对django-admin.py的简单包装，每个django project 里面都会包换一个manage.py

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


















