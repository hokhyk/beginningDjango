mysql 在opensuse 上安装
2013年07月24日 17:09:14
阅读数：392

1. 1 zypper search   mysql*

1.2 zypper install   mysql-community-server

 默认目录： 

可执行文件目录：/usr/bin/mysql 

配置文件目录：/etc/mysql 

/数据存放目录：/var/lib/mysql/

配置文件目录：/usr/share/mysql 

/usr/share/man/man1/mysql.1.gz

2，启动服务 serveice mysql start 停止服务 service mysql stop 

3,客户端操作

 >mysql -u root -p 

4.增加用户及权限(否则外部主机无法访问到该数据库服务器)

授权法。例如，你想myuser使用mypassword从任何主机连接到mysql服务器的话。
 1.1 grant all on  *.* to  'baseuser'@'%' identified by 'base0001'
GRANT ALL PRIVILEGES ON *.* TO 'baseuser'@'%' IDENTIFIED BY 'base0001' WITH GRANT OPTION;
如果你想允许用户myuser从ip为192.168.1.3的主机连接到mysql服务器，并使用mypassword作为密码
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.10.40.54' IDENTIFIED BY '123456' WITH GRANT OPTION;

6,参考文档：

http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_lower_case_table_names



# 修改mysql(MariaDB)root的密码：
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

# 修改mysql字符集编码：

登录mysql查看：

SHOW VARIABLES LIKE 'character%';

SHOW VARIABLES LIKE 'collation%'; 

 

 

mysql> SHOW VARIABLES LIKE 'character%';

+-----------------------------------+-----------------------------------------+

| Variable_name                  | Value                                |

+------------------------------------+----------------------------------------+

| character_set_client          | utf8                                   |

| character_set_connection | utf8                                   |

| character_set_database    | latin1                                |

| character_set_filesystem   | binary                               |

| character_set_results        | utf8                                   |

| character_set_server        | latin1                                 |

| character_set_system       | utf8                                    |

| character_sets_dir            | /usr/share/mysql/charsets/ |

+------------------------------------+-------------------------------------------+

8 rows in set (0.00 sec)

 

 

mysql> SHOW VARIABLES LIKE 'collation%'; 

+--------------------------+-----------------------+

| Variable_name          | Value                   |

+--------------------------+-----------------------+

| collation_connection | utf8_general_ci    |

| collation_database   | latin1_swedish_ci  |

| collation_server        | latin1_swedish_ci  |

+--------------------------+-----------------------+

3 rows in set (0.00 sec)

 

为了防止出现乱码，修改数据库编码为UTF-8，拷贝mysql安装路径下的my-small.cnf、my-medium.cnf、my-large.cnf和my-huge.cnf中的一个放到/etc/下 并改名为my.cnf

其中拷贝需要按照机器的配置和数据库连接压力来，我拷贝的是my-medium.cnf文件，命令为：

cp /usr/share/mysql/my-medium.cnf /etc/my.cnf

编辑my.cnf文件：

vi /etc/my.cnf 

 

在[mysqld]下面增加：

character_set_server = utf8

collation-server=utf8_bin

init_connect='SET NAMES utf8'

在[client]下面增加：

default-character-set = utf8

在[mysql]下面增加：

default-character-set=utf8

 

 

保存并退出，然后重启mysql服务：/etc/init.d/mysql restart或service mysql restart

 

重启完毕，登录mysql，查询编码:

mysql> SHOW VARIABLES LIKE 'character%';

+----------------------------------+-----------------------------------+

| Variable_name                    | Value                                  |

+----------------------------------+-----------------------------------+

| character_set_client           | utf8                                       |

| character_set_connection  | utf8                                       |

| character_set_database     | utf8                                       |

| character_set_filesystem    | binary                                   |

| character_set_results         | utf8                                       |

| character_set_server          | utf8                                       |

| character_set_system         | utf8                                       |

| character_sets_dir              | /usr/share/mysql/charsets/    |

+----------------------------------+------------------------------------+

8 rows in set (0.00 sec)

 

mysql> SHOW VARIABLES LIKE 'collation%'; 

+--------------------------+---------------------+

| Variable_name          | Value                 |

+--------------------------+---------------------+

| collation_connection | utf8_general_ci  |

| collation_database   | utf8_bin              |

| collation_server        | utf8_bin              |

+--------------------------+---------------------+

3 rows in set (0.01 sec) 
