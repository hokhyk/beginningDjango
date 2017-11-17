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
      
## start  a Django Project
To start a Django project you must use the django-admin executable or django-admin.py script that comes with Django. 

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
