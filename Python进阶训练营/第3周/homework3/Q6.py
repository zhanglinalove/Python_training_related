# 作业说明6: 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。


# create table if not exists testdb.userinfo(
#   user_id   bigint comment '用户的user_id',
#   user_name string comment '用户的user_name'
# )


# create table if not exists testdb.user_assets(
#   account_no   bigint  comment '账户id',
#   account_name string  comment '账户名称',
#   total_amt    double  comment '账户总额度',
#   remain_amt   double  comment '剩余总额度',
#   user_id      bigint  comment '用户id'

# )

# create table if not exists testdb.auditInfo(
#   payer_accountno bigint    comment '支付账户',
#   pay_time        datetime  comment '转账时间',
#   pay_amt         double    comment '转账金额',
#   payee_accountno bigint    comment '收款账户'
# )


from enum import unique
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class User_table(Base):  
    __tablename__ = 'user_info'
    user_id          = Column(Integer(), primary_key = True)
    user_name        = Column(String(100), unique = True)
    
class User_table(Base):  
    __tablename__ = 'user_asserts'
    user_id          = Column(Integer(), primary_key = True)
    user_name        = Column(String(100), unique = True)

class User_table(Base):  
    __tablename__ = 'user_audit'
    user_id          = Column(Integer(), primary_key = True)
    user_name        = Column(String(100), unique = True)

# 实例一个引擎
dburl = "mysql+pymysql://root:365040382@localhost:3306/testdb?charset=utf8mb4"
engine =  create_engine(dburl, echo = True, encoding ="utf-8")


# 创建表的操作
Base.metadata.create_all(engine)










