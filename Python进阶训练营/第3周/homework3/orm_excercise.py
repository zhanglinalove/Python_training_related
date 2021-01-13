from enum import unique
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime



# 作业2说明:使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，
# 并读取:【用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间。
# 将 ORM、插入、查询语句作为作业内容提交】

Base = declarative_base()

class User_table(Base):  
    __tablename__ = 'userorm'
    user_id          = Column(Integer(), primary_key = True)
    user_name        = Column(String(100), unique = True)
    age              = Column(Integer())
    birthday         = Column(String(20))
    sex              = Column(String(10))
    education_level  = Column(String(10))
    created_on       = Column(DateTime(), default = datetime.now)
    updated_on       = Column(DateTime(), default = datetime.now)

#  创建一个表，并将其实例化
#  实例一个引擎
dburl = "mysql+pymysql://root:365040382@localhost:3306/testdb?charset=utf8mb4"
engine =  create_engine(dburl, echo = True, encoding ="utf-8")


# 创建表的操作
Base.metadata.create_all(engine)



# 1- 创建一个Session，进行数据插入的操作

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

user_demo = User_table(user_id= 10010,
                       user_name= 'zhanglina1',
                       age= 31,
                       birthday= '2020-09-19',
                       sex= '女',
                       education_level= '本科'
                       )


user_demo1 = User_table(user_id= 10011,
                       user_name= 'lisi',
                       age= 32,
                       birthday= '2020-09-29',
                       sex= '女',
                       education_level= '研究生'
                       )



user_demo2 = User_table(user_id= 10012,
                       user_name= 'wangwu',
                       age= 33,
                       birthday= '2020-09-19',
                       sex= '女',
                       education_level= '研究生'
                       )

session.add(user_demo)
session.add(user_demo1)
session.add(user_demo2)
session.commit()


# 2- 创建一个Session，进行数据查询的操作

result = session.query(User_table.user_id,User_table.user_name,
                       User_table.age,
                       User_table.birthday,
                       User_table.created_on,
                       User_table.updated_on,
                       User_table.sex,
                       User_table.education_level
                       ).all()
for i in result:
    print(i)








