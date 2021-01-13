### mysql 安装过程中的学习笔记

##### Linux 上安装mysql 服务器有两种方式:
①可以用yum的方式来进行安装
A、yum install mysql57-community-release-el7-10.noarch.rpm，这个命令相当于创建了一个索引

B、安装完成之后，执行以下命令。
yum install mysql-community-server

C、安装完成mysql服务器之后，执行以下的命名来避免mysql版本的自动更新，移除索引

yum remove mysql57-community-release-el7-10.noarch



②可以将linux上的相关包下载下来，然后使用以下的命令进行安装
yum install *.rpm


##### Linux 安装完成MySQL之后，如何进行配置。

```
systemctl start mysqld.service  --- 启动mysql的服务
systemctl enable mysqld  --- 让mysql可以在Linux启动时，就可以自动启动

system status mysqld.service  --- 可以查看mysql的启动的状态

rpm -qa | grep -i 'mysql'  --- 可以查看安装了那些MySQL


----mysql 安装完成之后，会随机生成一个密码，这个密码在哪里找，通过以下的命令:

grep 'password' /var/log/mysqld.log| head -1

这个密码拿到之后，需要登录mysql数据库之后，进行密码的修改。

```


##### mysql 密码修改的命令：

alter user 'root'@'localhost' identified by '新的密码'。

但是这个密码的设置，服务器有一些强制性的要求，我们在哪里查看呢。

show variables like 'validate_password%'

可以通过以下的命令来调整密码复杂度的策略:

set global validate_password_policy = 0;
也可以修改其他的密码长度设置

set global validate_password_length = 9;

等等来调整mysql的密码策略。


##### 第一章节在Linux 安装mysql 遇到的主要问题是:

* 对于yum的这种安装方式不理解，找不到对应的包，群里的同学及老师帮助解答，然后才理解其含义，并成功的进行安装。
* 无网络环境的本地安装，总是无法成功，这个后期可以全部下载完成之后，进行安装尝试。
* 关于如何找这个包，还是需要仔细的问下这个同学。



##### 配置好mysql之后，让其可以允许其他机器进行远程连接。
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.3.32' IDENTIFIED BY '365040382' WITH GRANT OPTION;

配置完成之后，还要开启远程访问的权限,命令如下：
```
use mysql;
update user set host ='%' where user ='root';
select user,host from user;
flush privileges;  -- 使配置命令生效。
```


#####  作业1说明如下:
```
1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
将增加远程用户的 SQL 语句作为作业内容提交

具体的操作步骤如下:
①在 my.cnf 中进行一些字符集的修改 ,参考my.cnf 即可. 修改之后的字符集

+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+

② 创建 testdb的数据库
show create database testdb;                                                                               

testdb   | CREATE DATABASE `testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ |

③字符集的设置非常的重要。不建议自己在生产上进行操作。
④_ci 盒 _cs 分表表示大小写敏感与大小写不敏感。可以进行自行的设置。

set global collation_database='utf8mb4_unicode_cs' 创建大小写敏感的校对规则。

```






















