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

# 创建新的环境,位于 ~/.pyenv/versions/
$ pyenv virtualenv 2.7.9 2.7.9env

# 切换到新的环境
$ pyenv activate 2.7.9env

# 退回到系统环境
$ pyenv deactivate

# 删除新创建的环境
$ rm -rf ~/.pyenv/versions/2.7.9env/

# 1 installing Django
## installing virtualenv
