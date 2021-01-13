from enum import unique
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime


# 作业6文字说明: 
# 张三给李四通过网银转账 100 极客币，现有数据库中三张表：一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

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

#  创建一个表，并将其实例化
#  实例一个引擎
dburl = "mysql+pymysql://root:365040382@localhost:3306/testdb?charset=utf8mb4"
engine =  create_engine(dburl, echo = True, encoding ="utf-8")


# 创建表的操作
Base.metadata.create_all(engine)

# 1- 创建一个Session，进行数据插入的操作










