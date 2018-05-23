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
