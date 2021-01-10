特别说明: 本次作业，有部分在本机实现的时候，有卡壳的现象，需要资源助教及老师，确认问题的原因。
由于休息的比较晚，可能影响第二天的工作，所以存在问题的部分，待第二天继续进行研究

##### 1. 将增加远程用户的 SQL 语句作为作业内容提交
```
配置好mysql之后，让其可以允许其他机器进行远程连接。
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.3.32' IDENTIFIED BY '365040382' WITH GRANT OPTION;

配置完成之后，还要开启远程访问的权限,命令如下：
use mysql;
update user set host ='%' where user ='root';
select user,host from user;
flush privileges;  -- 使配置命令生效。

```

##### 2.使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:【用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间。将 ORM、插入、查询语句作为作业内容提交】

```


```





##### 3. 标注SQL的执行顺序

SELECT DISTINCT player_id, player_name, count(*) as num  5
FROM player JOIN team ON player.team_id = team.team_id   1
WHERE height > 1.80                                      2
GROUP BY player.team_id                                  3
HAVING num > 2                                           4
ORDER BY num DESC                                        6
LIMIT 2                                                  7





##### 4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

1)INNER JOIN

```
SQL 语句：
select t1.id,t1.name,t2.id,t2.name from table1 t1
  inner join table2 t2
     on t1.id = t2.id

SQL 查询结果语句：
1 table1_table2 1 table1_table2
```

2)LEFT JOIN

```
SQL 语句：
select t1.id,t1.name,t2.id,t2.name from table1 t1
  left join table2 t2
     on t1.id = t2.id

SQL 查询结果语句：
1 table1_table2 1    table1_table2
2 table1        null null


```

3)RIGHT JOIN

```
SQL 语句：
select t1.id,t1.name,t2.id,t2.name from table1 t1
  right join table2 t2
     on t1.id = t2.id


SQL 查询结果语句：
1 table1_table2  1    table1_table2
3 table2         null null
```

##### 5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。




##### 6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。