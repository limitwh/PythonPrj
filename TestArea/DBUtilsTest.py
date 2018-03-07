__author__ = 'limitwh'
#coding=utf-8
import pymysql
from DBUtils.PooledDB import PooledDB
pool = PooledDB(pymysql,5,host='localhost',user='pytest',passwd='password',db='JDdb',port=3306,charset="utf8")
conn = pool.connection()
cur=conn.cursor()
SearchSql="select * from goodstable "
try:
    cur.execute(SearchSql)    #执行sql语句
    results = cur.fetchall()    #获取查询的所有记录  
    print("Gid","Gname","Gprice","Gnum")  
    #遍历结果  
    for row in results :  
        Gid = row[0]  
        Gname = row[1]  
        Gprice = row[2]  
        Gnum = row[3]
        print(Gid,Gname,Gprice,Gnum)  
except Exception as e:  
    raise e  
finally: #关闭连接
	cur.close() 
	conn.close()