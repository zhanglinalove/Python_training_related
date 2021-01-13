# 作业说明6: 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。




from enum import unique
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import join
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import NullType

Base = declarative_base()

# 1 - 用户信息表 
# create table if not exists testdb.userinfo(
#   user_id   bigint comment '用户的user_id',
#   user_name string comment '用户的user_name'
# )

class User_table(Base):  
    __tablename__ = 'user_info'
    user_id       = Column(Integer()  , primary_key = True)
    user_name     = Column(String(100), unique = True)



# 2 - 资产表
# create table if not exists testdb.user_assets(
#   account_no   bigint  comment '账户id',
#   account_name string  comment '账户名称',
#   remain_amt   double  comment '账户余额',
#   user_id      bigint  comment '用户id'

# )
class Asserts_table(Base):  
    __tablename__ = 'user_asserts'
    account_no    = Column(Integer(), primary_key = True)
    account_name  = Column(String(100))
    remain_amt    = Column(Float())
    user_id       = Column(Integer(), ForeignKey("user_info.user_id"))


# 3 - 审计表
# create table if not exists testdb.audit_info(
#   payer_account_no bigint    comment '支付账户',
#   pay_time        datetime   comment '转账时间',
#   pay_amt         double     comment '转账金额',
#   payee_account_no bigint    comment '收款账户'
# )

class Audit_table(Base):  
    __tablename__ = 'user_audit'
    payer_account_no   = Column(Integer(), primary_key = True)
    pay_time           = Column(DateTime(), default = datetime.now)
    pay_amt            = Column(Float())
    payee_account_no   = Column(Integer())




def transfer_func(payer,payee,tranfer_amt,session):

    payer_user_id  = session.query(User_table.user_id).filter(User_table.user_name == payer).first()[0]


    payee_user_id = session.query(User_table.user_id).filter(User_table.user_name == payee).first()[0]
    

    payer_asserts_info = session.query(Asserts_table.account_no,Asserts_table.remain_amt).filter(Asserts_table.user_id == payer_user_id).first();
    payee_asserts_info = session.query(Asserts_table.account_no,Asserts_table.remain_amt).filter(Asserts_table.user_id == payee_user_id).first();
   
    payer_asserts_amt = payer_asserts_info[1] - 100
    payee_asserts_amt = payee_asserts_info[1] + 100


    asserts_data1 = session.query(Asserts_table.remain_amt).filter(Asserts_table.user_id == payer_user_id).update({Asserts_table.remain_amt:payer_asserts_amt});
    asserts_data2 = session.query(Asserts_table.remain_amt).filter(Asserts_table.user_id == payee_user_id).update({Asserts_table.remain_amt:payee_asserts_amt});

    
    
    # # 将转账记录插入流水表中
    audit_data = Audit_table(payer_account_no = payer_asserts_info[0] , pay_amt= tranfer_amt,payee_account_no = payee_asserts_info[0] )
    session.add(audit_data)

    session.commit()



# 实例一个引擎
dburl = "mysql+pymysql://root:365040382@localhost:3306/testdb?charset=utf8mb4"
engine =  create_engine(dburl, echo = True, encoding ="utf-8")


# 1- 创建表的操作，将Python的ORM映射为mysql的表
Base.metadata.create_all(engine)

# 2- 创建Session ，然后进行数据插入的操作

sessionClass = sessionmaker(bind=engine)
session = sessionClass()

# 实例化的userinfo
user_demo0 = User_table(user_id = 10001,user_name = "张三");
user_demo1 = User_table(user_id = 10002,user_name = "李四");
session.add(user_demo0)
session.add(user_demo1)
session.commit()  # 对于当前的事务，进行提交的操作。


# 实例化user_asserts,并将数据进行提交

assert_demo0= Asserts_table(account_no = 12345678, account_name ="中国银行", remain_amt = 100000, user_id = 10001)
assert_demo1= Asserts_table(account_no = 34789089, account_name ="建设银行", remain_amt = 300, user_id = 10002)
session.add(assert_demo0)
session.add(assert_demo1)
session.commit()

#  3- 进行相关的交易操作。
transfer_func("张三","李四",100,session)


























