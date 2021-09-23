# coding: utf-8
# @TIME:2021/8/3 20:53
# @Author: ckj

import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

sql = "create table stocks (data text,tran text,symbol text, qtr real,price real)"

c.execute(sql)
c.execute("insert into stocks values ('2021-8-3','buy','rhat',100,35.14)")

conn.commit()
conn.close()
