'''
   以下是实际的作业完成情况，请参考如下的步骤，操作即可。
   练习的过程中，发现还是有些地方使用不熟悉，查询文档才知晓
'''


from sqlalchemy import create_engine
import pandas as pd

# 作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。
# 因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
# 作业要求：请将以下的 SQL 语句翻译成 pandas 语句：
# 1. SELECT * FROM data;
engine = create_engine("mysql+pymysql://root:365040382@localhost:3306/testdb")
data = pd.read_sql_query("select * from data", engine)

# 2. SELECT * FROM data LIMIT 10;
print(data.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列

print(data["id"])

# 4. SELECT COUNT(id) FROM data;

print(data["id"].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id'] < 1000) & (data['age'] > 30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(data[["id", "order_id"]].groupby("id").order_id.nunique())

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

t1 = pd.read_sql_query("select * from data", engine)
t2 = pd.read_sql_query("select * from data", engine)

print(pd.merge(t1, t2, how="inner", on="id"))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([t1, t2]).groupby(["id", "name", "birthday", "age", "order_id"]))

# 9. DELETE FROM table1 WHERE id=10;

print(data.drop(index=data[data["id"] == 5].index, inplace=True))
# print(data)

# 10. ALTER TABLE table1 DROP COLUMN column_name;

print(data.drop(columns=["name"], axis=1))
