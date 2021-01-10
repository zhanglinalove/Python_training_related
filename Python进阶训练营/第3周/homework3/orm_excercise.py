from enum import unique
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

# class Book_table(Base):
#     __tablename__ = 'bookorm'
#     book_id = Column(Integer(), primary_key = True)
#     book_name = Column(String(50), Index = True)

#     def __repr__(self):
#         return "Book_table(book_id='{self.book_id}'," \
#             "book_name={self.book_name})".format(self=self)



class Author_table(Base):    
    __tablename__ = 'bookorm'
    user_id  = Column(Integer(), primary_key = True)
    user_name  = Column(String(15), nullable = False, unique = True)
    created_on = Column(DateTime(), default = datetime.now)
    updated_on = Column(DateTime(), default = datetime.now)


#  2.使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，
# 并读取:【用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间。
# 将 ORM、插入、查询语句作为作业内容提交】
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
dburl = "mysql+pymysql://root:365040382@192.168.3.32:3306/testdb?charset=utf8mb4"
engine =  create_engine(dburl, echo = True, encoding ="utf-8")

Base.metadata.create_all(engine)

# metadata = MetaData(engine)
# user_table = Table('userorm',metadata,
#     Column('user_id',Integer(), primary_key = True),
#     Column('user_name',String(30),nullable = False, unique = True),
#     Column('age',Integer(),  nullable = False),
#     Column('birthday',String(20), nullable = False),
#     Column('sex',String(10), nullable = False),
#     Column('education_level',String(10), nullable = False),
#     Column('created_on',DateTime(), default = datetime.now),
#     Column('updated_on',DateTime(), default = datetime.now)

# )

# try:
#     metadata.create_all()
# except Exception as e:
#     print(f'create table error{e}!')


# # 创建一个Session

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

user_demo = User_table(user_id= '123')
user_demo = User_table(user_name= 'zhanglina')
user_demo = User_table(age= '30')
user_demo = User_table(birthday= '2020-09-19')
user_demo = User_table(sex= '女')
user_demo = User_table(education_level= '本科')

session.add(user_demo)
session.commit()









