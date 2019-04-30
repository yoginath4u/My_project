import cx_Oracle
conn=cx_Oracle.connect("yogi/yogi@localhost/orcl")
cur=conn.cursor()
cur.execute("insert into yogi values(3,'c',200)")
cur.execute("commit")
cur.execute("select * from yogi")
for data in cur:
    print(data)